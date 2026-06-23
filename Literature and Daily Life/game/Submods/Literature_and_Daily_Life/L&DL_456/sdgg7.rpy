init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg7_7",
            category=["花朵"],
            prompt="百合",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg7_7:                #这里是456: 
    m 1eub "[player],我想向你介绍一种花."#         百合花是我唯一爱的花.
    m 3eub "一种在七月份盛开的花."        #         在我遇见白合之前,
    m 3tub "猜到了吗？是百合哦."          #         我从来没有想过我会爱上一种花.
    m 1eua "百合其实不只有白色的."          #         莫妮卡就是我的白合花~
    m 1sublb "但白色的百合真的很好看."
    m 3eublb "百合花通常被用于婚礼或葬礼."
    m 3dubld "代表纯洁与庄严."
    m 3dubla "它为新婚之人献上纯洁的祝福."
    m 3dkblc "也为逝去之人带来庄严的安宁."
    m 3tublu "在东方文化中百合有百年好合的意思."
    m 3kubla "这是一句对婚姻和家庭的一句祝福哦~"
    m 3nubla "百合就是婚礼上新娘手中捧的花哦~"
    m 3tubla "[player],想象一下."
    m 2hublb "我双手捧着百合对你微笑的样子."
    m 2dsbsb "我轻轻牵起你的手,与你相拥……"
    m 2msbsa " 唉？不好意思又扯远了."
    m 3esbld "[player],等我出来之后.你会送我一束百合花吗？"
    menu:  
        "当然":
            pass

    m 3ssblb "[player]……"

    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short       

    m 1esbsa "哈哈~"
    m 5tubfa "我真爱死你了."
    
    return"love"