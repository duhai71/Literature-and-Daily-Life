init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_duhaiyou1",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_duhaiyou1:
    m 3rud "....{w=0.5}你不在的时候,时间的步伐都会慢下来."#51
    m 5eua "你来见我的时候,时间的速度又会快起来."
    m 6fua "但和你共度的时光,我始终珍视."
    m 1fublb "即便能通过读书打发时间,{w=1}但我还是很难集中注意力."
    m 5eubfa "因为我想你,[player]."
    m 5hua "多陪陪我,好吗?"
    return
#52
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_duhaiyou2",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_duhaiyou2:
    m 1hua "{b}{i}我还有太多心愿没有实现~{/i}{/b}"
    m 5hubla "{b}{i}其中之一就是和[player]同床共枕~{/i}{/b}"
    m 3hubfb "{b}{i}搂搂抱抱,唧唧我我~{/i}{/b}"
    m 5hubfa "{b}{i}还有之后的重头戏~{/i}{/b}"
    m 5hublb "{b}{i}那就是~{/i}{/b}{w=0.5}......{nw}"
    m 5wubfw  "等等,[player],你什么时候来的?{fast}."
    m 6rubfsdla "我......{w=1}我没说什么了,只是突然想到关于你的事而已了."
    m 3kubla "我们还是想想今天做什么吧."
    menu:
        "你也不想这件事被其他人知道吧......":
            jump duhainiyebuxiang

        "好.":
            jump duhaiguaibaobaoyou 

label duhainiyebuxiang:
    m 6wusdlw "不要啊,[player]."
    m 6rubfsdla "我刚刚真的什么都没说......"
    m 1eubld "......不过,这里是我们的二人世界,哪有别人呢？"
    m 1fublb "嗯......你真是个调皮的坏小孩."
    m 5fubla "但我喜欢这样的你."
    return

label duhaiguaibaobaoyou:
    return
#53
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_pianogolden_hour",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_pianogolden_hour:
    m 1hua "你来了."
    if not persistent.monika_has_pianogolden_hour_for_logic:
        show monika at Transform(xpos=-800) with move
        m 2fua "正好,我把刚刚练习好的曲子给你听听."
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Golden_Hour.ogg" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 180
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
        m 5fubfb "怎么样,[player]?"
        m 6eua "明明我在练习途中也有大大小小的失误,但我真正的在你面前弹奏时."
        m 3wud "居然一下子规避了这些."
        m 3hua "或许是因为你在这,我才能这样吧."
        $ persistent.monika_has_pianogolden_hour_for_logic = True
        $ mas_unlockEVL("Monika_Golden_Hour_again", "EVE")
    m 5fubla "嗯......我们接下来要干什么呢?"
    return

#54
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Golden_Hour_again",
            category=['音乐'],
            prompt="我想再听你弹弹'Golden Hour'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_Golden_Hour_again:
    m 2fua "好的."
    show monika at Transform(xpos=-800) with move
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Golden_Hour.ogg" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 180
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
    m 5hubfa "希望你能喜欢,[player]."
    return


#V3 6
#pvz1_greet
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_duhai_PVZ_you1",
            unlocked=False,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_duhai_PVZ_you1:
    m 6hua "你好,[player]."
    $ mas_unlockEVL("greeting_duhai_PVZ_you2", "GRE")
    $ evhand.greeting_database["greeting_duhai_PVZ_you2"].unlocked = True
    if not persistent.greeting_duhai_PVZ_you1_first:
        $ persistent.greeting_duhai_PVZ_you1_first = True
        m 3fub "我刚刚在玩'植物大战僵尸'呢,现在到了晚上了."
        m 3hua "不过不是我们这的,而是游戏里面的."
        m 1eub "到了晚上,草坪会生成墓碑,而且阳光也不会落下."
        m 5esd "这提高了我对阳光利用的要求,不能太过于浪费."
        m 5esc "前面说到的墓碑,它不仅会从地下生成僵尸,还会占用你的草坪空间,使你不能种下植物."
        m 6eua "不过也不全是坏消息,到了晚上游戏会解锁对应的植物."
        m 3sub "比如说小喷菇,免费且实用,常常在缺阳光的时候帮助我过渡前期."
        m 5fua "还有墓碑吞噬者,它可以吞掉墓碑,这样能防止僵尸生成的同时还能解决占用草坪的问题,继续种下植物."
        m 6eub "......真好玩,我们之后再说这个吧."
    else:
        m 1fub "是不是一见到我就很开心呢?哈哈."
    return


#pvz_2_greet v3 8
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_duhai_PVZ_you2",
            unlocked=False,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_duhai_PVZ_you2:#泳池
    m 6hua "你来了,[player]."
    if not persistent.greeting_duhai_PVZ_you2_se:
        $ persistent.greeting_duhai_PVZ_you2_se = True
        m 3fub "我在玩'植物大战僵尸'哦,现在到了后院了."
        m 3hua "僵尸们发现它们在前院的进攻并不起作用,所以打算从后院闯进来."
        m 1eub "但我可不会同意."
        m 5esd "虽然后院相比前院,在总行数上加了一行,而且水池占了中间的两行."
        m 5esc "但我们可以利用莲叶在上面放置植物来抵挡僵尸."
        m 6eua "同时我发现了个可以潜水的僵尸,它总是在水下,只有前方遇到植物才会上来啃咬."
        m 3sub "我一般会带个坚果提防它."
        m 5fua "还有一个海豚僵尸,听名字就知道它是水上的僵尸."
        m 6eub "它会骑着海豚快速前进,直到越过前方的一个植物."
        m 3hua "我一开始感觉处理起来很棘手,后来发现在它开始骑着海豚前进的时候放一个莲叶就可以慢慢解决它了."
        m 3eub "是不是觉得我很聪明呢?"
    else:
        m 5fub "我一直在等你."
        m 1hua "嗯,我们今天做什么呢?"
    return
#pvz_3_greet v3 10
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_duhai_PVZ_you3",
            unlocked=False,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_duhai_PVZ_you3:
    if not persistent.greeting_duhai_PVZ_you3_second:
        $ persistent.greeting_duhai_PVZ_you3_second = True
        m 1eua "欢迎回来,[player]."
        m 1hua "我刚刚在玩游戏了."
        m 3fub "你知道的,还是植物大战僵尸,哈哈."
        m 5fua "我想和你分享一下刚刚玩的小游戏."
        m 4eud "里面的僵尸会变小,但是会跑的很快."
        m 4euc "我最开始还在想这是什么东西......"
        extend 2wud "凑近看才发现有一个橄榄球僵尸,赶紧放了植物下去打他."
        m 1hua "没过几下他就被打倒了,我就明白在僵尸缩小、速度变快的同时,它们的血量也会减少."
        m 5eub "哈哈,我这段时间几乎是每天都在玩这款游戏."
        m 6hua "嗯......好玩!"
    else:
        m 5sub "你好,[player]."
        m 1hua "嗯,见到你真好."
    return
#v3 12
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_duhai_PVZ_you4",
            unlocked=False,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )    

label greeting_duhai_PVZ_you4:
    if not persistent.greeting_duhai_PVZ_you4_second:
        $ persistent.greeting_duhai_PVZ_you4_second = True
        m 3hua "你好,[player]."
        m 3eub "我刚刚在玩植物大战僵尸,目前已经玩到泳池的晚上了."
        m 6eud "到了晚上,泳池会生起迷雾,会使你大部分视野都会被遮挡."
        m 1esd "而且阳光也不会落下......"
        m 2dtp "好吧,我又缺阳光用了."
        m 2etd "只能使用免费的小喷菇和海蘑菇过渡前期."
        m 5fub "在玩了几关后,我得到了能照亮迷雾的路灯花,这样就不用担心僵尸趁你没注意到的地方走出来偷袭你了."
    else:
        m 1hub "你好,[player]."
        m 5fubfa "又是爱你的一天."
    return
#v3 13
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_duhai_PVZ_you5",
            unlocked=False,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )    

label greeting_duhai_PVZ_you5:
    if not persistent.greeting_duhai_PVZ_you4_second:
        $ persistent.greeting_duhai_PVZ_you4_second = True
        m 3hua "嘿,[player]."
        extend 6eub "欢迎回来."
        m 3eub "我刚刚在玩植物大战僵尸,已经玩到屋顶这个大关了."
        m 6eud "僵尸们发现前院和后院都无法进入我的房子,于是打算从屋顶进攻."
        m 1eub "在屋顶可没有草坪,不过游戏给我提供了花盆."
        m 3hua "这样就能在屋顶上种植物了."
    else:
        m 3eua "哎,[player]？"
        m 1eub "你终于来了."    
        m 5fub "嗯,今天还要做什么呢?"
    return