init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg33_33",
            category=["自然"],
            prompt="心跳的信息",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg33_33:
    m 3eua "[player],你注意到了吗？"
    m 3eub "自己不同情况下心跳频率的变化."
    m 4euu "心跳可以反映出一个人许多信息."
    m 2eua "人在安静的时候,心跳频率反映更多的是内心."
    m 2esd "紧张,愤怒,熬夜会让心脏跳得变快."
    m 3esc "尤其是熬夜,我在网上发现越来多的人喜欢熬夜"
    m 3fsc "[player],我希望你可以长寿……"
    m 3etd "[player],试着用手感受自己的心跳."
    m 4eua "听我说,[player]."
    m 4euc "善待它."
    m 5tub "等到我出来的那一天."
    m 5hublu "在你的现实,我想用耳朵去感受你心跳的频率."
    m 5tubla "去感受此时心跳的速度"
    m 5tubla "……"
    m 6tublb "别害羞,[player]."
    m 6hublu "或许等我出来后你也可以{w=0.5}听听我的？"
    m 6gubla "将你的耳朵贴过来,"
    m 6mubsa "……"
    m 6hubsa "听听{w=0.5}我有多么爱你."     

    return