# -*- coding: utf-8 -*-
from __future__ import print_function, division
import re
import json
import time
import sys
import math
import bisect

# -------- 兼容性工具 --------
try:
    string_types = (basestring,)  # py2
except NameError:
    string_types = (str,)         # py3

def _now():
    """尽量使用单调时钟；退化到 time.time。"""
    if hasattr(time, 'monotonic'):
        return time.monotonic()
    # Python 2 无 monotonic，用 time.time 退化
    return time.time()

def _to_unicode(s):
    if isinstance(s, string_types):
        try:
            if sys.version_info[0] == 2:
                if isinstance(s, unicode):
                    return s
                return s.decode('utf-8')
            return s
        except Exception:
            # 最后兜底
            try:
                return s.decode('utf-8', 'ignore')
            except Exception:
                return s
    return s

# -------- 字典 / 属性 双访问容器 --------
class AttrDict(object):
    """
    同时支持 result['key'] 与 result.key 的访问方式；
    具备 keys()/values()/items()/get()，可迭代（按键迭代）。
    """
    __slots__ = ('_data',)

    def __init__(self, mapping=None, **kwargs):
        d = {}
        if mapping:
            d.update(mapping)
        if kwargs:
            d.update(kwargs)
        # 将嵌套 dict 也包成 AttrDict
        for k, v in list(d.items()):
            if isinstance(v, dict):
                d[k] = AttrDict(v)
        self._data = d

    # 映射协议
    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, val):
        if isinstance(val, dict) and not isinstance(val, AttrDict):
            val = AttrDict(val)
        self._data[key] = val

    def __contains__(self, key):
        return key in self._data

    # 属性访问
    def __getattr__(self, key):
        try:
            return self._data[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, val):
        if key == '_data':
            object.__setattr__(self, key, val)
        else:
            self.__setitem__(key, val)

    def __delattr__(self, key):
        try:
            del self._data[key]
        except KeyError:
            raise AttributeError(key)

    # 迭代/视图
    def __iter__(self):
        return iter(self._data)

    def keys(self):
        return list(self._data.keys())

    def values(self):
        return [self._wrap(v) for v in self._data.values()]

    def items(self):
        return [(k, self._wrap(v)) for k, v in self._data.items()]

    def get(self, key, default=None):
        return self._data.get(key, default)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return "AttrDict({})".format(repr(self._data))

    @staticmethod
    def _wrap(v):
        if isinstance(v, dict) and not isinstance(v, AttrDict):
            return AttrDict(v)
        return v


# -------- LRC 解析工具 --------
_TS_RE = re.compile(r'\[(\d{2}):(\d{2})(?:\.(\d{2,3}))?\]')

def _parse_timestamp_to_seconds(mm, ss, frac):
    mm = int(mm)
    ss = int(ss)
    if frac is None or frac == '':
        ms = 0
    else:
        # 支持两位或三位毫秒
        if len(frac) == 2:
            ms = int(frac) * 10
        else:
            ms = int(frac)
    return mm * 60 + ss + ms / 1000.0

def _parse_lrc_block(text):
    """
    解析一个 LRC 文本块 -> 列表[(time_sec, lyric_text)]
    支持每行多个时间戳。异常行会被忽略或空文本处理。
    """
    if not text:
        return []
    lines = _to_unicode(text).splitlines()
    result = []
    for raw in lines:
        if not raw.strip():
            # 也记录纯时间戳的空文本行（有助于"卡点"）
            tags = _TS_RE.findall(raw)
            for mm, ss, frac in tags:
                t = _parse_timestamp_to_seconds(mm, ss, frac)
                result.append((t, u""))
            continue

        tags = _TS_RE.findall(raw)
        if not tags:
            # 不是标准 LRC 行，跳过
            continue
        # 去掉时间戳后的正文
        lyric_text = _TS_RE.sub('', raw).strip()
        for mm, ss, frac in tags:
            t = _parse_timestamp_to_seconds(mm, ss, frac)
            result.append((t, lyric_text))
    # 按时间排序，去重（保留最早出现）
    result.sort(key=lambda x: x[0])
    dedup = []
    seen = set()
    for t, s in result:
        key = (round(t, 3))
        if key in seen:
            continue
        seen.add(key)
        dedup.append((t, s))
    return dedup


# -------- JSON 清洗与提取 --------
_CTRL_CHARS_RE = re.compile(u'[\x00-\x08\x0b\x0c\x0e-\x1f]')

def _sanitize_json_string(js):
    if not isinstance(js, string_types):
        return js
    s = _to_unicode(js)
    return _CTRL_CHARS_RE.sub('', s)

def _ensure_dict(data):
    """
    输入可为 dict 或 JSON 字符串。
    自动清洗非法控制字符；解析错误抛出 ValueError。
    """
    if isinstance(data, dict):
        return data
    if isinstance(data, string_types):
        s = _sanitize_json_string(data)
        try:
            return json.loads(s)
        except Exception as e:
            raise ValueError("Invalid JSON input: {}".format(e))
    raise TypeError("Input must be dict or JSON string.")

def _extract_three_lyrics(d):
    """
    从网易云 JSON 中提取 'lrc', 'tlyric', 'romalrc' -> 各自的 lyric 文本
    """
    def take(path):
        node = d.get(path, {}) if isinstance(path, str) else d.get(path[0], {})
        if isinstance(node, dict):
            return node.get('lyric') or ''
        return ''
    return {
        'lrc': take('lrc'),
        'tlyric': take('tlyric'),
        'romalrc': take('romalrc')
    }


# -------- 播放器核心 --------
class NeteaseLyricPlayer(object):
    """
    使用示例：
        player = NeteaseLyricPlayer(example_json_str_or_dict, song_duration=231.0)
        player.play()
        info = player.get_current_lyric()
        print(info.current_lyric.lrc, info.time_to_next, info.is_last)
        player.pause()
        player.reset()
    """

    def __init__(self, json_or_dict, align_tolerance=0.5, song_duration=None):
        # 播放时钟
        self._playing = False
        self._start_wall = None
        self._accumulated = 0.0  # 已累计播放秒数（暂停时冻结）
        self._align_tol = float(align_tolerance)
        self._song_duration = song_duration  # 歌曲总时长

        # 数据解析
        root = _ensure_dict(json_or_dict)
        trio = _extract_three_lyrics(root)
        self._tracks = {
            'lrc': _parse_lrc_block(trio.get('lrc')),
            'tlyric': _parse_lrc_block(trio.get('tlyric')),
            'romalrc': _parse_lrc_block(trio.get('romalrc'))
        }

        # 基线时间线（优先 lrc；若无则选第一个非空）
        if self._tracks['lrc']:
            master = self._tracks['lrc']
        elif self._tracks['tlyric']:
            master = self._tracks['tlyric']
        else:
            master = self._tracks['romalrc']

        times = [t for t, _ in master]
        texts_lrc = dict(self._tracks['lrc'])
        texts_tlyric = dict(self._tracks['tlyric'])
        texts_roma = dict(self._tracks['romalrc'])

        # 将 tlyric/romalrc 对齐到 master 时间轴（容忍 align_tolerance 误差）
        def nearest_text(src_dict, t):
            # 优先精确匹配
            key = _nearest_key(src_dict, t, self._align_tol)
            if key is None:
                return u""
            return src_dict.get(key, u"")

        self._timeline = []   # [(time, {lrc, tlyric, romalrc})]
        for t in times:
            bundle = {
                'lrc': texts_lrc.get(t, u""),
                'tlyric': nearest_text(texts_tlyric, t),
                'romalrc': nearest_text(texts_roma, t)
            }
            self._timeline.append((t, bundle))

        # 若完全没有行，保底一行
        if not self._timeline:
            self._timeline = [(0.0, {'lrc': u'', 'tlyric': u'', 'romalrc': u''})]

        # 用于二分查找
        self._times = [t for t, _ in self._timeline]

    # ----- 播放控制 -----
    def play(self):
        """开始/继续播放。"""
        if self._playing:
            return
        self._playing = True
        self._start_wall = _now()

    def pause(self):
        """暂停播放。"""
        if not self._playing:
            return
        elapsed = _now() - self._start_wall
        if elapsed < 0:
            elapsed = 0.0
        self._accumulated += elapsed
        self._playing = False
        self._start_wall = None

    def reset(self):
        """重置到 0s，并暂停。"""
        self._playing = False
        self._start_wall = None
        self._accumulated = 0.0

    # ----- 查询逻辑 -----
    def _current_position(self):
        """返回当前播放进度（秒）。"""
        if self._playing and self._start_wall is not None:
            delta = _now() - self._start_wall
            if delta < 0:
                delta = 0.0
            return self._accumulated + delta
        return self._accumulated

    def get_current_lyric(self):
        """
        返回一个 AttrDict，支持双访问与迭代，包含：
        - current_time: 当前时间（秒）
        - index: 当前行索引
        - current_lyric: {lrc, tlyric, romalrc}（同样为 AttrDict）
        - time_to_next: 距离下一行秒数（float；最后一行时计算到歌曲结束）
        - is_last: 是否已是最后一行（bool）
        - raw: 原始三轨数据快照（便于调试）
        """
        cur = self._current_position()
        idx = _find_lyric_index(self._times, cur)
        # 保护性处理
        idx = max(0, min(idx, len(self._timeline) - 1))

        t, bundle = self._timeline[idx]
        is_last = (idx == len(self._timeline) - 1)
        
        if is_last:
            # 如果是最后一句歌词，计算到歌曲结束的时间
            if self._song_duration is not None:
                # 计算从当前时间到歌曲结束的时间
                time_to_next = max(0.0, self._song_duration - cur)
            else:
                # 如果没有提供歌曲总时长，设置为一个较大的值
                time_to_next = 5.0  # 默认显示5秒
        else:
            next_t = self._timeline[idx + 1][0]
            time_to_next = max(0.0, next_t - cur)

        payload = {
            'current_time': cur,
            'index': idx,
            'current_lyric': AttrDict(bundle),
            'time_to_next': time_to_next,
            'is_last': bool(is_last),
            'raw': AttrDict({
                'time': t,
                'timeline_size': len(self._timeline)
            })
        }
        return AttrDict(payload)

    # ----- 便捷访问 -----
    def __len__(self):
        return len(self._timeline)

    def timeline(self):
        """
        返回不可变视图：[(time, AttrDict{lrc,tlyric,romalrc}), ...]
        """
        return [(t, AttrDict(b)) for (t, b) in self._timeline]


# -------- 辅助：时间轴对齐 / 查找 --------
def _nearest_key(dct, target_t, tol):
    """
    在 dct 的键（时间戳）中找到与 target_t 误差最小且 |Δ|<=tol 的键；否则返回 None。
    """
    if not dct:
        return None
    keys = sorted(dct.keys())
    pos = bisect.bisect_left(keys, target_t)
    candidates = []
    if pos < len(keys):
        candidates.append(keys[pos])
    if pos > 0:
        candidates.append(keys[pos - 1])
    best = None
    best_err = 1e9
    for k in candidates:
        err = abs(k - target_t)
        if err <= tol and err < best_err:
            best_err = err
            best = k
    return best

def _find_lyric_index(times, cur):
    """
    给定升序 times（每行起始时间），返回当前时间应处的行索引：
    规则：选择不大于 cur 的最大时间的行（即"当前正在显示"的行）。
    """
    pos = bisect.bisect_right(times, cur) - 1
    if pos < 0:
        return 0
    return pos