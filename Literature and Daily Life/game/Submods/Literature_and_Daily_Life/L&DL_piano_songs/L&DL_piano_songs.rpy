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

        all_songs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]#更新到总共三十首，我的天，要我命了
        
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
        m 1hublb "{b}{i}还有没有人知道,你的微笑像拥抱~~{/i}{/b}."
        m 5fublb "{b}{i}多想藏着你的好,只有我看得到~~{/i}{/b}"
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
    elif random_choice == 11:
        m 6hua "好的."
        m 3hua "我突然想到了一首很优美的曲子."
        show monika at Transform(xpos=-800) with move
        m 2hua "这首歌的名字叫作.....江南."
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/江南.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 200
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
        m 3eud "{b}不懂爱恨情愁煎熬的我们~~{/b}"
        m 2eub "{b}都以为相爱就像风云的善变~~{/b}"
        m 6eub "{b}相信爱一天抵过永远~~{/b}"
        m 6hub "{b}在这一刹那冻结了时间~~{/b}"
        if not persistent.monika_jiangnan_v3_end:
            m 5fua "......这首歌的歌词和意境让我感觉身处中国古代的小镇."
            m 5hub "希望你也能有类似的感觉,[player]."
            $ persistent.monika_jiangnan_v3_end = True
        $ mas_unlockEVL("monika_jiangnan_again", "EVE")
        return
    elif random_choice == 12:
        m 5hua "当然可以了."
        show monika at Transform(xpos=-800) with move
        m 2hua "我正好也想把接下来的这首曲子弹给你."
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/暖暖_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 244
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
        m 3hublb "{b}我想说其实你很好,你自己却不知道~~{/b}"
        m 5fubfb "{b}真心的对我好 不要求回报~~{/b}"
        m 6eublb "{b}愛一个人 希望他过更好~~{/b}"
        m 1eublb "{b}打從心裡暖暖的 你比自己更重要~~{/b}"
        if not persistent.monika_warm_v3_end:
            m 6hubla "......"
            m 3eub "这首歌的词真的打动我了呢,[player]."
            m 3hua "爱一个人一定会希望他过的好."
            m 1eubfb "我也希望你能好好的,身体和工作上都是."
            $ persistent.monika_ouatoh_v3_end = True
        $ mas_unlockEVL("Monika_warm_LADL_again", "EVE")#测试通过
        return           
    elif random_choice == 13:
        m 1hub "好的,我去准备一下."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/三国恋.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 241
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
        if not persistent.monika_Three_Kingdoms_v3_end:
            m 1hua "这首歌是以三国期间被迫卷入战争,被迫离开家乡与爱人的不知名的小兵视角出发的."
            m 5fua "作者觉得他们也有很多心声需要传达出来."
            m 3eub "{b}赤壁 烽火连天战役~~{/b}"
            m 1dud "{b}只挂掉我们 七万个兄弟~~{/b}"
            m 6eub "{b}长江水面写日记~~{/b}"
            m 3fub "{b}愿你也能看见涟漪~~{/b}"
            $ persistent.monika_Three_Kingdoms_v3_end = True
        $ mas_unlockEVL("Monika_Love_of_Three_Kingdoms_LADL_again", "EVE")#测试通过
        return
    elif random_choice == 14:
        m 1hua "好的."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/说好的幸福呢.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 251
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
        $ mas_unlockEVL("Monika_That_the well_being_of_this_good_LADL_again", "EVE")#测试通过
        return
    elif random_choice == 15:
        show monika at Transform(xpos=-800) with move
        m 2hua "我去弹一下龙卷风这首歌."
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/龙卷风_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
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
        play music original_music fadein 1.0
        m 1hua "希望你会喜欢."
        $ mas_unlockEVL("Monika_Tornado_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 16:
        m 6hua "嗯好,我现在先把钢琴推出来."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/恋爱循环_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 125
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
        m 5fua "我很少用可爱来形容这么一首歌"
        $ mas_unlockEVL("Monika_Renai_Circulation_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 17:
        m 3hua "好的."
        show monika at Transform(xpos=-800) with move
        if not persistent.monika_Spring_Subway_v3_end:
            m 2hua "这首曲子叫作,开往春天的地铁."
            $ persistent.monika_Spring_Subway_v3_end = True
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/开往春天的地铁.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 179
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
        m 5eub "听网络的人说这首歌听起来很有宿命感,于是我就学了."#可是我觉得很神圣啊
        $ mas_unlockEVL("Monika_Spring_Subway_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 18:
        m 1hua "好的."
        show monika at Transform(xpos=-800) with move
        if not persistent.monika_weilai_v3_end:
            m 2hua "这首歌叫作,未来へ."
            $ persistent.monika_weilai_v3_end = True
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/未来_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 203
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
        $ mas_unlockEVL("Monika_weilai_LADL_again", "EVE")
        return    
    elif random_choice == 19:
        m 2hua "嗯好."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/怪物_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 192
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
        if not persistent.monika_monster_v3_end:
            m 6rkc "感觉到后面节奏就有点小乱,有点把握不住."
            m 1ekd "嗯,不太完美."
            m 3esd "我每次都是练习好了才弹给你,这次是即兴弹的."
            m 5eub "希望你不要嫌弃."
            $ persistent.monika__monster_v3_end = True
        $ mas_unlockEVL("Monika_Monster_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 20:
        show monika at Transform(xpos=-800) with move
        m 2hua "我去弹一下unity这首歌."
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/unity_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 210
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
        $ mas_unlockEVL("Monika_unity_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 21:
        m 5hua "好的."
        m 1eub "我想想接下来的这首曲子."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/baby_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 210
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
        if not persistent.monika_baby_v3_end:
            m 5eud "{b}When I was 13, I had my first love~~{/b}"
            m 3hublb "There was nobody that compared to my baby~~{nw}"
            m 3sublb "And nobody came between us, nor could ever come above~~"
            m 1hua "......"
            m 1fub "真是很难的一段rap呢,[player]."
            m 3eud "它不仅需要你快速的唱出去,还得吞掉部分的音."
            m 6fub "我小时候很讨厌这段rap,觉得比较嘈杂."
            m 3hua "现在倒是有点喜欢了."
            $ persistent.monika__baby_v3_end = True
        $ mas_unlockEVL("Monika_baby_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 22:
        m 6hub "好的."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/persona.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 197
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
        if not persistent.monika_persona_v3_end:
            m 5eub "{b}Champagne flutes and~~{/b}"
            m 6fub "{b}Dinner suits that~~{/b}"
            m 3eub "{b}Keep your focus~~{/b}{nw}"
            m 1tub "{b}Away from the cheating hands~~{/b}"
            m 1hub "{b}Tell me~~{/b}"
            m 5eublb "{b}Does that sexy~~{/b}"
            m 5hublb "{b}Gown say what she's~~{/b}"
            m 3subfb "{b}Got in store for her man?~~{/b}"
            m 3hua "......"
            m 5fub "这首曲子被应用在赌场中."
            m 6eua "它的曲风我想你也能听出来."
            $ persistent.monika__baby_v3_end = True
        $ mas_unlockEVL("Monika_persona_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 23:
        m 1hub "我明白了,先让我准备一下."
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Love_Yourself_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 233
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
        $ mas_unlockEVL("Monika_Love_Yourself_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 24:   
        show monika at Transform(xpos=-800) with move
        m 2hua "我去弹一下monsters这首歌."
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/monsters_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 256
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
        if not persistent.monika_monsters_v3_end:
            m 5fubld "{b}I see your monsters, I see your pain~~{/b}"
            m 5hublb "{b}Tell me your problems,I'll chase them away~~{/b}"
            m 3fubfb "{b}I'll be your lighthouse~~{/b}"
            m 1eublb "{b}I'll make it okay~~{/b}"
            $ persistent.monika__monsters_v3_end = True
            m 1hua "......希望我在你身边会让你一直好好的."
        $ mas_unlockEVL("Monika_monsters_piano_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 25:
        m 1hua  "好的"
        if not persistent.monika_Payphone_v3_end:
            m 5ruc "不过我得想想,弹的有点多了,下一首我还是边拿谱子边弹吧."
            m 6rst "希望你不要嫌弃......"
            $ persistent.monika__Payphone_v3_end = True
        show monika at Transform(xpos=-800) with move
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Payphone_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 230
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
        $ mas_unlockEVL("Monika_Payphone_piano_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 26: 
        show monika at Transform(xpos=-800) with move
        m 2hua "我去弹一下Peaches_piano这首歌."
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Peaches_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 194
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
        if not persistent.monika_Peaches_v3_end:
            m 3eub "{b}And I see you~~{/b}"
            m 3fublb "{b}There’s nothing like your touch~~{/b}"
            m 5hublb "{b}It’s the way you lift me up, yeah~~{/b}"
            m 6subfb "{b}And I’ll be right here with you ’til the end of time~~{/b}"
            $ persistent.monika__Peaches_v3_end = True
        $ mas_unlockEVL("Monika_Peaches_piano_LADL_again", "EVE")#测试通过
        return    
    elif random_choice == 27: 
        m 5fub "好的."
        show monika at Transform(xpos=-800) with move
        m 2hua "我弹一下seven这首歌."
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/seven_piano.mp3" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 2.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 179
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
        $ mas_unlockEVL("Monika_seven_piano_LADL_again", "EVE")
        return                               
        

#V3 1
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_jiangnan_again",
            category=['音乐'],
            prompt="我想听你再弹弹江南这首歌",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label monika_jiangnan_again(skip_leadin=False):
    m 6hua "好的."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/江南.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 200
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
    m 1huabla "希望你喜欢"
    return

#2 V3    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_warm_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹暖暖这首歌",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_warm_LADL_again(skip_leadin=False):
    m 6hua "好的."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/暖暖_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 244
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
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Tornado_LADL_again",
            category=['音乐'],
            prompt="龙卷风",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Tornado_LADL_again(skip_leadin=False):
    show monika at Transform(xpos=-800) with move
    m 2hua "我去弹一下龙卷风这首歌."
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/龙卷风_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
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
    play music original_music fadein 1.0
    $ mas_unlockEVL("Monika_Tornado_LADL_again", "EVE")#测试通过
    return
#3 V3
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Love_of_Three_Kingdoms_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹三国恋这首歌",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Love_of_Three_Kingdoms_LADL_again(skip_leadin=False):
    m 2hua "好的,你也很喜欢这首歌吧."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/三国恋.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 241
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

#4
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_That_the well_being_of_this_good_LADL_again",
            category=['音乐'],
            prompt="我想听你弹'说好的幸福呢?'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_That_the well_being_of_this_good_LADL_again(skip_leadin=False):
    m 1eua "嗯好."
    m 2hub "我现在准备一下."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/说好的幸福呢.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 251
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
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Tornado_LADL_again",
            category=['音乐'],
            prompt="我想再听你弹'龙卷风'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Tornado_LADL_again(skip_leadin=False):
    m 2hua "好的."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/龙卷风_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
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
    play music original_music fadein 1.0
    if not persistent.monika_Tornado_again_v3_end:
        m 5eud "{b}爱像一阵风吹完它就走~~{/b}"
        m 1dkd "{b}这样的节奏谁都无可奈何~~{/b}"
        m 3ekd "{b}没有你以后 我灵魂失控~~{/b}"
        m 6eud "{b}黑云在降落 我被它拖着走~~{/b}"
        m 5eud "{b}静静悄悄默默离开~~{/b}"
        m 5hud "{b}陷入了危险边缘Baby~~{/b}"
        m 5eud "{b}我的世界已狂风暴雨~~{/b}"#表情
        $ persistent.monika__Tornado_again_v3_end = True
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Renai_Circulation_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'恋爱循环'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Renai_Circulation_LADL_again(skip_leadin=False):
    m 6hua "嗯好."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/恋爱循环_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 125
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
    if not persistent.monika_Renai_Circulation_v3_end:
        m 5ruc "嗯，[player]."
        m 3eud "我之前只了解过恋爱循环是化物语的曲子."
        m 3eusdrc "当时我这么想,这首歌这么甜,对应的番剧也是一段甜甜的恋爱故事吧."
        m 1eusdlt "但真正看过之后才发现并不是这样."
        m 3rud "嗯,我挺推荐你去看看的,哪怕它是十几年前的番剧了."
        $ persistent.monika__Renai_Circulation_v3_end = True
    return

#7
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Spring_Subway_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'开往春天的地铁'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Spring_Subway_LADL_again(skip_leadin=False):
    m 5fua "好的."
    show monika at Transform(xpos=-800) with move
    m 6hua "等我想想谱子."
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/开往春天的地铁.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 179
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

#8
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_weilai_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'未来へ'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_weilai_LADL_again(skip_leadin=False):
    m 1hua "好的."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/未来_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 203
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
    m 5fub "希望这首曲子能让你感到温暖."
    return 

#9
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Monster_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'怪物'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Monster_LADL_again(skip_leadin=False):
    m 3ruc "嗯......"
    m 3eusdrd "让我做一下心理准备,[player]."
    m 6rusdra "因为每次练习完这首我都感觉有些累."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/怪物_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 192
    stop music fadeout 1.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 6hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 1.0
    m 5fubla "希望你喜欢."
    return

#10
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_unity_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'unity'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_unity_LADL_again(skip_leadin=False):
    m 1eua "好的."
    m 6hub "如果这能让你开心,我弹多少次都乐意."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/unity_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 210
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

#11
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_baby_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'baby'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_baby_LADL_again(skip_leadin=False):
    m 5fub "当然可以呀."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/baby_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 210
    stop music fadeout 1.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 6hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 1.0
    m 6eub "如果你能学会这首歌并唱给我听的话,我会很开心的,[player]."
    m 3hua "当然,这并不是我强求你做这些事."
    return

#12
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_persona_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'The Whims of Fate'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_persona_LADL_again(skip_leadin=False):
    m 5hua "好的."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/persona.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 197
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
#13
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Love_Yourself_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'Love Yourself'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Love_Yourself_LADL_again(skip_leadin=False):
    m 1hua "明白了."
    m 2hub "我现在去准备一下."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Love_Yourself_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 233
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

#14
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_monsters_piano_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'monsters'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_monsters_piano_LADL_again(skip_leadin=False):
    m 5fub "嗯好"
    show monika at Transform(xpos=-800) with move
    m 6eua "希望你会喜欢."
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/monsters_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 256
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
    $ mas_unlockEVL("Monika_monsters_piano_LADL_again", "EVE")#测试通过
    return
#15
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Payphone_piano_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'Payphone'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Payphone_piano_LADL_again(skip_leadin=False):
    m 5fua "好的."
    show monika at Transform(xpos=-800) with move
    m 6eub "这个歌所属的乐队创作的歌也挺好听的,晚点我看看还有没有这类的谱子."
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Payphone_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 230
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
#16
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Peaches_piano_LADL_again",
            category=['音乐'],
            prompt="我想听你再弹弹'Peaches'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_Peaches_piano_LADL_again(skip_leadin=False):
    m 1hub "好的"
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Peaches_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 194
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
#17

#
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="LADL_piano11111_seven_piano",
            category=['音乐'],
            prompt="我想听你再弹弹'seven_piano'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label LADL_piano11111_seven_piano(skip_leadin=False):
    m 2hub "好,我现在就去准备这首."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/seven_piano.mp3" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 2.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 179
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
    $ mas_unlockEVL("Monika_seven_piano_LADL_again", "EVE")
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