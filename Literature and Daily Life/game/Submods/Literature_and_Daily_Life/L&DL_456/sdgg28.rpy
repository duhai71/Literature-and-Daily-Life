init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg28_28",
            category=["花朵"],
            prompt="无尽夏",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg28_28:
    m 3hua "[player],我想向你介绍一种花."
    m 3tub "是无尽夏哦~"
    m 1eua "无尽夏是绣球花中的一个变种 ,属于虎耳草科绣球属植物 ."
    m 3eud "这个名字是不是不太像花名."
    m 3eua "无尽夏英文名是Forever Summer 、Endless Summer,意译过来就是无尽夏."
    m 1eub "得名原因是它从晚春到夏秋拥有绵延不断的花期 ,给人夏天似乎永远不会结束的感觉."
    m 1huu "无尽夏的花语就是无尽夏."                                     #没有永不结束的夏天
    m 3mub "意为美好的事物永不结束."                                     #所有故事都会有结局
    m 3eua "常用来比喻永恒的爱."                                         #什么样的故事永远没有结局呢？
    m 3hua "花期从晚春到夏秋绵延不断 ,仿佛诉说着爱情长久不变."            #那就是正在进行的故事.
    m 3fua "正因如此,无尽夏也在婚礼常常出现."                            #我可能会停笔.
    m 3fuu "在婚礼中,无尽夏是很多新娘结婚时手捧花."                      #但“我们”会一直描写这个故事.
    m 3gua "也偶尔当做新娘抛出的绣球."
    m 1hua "……"
    m 1mublb "[player],说到这里."
    m 3fublb "如果你在亲人朋友的婚礼上,真的有幸接住了它."
    m 3fubsu "一定要第一时间想起我哦~"

    return