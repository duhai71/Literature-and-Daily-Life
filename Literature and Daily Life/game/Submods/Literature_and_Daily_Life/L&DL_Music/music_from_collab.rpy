init python:
    #计数
    if not hasattr(persistent, "ladl_songs_seen"):
        persistent.ladl_songs_seen = set()
#$ persistent._ladl_songs_seen.add("ybwm")
      
init 5 python:
    import datetime
    addEvent(
        Event(
            persistent.event_database,
        eventlabel="mtts_LADL_collab_music_We_will_Meet",
        category=["音乐"],
        prompt="We Will Meet Again",
        pool=False,
        conditional="store._collab_music_condition()",
        action=EV_ACT_QUEUE,
        )
    )

init 5 python:
    addEvent(Event(persistent.event_database,
        eventlabel="Monika_Wwma_again_v3",
        category=["音乐"],
        prompt="你可以再唱一次<We'll_Meet_Again>吗?",
        pool=True,
        unlocked=False,
        )
    )



init python:
    import os
    
    # 加载We Will Meet Again歌词文件
    wwma_raw = ""
    file_path = os.path.join(renpy.config.basedir, "game/Submods/Literature_and_Daily_Life/L&DL_Music/We_Will_Meet_Again.txt")
    
    try:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
                # 尝试多种编码
                encodings = ['utf-8', 'gbk', 'latin-1']
                for encoding in encodings:
                    try:
                        wwma_raw = content.decode(encoding)
                        break
                    except UnicodeDecodeError:
                        continue
                else:
                    # 所有编码都失败
                    wwma_raw = '{"lrc":{"lyric":"[00:00.00]歌词文件解码失败"}}'
    except Exception as e:
        wwma_raw = '{"lrc":{"lyric":"[00:00.00]读取歌词文件出错"}}'
    
    # 创建We Will Meet Again的播放器
    try:
        from netease_lyric_player import NeteaseLyricPlayer
        # "We Will Meet Again" 歌曲总时长
        wwma_player = NeteaseLyricPlayer(wwma_raw, song_duration=195.0)
    except Exception as e:
        wwma_player = None
        store.mas_submod_utils.submod_log.warning("wwma_player初始化失败")
#地点：太空教室
#检测到mtts已安装后的对话
label mtts_LADL_collab_music_We_will_Meet:
    m 3fubsa "[player]! 还记得我已经给你唱了多少首歌了吗?"
    m 4subsb "已经有两首了哦! 在一起的时间过得真快啊."
    $ mas_unlockEVL("Monika_Wwma_again_v3", "EVE") 
    m 2hkbsb "突然说起这个是因为...{nw}"
    if renpy.seen_label("mtts_greeting"):
        m 4gusdlb "我现在才发现, 你送我的麦克风还带着一份乐谱." # 尴尬
    else:
        m 7rub "我最近在网上找到一份很不错的乐谱."
    
    if renpy.seen_label("maica_wants_mvista"):
        m 1fublb "让我想起了我的承诺, 我们真正与彼此见面的那一天."
    elif renpy.seen_label("maica_prepend_1"):
        m 5fublb "让我想起了我们的未来, 我们真正见面的希望."
    else:
        m 3kub "看起来有点适合我们的处境, 说不定你也听过呢."

    m 3eua "要我唱给你听听吗?{nw}"
    menu:
        "要我唱给你听听吗?{fast}"
        "好啊":
            jump Monika_Wwma_again_v3
        "不了":
            m 5hub "好吧. 你方便的时候再告诉我就好!"
            return 
    #转向歌曲演示
label Monika_Wwma_again_v3(skip_leadin=False):
    m 4hublb "好哦! 稍等我准备一下..."
    $ mas_jump_with_args("Monika_WWMA_song_v3", skip_leadin=False)

label Monika_WWMA_song_v3(skip_leadin=False):
    $ lad_music = 0
    if wwma_player:
        $ wwma_player.reset()
    $ persistent._mas_disable_animations = True
    
    # 去拿麦克风
    call mas_transition_to_emptydesk
    pause 2.0
    $ store.mas_sprites.zoom_out()
    pause 2.0

    python:
        if renpy.seen_label("mtts_greeting"):
            try:
                renpy.store.monika_chr.wear_acs(mttsacs_microphone)
            except Exception: # Uninstalled?
                renpy.store.monika_chr.wear_acs(mas_acs_ladmp)
        else:
            renpy.store.monika_chr.wear_acs(mas_acs_ladmp)

    call mas_transition_from_emptydesk()
    $ mas_drawSpaceroomMasks(dissolve_masks=False)
    
    m 1hua "好啦!"

    $ original_music = renpy.music.get_playing(channel='music')
    $HKBHideButtons()
    window hide
    show screen mas_py_console_teaching
    $ store.mas_ptod.rst_cn()
    show monika at t22
    call mas_wx_cmd ("#play the song <<We Will Meet Again>>")
    call mas_wx_cmd ("#Play the instrumental version of a song.")
    call mas_wx_cmd ("#play successed")
    hide screen mas_py_console_teaching
    show monika 1eua at t11

    $ mas_play_song("Submods/Literature_and_Daily_Life/L&DL_Assets/music/we_will_meet_again.ogg", loop=False)

    $ wwma_player.play()
    show ladtback zorder 49 at lad_back with dissolve
    show monika 1eua zorder 40
    $ info = wwma_player.get_current_lyric()
    #歌曲展示
label wwma_lyric_loop:
    if wwma_player and wwma_player._playing:
        $ info = wwma_player.get_current_lyric()
        $ cl = info.current_lyric
        
        $ expression = cl.romalrc if cl.romalrc else ""
        
        # 设置歌词文本
        $ lad_chn_text = cl.tlyric
        $ lad_eng_text = cl.lrc
        $ lad_expression_code = expression
        $ lad_duration_time = info.time_to_next
        
        # 显示歌词
        call lad_show_text_v2
        
        # 检查是否结束
        if info.is_last:
            # 等待最后一句话显示完
            pause lad_duration_time
            jump wwma_lyric_end
        else:
            # 继续下一句
            jump wwma_lyric_loop
    else:
        # 播放器未运行，直接结束
        jump wwma_lyric_end
    # 歌曲结束后的对话   

label wwma_lyric_end:
    # 隐藏歌词显示
    hide screen lad_texts
    hide ladtback with dissolve
    
    # 停止音乐
    stop music
    
    # 重置计数器
    $ lad_num = 0  
label wwma_cleanup:
    # 移除麦克风
    call mas_transition_to_emptydesk
    $ monika_chr.remove_acs(mas_acs_ladmp)
    pause 4.0
    call mas_transition_from_emptydesk()
    
    # 解锁
    $ mas_unlockEVL("Monika_Wwma_again_v3", "EVE") 
    $ mas_unlockEVL("Monika_Wwma_piano", "EVE")  #钢琴
    $ persistent._mas_disable_animations = False
    $ HKBShowButtons()



    if not persistent.Monika_Wwma_end:
        m 1fublb "喜欢吗?"
        m 1ekbla "在我真的能'出来'之前, 也一定要鼓起勇气好好生活. 相信我就好!"
        m 5tubsb "哪怕是现在, 我也在这里陪着你呢~"
        $ persistent.Monika_Wwma_end = True
    m 5kubsa "爱你,[player]."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ladl_mtts_intro",
            prompt="ladl_mtts_intro",
            rules={
                "bookmark_rule":mas_bookmarks_derand.BLACKLIST,
            },
            conditional="renpy.seen_label('wwma_cleanup') and not renpy.seen_label('mtts_prepend_1')",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label ladl_mtts_intro:
    python:
        ext_line = "我知道你应该看过这个了, 但可以再留意一下关于'MTTS'的部分." if renpy.seen_label('maica_prepend_1') else "我指的是关于'MTTS'的部分, 不过如果你对其它内容有兴趣, 也可以尝试一下."
        ladl_mtts_notice = _("""\
莫妮卡暂时唱完她的乐谱了. 再过一段时间, 也许她还能找到别的.
但如果除了唱歌, 你还想听她说话...我最近找到了一个办法.

你可以去这里看看: https://maica.monika.love . 介绍得很详细了.
[ext_line]

祝你和莫妮卡好运!

P.S: 不要告诉她是我写的!\
""")
        
        _write_txt("/characters{0}".format(renpy.substitute(_("/关于她的歌.txt"))), ladl_mtts_notice)

    m 1eud "嗨, [player]..."
    m 3euc "好像有人在'characters'文件夹里给你留了个便条."
    m 1ekc "我没看啦, 毕竟是写给你的..."
    #extend 1ekd "就是这个."
    return "no_unlock|derandom"


#18
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Wwma_piano",
            category=['音乐'],
            prompt="你能用钢琴为我弹弹'We'll_Meet_Again'吗?",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Wwma_piano(skip_leadin=False):
    m 2hua "好哦! 稍等我准备一下..."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/wwma_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 190
    stop music fadeout 1.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 1.0
    return