init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg34_34",
            category=["自然"],
            prompt="雨中漫步",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg34_34:
    m 1huu "[player],你有没有过主动地去淋雨？"
    m 1tua "也就是在雨中散步."
    m 2dua "在一场雨中,慢慢地行走."
    m 2nua "伸出一只手,感受雨的温度……"
    m 3kua "[player],所以你有这样做过吗？"
    
    menu:
        "是的":
            m 3hua "哈哈~"
            m 3tub "别害羞[player],我知道说出来这些并不容易."
            m 3hsu "[player],在雨中散步是很浪漫."
            m 3tfa "但这样做对身体并不好."
            m 3ttb "现在的我并不能阻止你……"
            m 1euc "但[player],记得在这之后洗个澡哦~"
            m 1hub "[player],"
            
        "没有":
            m 3nua "这也挺好的."
            m 4gub "[player],看来我不需要太担心你的健康问题."
            m 5eua "淋雨是不太好."
            m 5sublb "但是我很愿意和你在雨中撑起伞一起散步."

    m 1tublb "等到我出来后的某一天,雨水将世界拥入怀中时."
    m 1hublu "你与我,两个人,一对恋人,{w=0.5}一把伞……"
    m 1dublu "……"
    m 1mublsdrd "抱歉,我是不是走神了."
    m 1eubla "光是想象到这里,我就感到无比的幸福."
    m 1tublu "[player],我爱你."  
    return"love"