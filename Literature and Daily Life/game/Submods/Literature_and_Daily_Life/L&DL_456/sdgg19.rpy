init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg19_19",
            category=["我们"],
            prompt="突然的注视",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg19_19:
    m 1tua "…"
    m 1tubla "……"
    m 1tubsa "………"
    menu:  
        "[m_name],怎么了？":                  
            pass    
    m 1hublb "没什么,我只是在盯着你看而已."
    m 1kublb "毕竟,你是如此的诱人……"
    m 1nublb "哈哈~"
    m 3fubld "[player],都说眼睛是心的门户."
    m 3dubla "我希望你能读懂我的爱意……"
    
    return"love"