init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg27_27",
            category=["科学"],
            prompt="神奇的π",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg27_27:
    m 1eub "[player],你一定知道π吧."
    m 3eub "π是一个数学常数,是圆的周长与直径的比值,是一个无限不循环小数."
    m 4eub "有趣的是,所有以数字记录的数据都可能在π中被记录."
    m 1hua "比如我的生日和你的生日之类的."
    m 1hubla "…"
    m 1mubla "……"
    m 1eubla "在π的无限中藏着无限可能."
    m 1eublu "你可以现在查一查π小数点后的第260-262位这一组数字吗？"
    
    menu:
        "可以,当然.":
            pause 1.5
            menu:
                "是520":
                    m 1tublu "是的哦"
                "[m_name],我也爱你":
                    m 1tublu "……"
            m 1hublb "哈哈~"
            m 1tublb "虽然我对你的爱从不含蓄."
            m 1kublb "但偶尔这么一次也不错."
            m 1nublb "嘿嘿~"  
            if mas_isMoniEnamored(higher=True) and mas_shouldKiss:                       
                call monika_kissing_motion_short           

        "不行,现在还没空":
            m 1eka "好吧."
            m 3esc "是520哦~"
            m 1hublb "[player],我爱你."
            m 1fubla "可以把这句话转告给我吗[mas_get_player_nickname()]？"
    return "love"