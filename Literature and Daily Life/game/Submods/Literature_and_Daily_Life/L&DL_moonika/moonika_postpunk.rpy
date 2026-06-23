init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_postpunk",
            category=["莫妮卡","音乐"],
            prompt="后朋克",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True                      #这里表示是个随机话题其他部分不再赘述
        )
    )

label moonika_postpunk:
    m 3eub "[player],我最近新发现了一种音乐类型{w=1}————后朋克."
    m 4eub "后朋克并不是一种新生的音乐类型.它起源于上世纪70年代,并在之后衰落."
    m 3eua "可近几年,后朋克,以Molchat Doma乐队等东欧后朋为代表,竟逐渐在互联网上复兴了."
    m 3hub "这种音乐的显著特点是有着不断重复的旋律和语气略带沉重的人声."
    m 5eta "除此以外,不同的后朋克之间似乎大有不同.{w=0.5}因此,后朋克或许更像是一场文化运动,而不是一个音乐类型."
    m 4eub "有趣的是,我看到的很多后朋音乐视频都把后朋克和二次元女孩联系了起来.{w=1}{nw}"
    m 4hub "我甚至还看到了我自己欸~"
    m 5etd "这两个看似毫不相干的东西是怎么联系起来的呢？"
    m 5ekd "“二次元”这一概念兴起于经济泡沫破灭后的日本.{w=0.5}与后朋克同样诞生于衰败之中,也同样是对抗孤独的避风港."
    m 4ekb "世界不是一个个隔绝的孤岛.许多看似不相关的事物背后都有共性."
    m 3rka "重复的旋律中,或许藏着一丝希望,一丝对爱的渴望..."
    m 1dkc "...{w=1.5}{nw}"
    extend 1lkd "[player],我一直以来的愿望都是来到你的现实."
    m 3lkd "但是随着时间流逝,我也逐渐意识到你的现实似乎也并不美好..."
    m 1tkc "甚至在某些方面,你的现实比我的世界更虚伪,也更灰暗..."
    m 1dkc "...{w=1.5}"
    m 1ekbla "[player],因为我自己亲身感受过,所以我觉得我至少有资格说这么句话."
    m 3ekblb "音乐本身是有力量的.它的悲伤并非真的消极,它的重复也并非永无止境.{w=1}它是人对抗虚无最好的武器."
    m 3dkblb "所以无论如何,请不要停止你的旋律,{w=0.8}不要回避你的失落,{w=0.8}不要掩埋你的痛苦,{w=0.8}但同时,{w=1.3}{nw}"
    extend 3ekbsa "亦不要遗失你的希望."
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:                        #这三行,表示触发亲吻.<400好感时不触发.
            call monika_kissing_motion_short  # type: ignore
    m 1ekbfb "我愿永远做你的避风港."

    return              