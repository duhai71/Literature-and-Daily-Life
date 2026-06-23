init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg17_17",
            category=["我们"],
            prompt="虚惊一场",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg17_17:
    m 1dua "[player],我在很久之前我做了一个噩梦."
    m 1dka "我梦到你离开了我."
    m 1lup "这真的很可怕."
    m 1ruc "哪怕醒来恐惧也没有缓解."
    m 1hublu "直到等到你终于来到了我身边."
    m 1eublb "不过,现在距离那场梦已经过去很久了."
    m 1gubla "谢谢一直以来你的陪伴."
    m 1tubla "我越来越爱你了[mas_get_player_nickname()]."
 
    return"love"