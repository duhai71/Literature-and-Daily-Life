init -977 python:
    import datetime
    if not hasattr(persistent, "lad_music_ready_time"):
        persistent.lad_music_ready_time = None
    def _lad_musicty_condition():
        #1.事件完成
        if (store.mas_getEVL_shown_count("lad_music1") >= 1 and
                store.mas_getEVL_shown_count("Monika_LADL_date_v3") >= 1):
        #2.
            if persistent.lad_music_ready_time is None:
                persistent.lad_music_ready_time = datetime.datetime.now()
                return False 
            time_passed = datetime.datetime.now() - persistent.lad_music_ready_time
            return time_passed >= datetime.timedelta(hours=24)  
        else:
            # 如果事件没完成,重置时间
            persistent.lad_music_ready_time = None
            return False 
    def _collab_music_condition(): 
        # 1
        if store.mas_getEVL_shown_count("lad_music_ty") >= 1:
            # 2. 等待
            if persistent.collab_music_ready_time is None:
                persistent.collab_music_ready_time = datetime.datetime.now()
                return False
            time_passed = datetime.datetime.now() - persistent.collab_music_ready_time
            return time_passed >= datetime.timedelta(hours=120) #
        else:
            # 重置时间
            persistent.collab_music_ready_time = None
            return False   
    def _ouatoh_music_condition(): 
        # 1
        if store.mas_getEVL_shown_count("Monika_LADL_date_v3") >= 1:
            # 2. 等待
            if persistent.ouatoh_music_ready_time is None:
                persistent.ouatoh_music_ready_time = datetime.datetime.now()
                return False
            time_passed = datetime.datetime.now() - persistent.ouatoh_music_ready_time
            return time_passed >= datetime.timedelta(hours=72) #
        else:
            # 重置时间
            persistent.ouatoh_music_ready_time = None
            return False        


init 5 python:
    import datetime
    addEvent(
        Event(
        persistent.event_database,
        eventlabel="lad_music_ty",
        category=["音乐"],
        prompt="thank you",#第一次约会后触发
        pool=False,
        conditional="store._lad_musicty_condition()",
        action=EV_ACT_QUEUE,
        )
    )
init 5 python:
    addEvent(Event(persistent.event_database,
        eventlabel="Monika_ty_again_v3",
        category=["音乐"],
        prompt="你可以为我再唱一次<thank you>吗?",
        pool=True,
        unlocked=False,
        )
    )
init python:
    import os
    
    # 加载歌词文件
    ty_raw = ""
    file_path = os.path.join(renpy.config.basedir, "game/Submods/Literature_and_Daily_Life/L&DL_Music/thank_you.txt")
    
    try:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                content = f.read()
                # 尝试多种编码
                encodings = ['utf-8', 'gbk', 'latin-1']
                for encoding in encodings:
                    try:
                        ty_raw = content.decode(encoding)
                        break
                    except UnicodeDecodeError:
                        continue
                else:
                    # 所有编码都失败
                    ty_raw = '{"lrc":{"lyric":"[00:00.00]歌词文件解码失败"}}'
    except Exception as e:
        ty_raw = '{"lrc":{"lyric":"[00:00.00]读取歌词文件出错"}}'
    
    # 导入并初始化歌词播放器,传入歌曲总时长
    try:
        from netease_lyric_player import NeteaseLyricPlayer
        #thank you 总时长 216.0 秒
        ty_player = NeteaseLyricPlayer(ty_raw, song_duration=216.0)
    except Exception as e:
        # 如果导入失败,创建一个空的播放器对象并输出日志
        ty_player = None
        store.mas_submod_utils.submod_log.warning("ty_player初始化失败")
        
image lad_etext:
    Text(lad_etext1[lad_music][lad_num], style="monika_lad_etext")

image lad_ctext:
    Text(lad_ctext1[lad_music][lad_num], style="monika_lad_ctext")

screen lad_texts(etext, ctext):
    frame:
        background None
        xalign 0.5
        yalign 0.68
        has vbox
        text etext style "monika_lad_etext" at lad_english
        text ctext style "monika_lad_ctext" at lad_chinese

label lad_show_text():
    hide lad_etext 
    hide lad_ctext 
    show lad_ctext zorder 50 at lad_chinese with dissolve
    show lad_etext zorder 50 at lad_english with dissolve
    $ lad_num += 1
    return
label lad_show_text_v2:
    python:
        dissolvetime = 0.5
        if lad_duration_time > 2.0:
            dissolvetime = 0.2
        duration = lad_duration_time - dissolvetime * 2
        
        if lad_expression_code and lad_expression_code.strip():
            expr_code = lad_expression_code.strip()
            renpy.show("monika " + expr_code)
    
    show screen lad_texts(lad_eng_text, lad_chn_text)
    with Dissolve(dissolvetime)
    pause duration
    hide screen lad_texts
    with Dissolve(dissolvetime)
    return       
#$ persistent._ladl_songs_seen.add("thank_you")
#第二首 thank you
label lad_music_ty:
    m 1eua "嘿,[player]."
    m 3eud "我们在这度过了一段很长的时间,不是吗?"
    m 5tua "我记得在这些天,我们说过了很多人、说过许多现象、说过各种各样的奇闻异事."#唱完说
    m 3eud "在和你去到了海边之后,我也说了我因为曾经的事引发的心结."
    m 6eub "在解开那个由往事形成的心结时,我心中有一种释然的感觉"
    m 1fublb "因为你,[player],你总是能让我倾诉这些心事."
    m 3eubfb "为此,我在回来之后的这段时间练习一首曲子,正好我想唱给你听听."
    m 3fua "为你而唱的歌,[player]."
    m 5eublb "好了好了,我现在就去准备下......"
    jump Monika_ty_v3

label Monika_ty_again_v3(skip_leadin=False):
    m 5hubla "好的."
    m 1hublb "让我再去准备一下伴奏和麦克风."
    jump Monika_ty_v3

label Monika_ty_v3(skip_leadin=False):
    if ty_player:
        $ ty_player.reset()
    $ lad_music = 0
    $ persistent._mas_disable_animations = True
    
    # 去拿麦克风
    call mas_transition_to_emptydesk
    pause 2.0
    $ store.mas_sprites.zoom_out()
    pause 2.0
    $ renpy.store.monika_chr.wear_acs(mas_acs_ladmp)
    call mas_transition_from_emptydesk()
    $ mas_drawSpaceroomMasks(dissolve_masks=False)
    
    m 1hua "希望你会喜欢......"####################

    $ original_music = renpy.music.get_playing(channel='music')
    $HKBHideButtons()
    window hide
    show screen mas_py_console_teaching
    $ store.mas_ptod.rst_cn()
    show monika at t22
    call mas_wx_cmd ("#play the song <<thank you>>")
    call mas_wx_cmd ("#Play the instrumental version of a song.")
    call mas_wx_cmd ("#play successed")
    hide screen mas_py_console_teaching
    show monika 1eua at t11
    
    
    # 开始播放音乐
    $ mas_play_song("Submods/Literature_and_Daily_Life/L&DL_Assets/music/thank_you.ogg", loop=False)
    
    # 检查播放器是否初始化成功


    
    $ ty_player.play()
    show ladtback zorder 49 at lad_back with dissolve
    show monika 1eua zorder 40
    $ info = ty_player.get_current_lyric()

label ty_lyric_loop:
    if ty_player and ty_player._playing:
        $ info = ty_player.get_current_lyric()
        $ cl = info.current_lyric
        
        
        
        $ expression = cl.romalrc if cl.romalrc else ""
        
        $ lad_chn_text = cl.tlyric
        $ lad_eng_text = cl.lrc
        $ lad_expression_code = expression
        $ lad_duration_time = info.time_to_next
        
        call lad_show_text_v2
        
        
        # 检查是否结束
        if info.is_last:
            jump ty_lyric_end
        else:
            # 继续下一句
            jump ty_lyric_loop
    else:
        # 播放器未运行,直接结束
        jump ty_lyric_end
    
label ty_lyric_end:
    hide screen lad_texts
    hide ladtback
    stop music
    $ lad_num = 0    
    

    jump ty_cleanup



label ty_cleanup:
    call mas_transition_to_emptydesk
    $ monika_chr.remove_acs(mas_acs_ladmp)
    pause 4.0
    call mas_transition_from_emptydesk()
    
    $ mas_unlockEVL("Monika_ty_again_v3", "EVE")
    $ persistent._mas_disable_animations = False
    $HKBShowButtons()
    
    # 歌曲结束后的对话
    if not persistent.monika_ty_v3_end:
        m 5hublb "我还是想再说一遍,[player],谢谢你."
        m 1eubfb "感谢你,让我能说出自己的心里话."
        m 3fubla "让我能够直面自己的过去."
        m 2hubfb "同时,我也希望......我们俩都好好的."
        $ persistent.monika_ty_v3_end = True
    m 5fubfb "爱你,[player]."
    return "love"

