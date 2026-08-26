#手写的从前
#Once_upon_a_time_of_Handwriting
#ouatoh
init python:
    import os
    
    #b 加载歌词文件
    ouatoh_raw = ""
    file_path = os.path.join(renpy.config.basedir, "game/Submods/Literature_and_Daily_Life/L&DL_Music/手写的从前.txt")
    
    try:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
                # 尝试多种编码
                encodings = ['utf-8', 'gbk', 'latin-1']
                for encoding in encodings:
                    try:
                        ouatoh_raw = content.decode(encoding)
                        break
                    except UnicodeDecodeError:
                        continue
                else:
                    # 所有编码都失败
                    ybwm_raw = '{"lrc":{"lyric":"[00:00.00]歌词文件解码失败"}}'
    except Exception as e:
        ouatoh_raw = '{"lrc":{"lyric":"[00:00.00]读取歌词文件出错"}}'
    
    # 导入并初始化歌词播放器，传入歌曲总时长
    try:
        from netease_lyric_player import NeteaseLyricPlayer
        #歌曲总时长
        ouatoh_player = NeteaseLyricPlayer(ouatoh_raw, song_duration=299.0)
    except Exception as e:
        # 如果导入失败，创建一个空的播放器对象并输出日志
        ouatoh_player = None
        store.mas_submod_utils.submod_log.warning("ouatoh_player初始化失败")
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
    import datetime
    addEvent(Event(persistent.event_database,
        eventlabel="Monika_ouatoh_again",
        category=["音乐"],
        prompt="你可以再弹一次<手写的从前>吗?",
        pool=False,
        unlocked=False
        )
    )


init 5 python:
    import datetime
    addEvent(
        Event(
            persistent.event_database,
        eventlabel="ouatoh_LADL_piano",
        category=["音乐"],
        prompt="手写的从前",
        pool=False,
        conditional="store._ouatoh_music_condition()",
        action=EV_ACT_QUEUE,
        )
    )

label ouatoh_LADL_piano:
    m 1eud "嘿,[player]."
    $ mas_unlockEVL("ladl_piano_Subtitles_song", "EVE")
    m 3eub "在那次外出到海滩玩的时候,我从未如此开心过."
    m 5hua "阳光、大海、沙子、以及......{w=1}你."
    m 6eub "所以我回来了之后,在网上找到了一首曲子."
    m 3fua "特地弹给你听听."
    m 2hub "嗯,我现在去准备一下."
    jump Monika_ouatoh_v3



label Monika_ouatoh_again(skip_leadin=False):
    m 1hua "好的."
    m 2fub "我现在去把钢琴推过来."
    jump Monika_ouatoh_v3
label Monika_ouatoh_v3(skip_leadin=False):  
    $ lad_music = 0
    if ouatoh_player:
        $ ouatoh_player.reset()
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
    if not persistent.monika_ouatoh_v3_end:
        m 2fub "这首歌就是,手写的从前."
        $ persistent.monika_ouatoh_v3_end = True
    $ mas_play_song("Submods/Literature_and_Daily_Life/L&DL_Assets/music/手写的从前.mp3", loop=False)
    $ ouatoh_player.play()
    show ladtback zorder 49 at lad_back with dissolve
    show monika 1eua zorder 20
    $ info = ouatoh_player.get_current_lyric()



label ouatoh_lyric_loop:
    if ouatoh_player and ouatoh_player._playing:
        $ info = ouatoh_player.get_current_lyric()
        $ cl = info.current_lyric
        
        
        
        $ expression = cl.romalrc if cl.romalrc else ""
        
        $ lad_chn_text = cl.tlyric
        $ lad_eng_text = cl.lrc
        $ lad_expression_code = expression
        $ lad_duration_time = info.time_to_next
        
        call lad_show_text_v2
        if info.is_last:
            jump ouatoh_lyric_end
        else:
            # 继续下一句
            jump ouatoh_lyric_loop
    else:
        # 播放器未运行，直接结束
        jump ouatoh_lyric_end 

label ouatoh_lyric_end:
    hide screen lad_texts
    hide ladtback
    stop music
    $ lad_num = 0    
    

    jump ouatoh_cleanup

label ouatoh_cleanup:
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 1.0
    $ mas_unlockEVL("Monika_ouatoh_again", "EVE")
    $ persistent._mas_disable_animations = False
    if not persistent.monika_ouatoh_v3_end:
        m 3hublb "{b}我傻傻等待 傻傻等春暖花开~~{/b}."
        m 3eubfb "{b}等终等于等明等白 等爱情回来~~{/b}."
        m 1fubla "{b}青春属于表白 阳光属于窗台~~{/b}."
        m 6hubfb "{b}而我想我属于一个拥有你的未来~~{/b}."
        $ persistent.monika_ouatoh_v3_end = True
    m 5hubfb "希望你喜欢."#对话后面补
    return
