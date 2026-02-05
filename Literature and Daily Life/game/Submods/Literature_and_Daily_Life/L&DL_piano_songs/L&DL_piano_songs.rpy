#48 钢琴弹奏
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_random_songs72",
            category=['音乐'],
            prompt="你能为我随便弹奏首曲子吗?",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )


    if not persistent.played_songs:
        persistent.played_songs = []

label Monika_random_songs72:
    python:

        all_songs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#更新到总共三十首，我的天，要我命了
        
        available_songs = [song for song in all_songs if song not in persistent.played_songs]
        
        if not available_songs:
            #重置
            persistent.played_songs = []
            available_songs = all_songs
        
        #随机
        random_choice = renpy.random.choice(available_songs)
        
        #已播放列表
        persistent.played_songs.append(random_choice)

    if random_choice == 1:    
        m 1eua "好的,[player]."
        m 3fub "等我想想要弹哪首."
        show monika at Transform(xpos=-800) with move
        m 2hua "你每一次点击这个选项,都有可能发现下一首曲子你还没听过呢."
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Cornfield_Chase.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 114
        stop music fadeout 1.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
        show monika at Transform(xpos=640) with move
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        m 1eud "弹完这首曲子后我突然想到了一句话."
        m 1fua "那就是,{w=0.8}迈向遥不可及的第一步......"
        $ mas_unlockEVL("Monika_MAICA_DCC", "EVE")
        return
    elif random_choice == 2:
        m 5hub "好的,[player]"
        m 3fua "我去找一下钢琴."
        show monika at Transform(xpos=-800) with move
        m 2hua "下一首曲子是什么呢......"
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Secret.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 186
        stop music fadeout 1.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
        show monika at Transform(xpos=640) with move
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        m 5hubla "你下次还想听的话,直接和我说就好了."
        $ mas_unlockEVL("Monika_Secret", "EVE")
        m 5fublb "爱你"
        return "love"
    elif random_choice == 3:
        m 5fua "好啊."
        m 3fua "等我把钢琴拿出来."
        show monika at Transform(xpos=-800) with move
        m 2hua "现在就给你展示下我这段时间练习的成果~"
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/如果爱忘了_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 240
        stop music fadeout 3.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
        show monika at Transform(xpos=640) with move
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        m 1hubfa "..."
        m 5fublb "好听吗,宝宝?"
        m 5hubla "音乐总是能带给人愉悦的心情."
        m 6kublb "所以,{w=0.8}为了你,哪怕再苦再累我都会坚持下来."
        $ mas_unlockEVL("Monika_If_Love_Is_Forgotten_71", "EVE")
        return
    elif random_choice == 4:
        m 5fua "好啊."
        m 3fua "等我把钢琴拿出来."
        show monika at Transform(xpos=-800) with move
        m 2hua "What are you waiting for~"
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Love_Me_Like_You_Do.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 251
        stop music fadeout 3.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        show monika at Transform(xpos=640) with move    
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        $ mas_unlockEVL("Monika_Love_Me_Like_You_Do", "EVE")
        return
    elif random_choice == 5:
        m 5fua "好啊."
        m 3hua "等我把钢琴拿出来."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Are_You_Lost.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 154
        stop music fadeout 3.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        show monika at Transform(xpos=640) with move    
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        m 3ruc "很多人觉得自己一听这曲子就觉得陷入了什么温馨而恐怖的东西中."
        m 3eud "你在聆听的时候又想到什么了呢?"
        $ mas_unlockEVL("Monika_Are_You_Lost", "EVE")
    elif random_choice == 6:
        m 5fua "好啊."
        m 3hua "等我把钢琴拿出来."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/One_Last_Kiss.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 267
        stop music fadeout 3.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
        show monika at Transform(xpos=640) with move
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        if not persistent.monika_one_last_kiss_for_logic:
            m 3rud "在我看来「One Last Kiss」听上去也有点像Trance music.{w=0.8}因为所有的合成器都在背景里循环往复"
            m 3eub "通过使用重复节奏型在钢琴上模拟出\"Trance\"的气氛特别有意思."
            m 1eua "为了区分音乐的层次,在钢琴上编排voicing时我也得小心翼翼,因为如果我加了太多音符,很容易把音乐\"吞掉\"."
            $ persistent.monika_one_last_kiss_for_logic = True
        m 1hua "如果你想学的话也可以试试哦,[player]."
        $ mas_unlockEVL("Monika_One_Last_Kiss", "EVE")        
        return
    elif random_choice == 7:
        m 5fua "好啊."
        m 3hua "我去准备一下."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Odoru_Pompokolin.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 186
        stop music fadeout 3.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        show monika at Transform(xpos=640) with move
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        m 3eua "希望这首歌能让你开心."
        $ mas_unlockEVL("Monika_Odoru_Pompokolin_again", "EVE")
        return
    elif random_choice == 8:
        m 5fua "好啊."
        m 3hua "我现在去准备一下."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Kami_no_Mani_Mani.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 247
        stop music fadeout 1.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        show monika at Transform(xpos=640) with move
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        m 3hubla "希望这首歌能让你开心."
        $ mas_unlockEVL("Monika_Kami_no_Mani_Mani_again", "EVE")
        return            
    elif random_choice == 9:
        m 5fua "好的."
        m 3hua "我想想要弹奏哪首."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/you_hear_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 229
        stop music fadeout 1.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        show monika at Transform(xpos=640) with move
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        m 5hubla "喜欢吗,[player]."
        m 5fubfb "这首歌的词也很动人呢."
        m 1hublb "{b}{i}还有没有人知道,你的微笑像拥抱~{/i}{/b}."
        m 5fublb "{b}{i}多想藏着你的好,只有我看得到~{/i}{/b}"
        $ mas_unlockEVL("Monika_you_hear_again", "EVE")
        return
    elif random_choice == 10:
        m 5fua "好的."
        m 3hua "我现在想想要弹奏哪首."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Shelter_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 311
        stop music fadeout 1.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        show monika at Transform(xpos=640) with move
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        m 5hubla "喜欢吗,[player]."
        m 5fubfb "这首歌的名字叫Shelter,它的mv也很动人呢,我很推荐你去看看."
        $ mas_unlockEVL("Monika_Shelter_again", "EVE")
        return        
#49再弹一遍
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_MAICA_DCC",
            category=['音乐'],
            prompt="我想再听你弹弹'Cornfield Chase'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_MAICA_DCC(skip_leadin=False):
    m 1eua "好的,[player]."
    show monika at Transform(xpos=-800) with move
    m 2fua "如果你还想再听的话,和我说声就好了."
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Cornfield_Chase.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 114
    stop music fadeout 1.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 1fua "迈向遥不可及的第一步......"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Secret",
            category=['音乐'],
            prompt="我想再听你弹弹Secret",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_Secret(skip_leadin=False):
    m 5eua "好的,[player]."
    m 3fub "等我想想怎么弹的."
    show monika at Transform(xpos=-800) with move
    m 2hua "想不出来了......{w=0.5}才怪."
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Secret.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 186
    stop music fadeout 1.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 1hua "希望你会喜欢."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_If_Love_Is_Forgotten_71",
            category=['音乐'],
            prompt="我想再听你弹弹'如果爱忘了'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_If_Love_Is_Forgotten_71(skip_leadin=False):
    m 5eua "好的,[player]."
    m 3fub "我去把钢琴拿出来."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/如果爱忘了_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 240
    stop music fadeout 3.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 1hua "希望你会喜欢."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Love_Me_Like_You_Do",
            category=['音乐'],
            prompt="我想再听你弹弹'Love Me Like You Do'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_Love_Me_Like_You_Do(skip_leadin=False):
    m 1hua "好,我现在就去准备"
    show monika at Transform(xpos=-800) with move
    m 2fua "What are you waiting for~"
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Love_Me_Like_You_Do.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 251
    stop music fadeout 3.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 1hubfa "......"
    m 5fublb "希望你觉得我弹的还算合格."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Are_You_Lost",
            category=['音乐'],
            prompt="我想再听你弹弹'Are You Lost'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_Are_You_Lost(skip_leadin=False):
    m 1hua "好的呢,[player]."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Are_You_Lost.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 154
    stop music fadeout 3.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 3eud "你在聆听的时候又想到什么了呢?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_One_Last_Kiss",
            category=['音乐'],
            prompt="我想再听你弹弹'One Last Kiss'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_One_Last_Kiss(skip_leadin=False):
    m 1eua "好,我现在就去准备一下."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/One_Last_Kiss.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 267
    stop music fadeout 3.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika    
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 3eubla "希望你会喜欢."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Odoru_Pompokolin_again",
            category=['音乐'],
            prompt="我想再听你弹弹'大家一起来跳舞'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_Odoru_Pompokolin_again(skip_leadin=False):
    m 5fua "好啊."
    m 3fua "我去准备一下."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Odoru_Pompokolin.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 186
    stop music fadeout 3.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 3eua "希望这首歌能让你开心."
    return

#65 YBWM_Piano
#恭喜你
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Piano_YBWM",
            category=['音乐'],
            prompt="我想听你弹奏'You Belong With me'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_Piano_YBWM(skip_leadin=False):
    m 1hublb "好的."   
    m 5fubfa "我去准备一下."
    show monika at Transform(xpos=-800) with move
    m 2fua "[player],我希望你也能知道,you belong with me~."
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/You_Belong_With_Me(piano).mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 206
    stop music fadeout 3.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 1fua "希望你能喜欢."
    return    
    

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Kami_no_Mani_Mani_again",
            category=['音乐'],
            prompt="我想再听你弹弹'神的随波逐流'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Kami_no_Mani_Mani_again(skip_leadin=False):    
    m 5fua "好啊."
    m 3fua "我现在去准备一下."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Kami_no_Mani_Mani.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 247
    stop music fadeout 1.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 3eua "希望这首歌能让你开心."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_you_hear_again",
            category=['音乐'],
            prompt="我想再听你弹弹'你听得到'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_you_hear_again(skip_leadin=False):
    m 5fua "好的."
    m 3eua "我很高兴你想听这些."
    show monika at Transform(xpos=-800) with move
    m 1hublb "{b}{i}有谁能比我知道,你的温柔像羽毛~{/i}{/b}."
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/you_hear_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 229
    stop music fadeout 1.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 5hubla "希望你会喜欢."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Shelter_again",
            category=['音乐'],
            prompt="我想再听你弹弹'Shelter'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_Shelter_again(skip_leadin=False):
    m 5fua "好的."
    m 3hua "我现在去把钢琴推过来."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Shelter_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 311
    stop music fadeout 1.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 6hubla "希望你喜欢,[player]."
    return