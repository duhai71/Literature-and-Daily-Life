#那时雨
#The_Rain_at_That_Time
#TRATT
init python:
    import os
    
    #b 加载歌词文件
    TRATT_raw = ""
    file_path = os.path.join(renpy.config.basedir, "game/Submods/Literature_and_Daily_Life/L&DL_Music/The_Rain_at_That_Time.txt")
    
    try:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
                # 尝试多种编码
                encodings = ['utf-8', 'gbk', 'latin-1']
                for encoding in encodings:
                    try:
                        TRATT_raw = content.decode(encoding)
                        break
                    except UnicodeDecodeError:
                        continue
                else:
                    # 所有编码都失败
                    ybwm_raw = '{"lrc":{"lyric":"[00:00.00]歌词文件解码失败"}}'
    except Exception as e:
        TRATT_raw = '{"lrc":{"lyric":"[00:00.00]读取歌词文件出错"}}'
    
    # 导入并初始化歌词播放器，传入歌曲总时长
    try:
        from netease_lyric_player import NeteaseLyricPlayer
        #歌曲总时长
        TRATT_player = NeteaseLyricPlayer(TRATT_raw, song_duration=218.0)
    except Exception as e:
        # 如果导入失败，创建一个空的播放器对象并输出日志
        TRATT_player = None
        store.mas_submod_utils.submod_log.warning("TRATT_player初始化失败")
label lad_show_text_v2:
    python:
        dissolvetime = 0.5
        if lad_duration_time > 2.0:
            dissolvetime = 0.2
        duration = lad_duration_time - dissolvetime * 2
        
        if lad_expression_code and lad_expression_code.strip():
            expr_code = lad_expression_code.strip()
            renpy.show("monika " + expr_code, zorder=20)
    
    show screen lad_texts(lad_eng_text, lad_chn_text)
    with Dissolve(dissolvetime)
    pause duration
    hide screen lad_texts
    with Dissolve(dissolvetime)
    return
# 事件定义
init 5 python:
    addEvent(Event(persistent.event_database,
        eventlabel="Monika_TRATT_again_rain_yu",
        category=["音乐"],
        prompt="你可以为我弹一首<那时雨>吗?",
        pool=False,
        unlocked=False
        )
    )


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
        eventlabel="LADL_TRATT_began",
        category=["音乐"],
        prompt="那时雨",
        pool=False,
        unlocked=False
        )
    )

label LADL_TRATT_began:
    $ mas_unlockEVL("Monika_TRATT_again_rain_yu", "EVE")
    if not persistent.monika_TRATT_v3_began_piano:
        m 5fua "真的吗?那太好了."
        m 3hub "我很高兴你能抽出时间."
        $ persistent.monika_TRATT_v3_began_piano = True
    m 1eua "嗯......我现在去准备."
    jump Monika_TRATT_v3



label Monika_TRATT_again_rain_yu(skip_leadin=False):
    m 5hua "好的."
    m 6fub "我现在准备一下."
    jump Monika_TRATT_v3
label Monika_TRATT_v3(skip_leadin=False):  
    $ lad_music = 0
    if TRATT_player:
        $ TRATT_player.reset()
    $HKBHideButtons()    
    show monika at Transform(xpos=-800) with move
    # 去搬钢琴
    pause 2.0
    window hide
    $ store.mas_sprites.zoom_out()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 40
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) zorder 20 with move
    if not persistent.monika_TRATT_v3_end:
        m 2fub "{b}{i}你说你是雨,划过我的脸际~~{/i}{/b}."
        m 2hua "{b}{i}就会变成泪滴,忘掉过去~~{/i}{/b}"
        $ persistent.monika_TRATT_v3_end = True
    $ mas_play_song("Submods/Literature_and_Daily_Life/L&DL_Assets/music/The_Rain_at_That_Time.mp3", loop=False)
    $ TRATT_player.play()
    show ladtback zorder 49 at lad_back with dissolve
    show monika 1eua zorder 20
    $ info = TRATT_player.get_current_lyric()



label TRATT_lyric_loop:
    if TRATT_player and TRATT_player._playing:
        $ info = TRATT_player.get_current_lyric()
        $ cl = info.current_lyric
        
        
        
        $ expression = cl.romalrc if cl.romalrc else ""
        
        $ lad_chn_text = cl.tlyric
        $ lad_eng_text = cl.lrc
        $ lad_expression_code = expression
        $ lad_duration_time = info.time_to_next
        
        call lad_show_text_v2
        if info.is_last:
            jump TRATT_lyric_end
        else:
            # 继续下一句
            jump TRATT_lyric_loop
    else:
        # 播放器未运行，直接结束
        jump TRATT_lyric_end 

label TRATT_lyric_end:
    hide screen lad_texts
    hide ladtback
    stop music
    $ lad_num = 0    
    

    jump TRATT_cleanup

label TRATT_cleanup:
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 1.0
    $ mas_unlockEVL("Monika_TRATT_again", "EVE")
    $ persistent._mas_disable_animations = False
    if not persistent.monika_TRATT_v3_end:
        m 3fua "如果可以的话,我也希望你能多听听这首歌的原曲."
        $ persistent.monika_TRATT_v3_end = True
    m 5hubfb "希望你喜欢."
    return
