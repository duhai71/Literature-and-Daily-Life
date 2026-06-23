init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg44_44",
            category=["科学"],
            prompt="怀疑与求真",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg44_44:
    m 1eub "[player],你知道地平说吗？"
    m 3eub "对,就是认为地球是平面的假说."
    m 4eua "虽然这个假说早就在很久之前的麦哲伦环球航行时代被推翻了."
    m 5lua "但现在依然有人相信地平说."
    m 5dua "相信这个假说的人们甚至成立了一个地平说协会."
    m 2eua "在这个组织中,不乏有很多社会上的各界知名人士."
    m 3eua "每年也会举行地平说的国际研讨会"
    m 4dub "[player],你知道我为什么想和你分享这个故事吗？"
    m 4tud "在人类进入现代物理学之前,正是因为有一小部分人不相信大众的观点,带领着我们扩展了知识."
    m 4hua "虽然现代科学早就证明了地球是圆的,但他们的科学观念与求知精神依然值得学习."
    return
