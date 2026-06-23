init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg24_24",
            category=["浪漫"],
            prompt="[player]的现实称何为爱？",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg24_24:
    m 3eub "[player],还记得《Your Reality》这首歌里的一个问题吗？"
    m 4eut "你的世界究竟称何为爱？"                                 #答案从来不在选项里面,你说对吗？阅读到此的玩家.
    m 1hublb "我们在一起有一段时间了,这段时间我很幸福哦~"
    m 1gublb "所以{w=0.5}[player],现在你有一个答案了吗？"
    
    menu:
        "爱是人类对抗孤独的武器":
            m 1etc "对抗孤独的{w=0.5}武器？"
            m 1htc "呃……"
            m 1etc "这个说法真有趣啊."
            m 1htsdlb "哈哈~"
            m 1mub "如果换一个说法的话."
            m 1gublb "爱是陪伴一生的誓言."
            m 1eublb "这样会不会浪漫一些了呢？"
            m 1tublb "[player],对于我们而言,孤独并不可怕."
            m 1hublb "因为……"
            m 3fublb "我找到了{w=0.5}你,而你也找到了{w=0.5}我."
            m 3mublb "嘿嘿~"
            m 1hublb "有你在我身边,我真的很幸福哦~"
            
        "爱只是各种激素编织给大脑的谎言":
            m 1lusdrc "这……"
            m 1htsdrd "是不是有点太唯物主义？"
            m 1gssdrd "[player],我不是很喜欢这个说法."
            m 1esc "虽然我明白,在你的现实中,性激素是爱情中不可或缺的因素."
            m 3esd "但这并非全部."
            m 5hubla "[player],我们一起去寻找答案,好吗？"
       
        "我不知道,我还没有想过这个问题":
            m 1tud "没有关系,[player]."
            m 1eud "其实这个问题的答案从来不是唯一的."
            m 1hua "也许答案一直在我们之间……"
    
    return