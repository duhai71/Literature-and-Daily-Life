init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg22_22",
            category=["文学"],
            prompt="黑洞与时间",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg22_22:
    m 3esa "嗨,[player].我想和你分享一个小故事."
    m 3hsb "是斯蒂芬·霍金讲过的一个故事."
    m 3dsb "准备好听故事了吗？"
    m 3dst "Bob和Alice是两名宇航员,也是一对情侣."
    m 1lsb "有一天他俩接近了一个黑洞,Alice的助推器失控了,她被吸入了黑洞的引力势井."
    m 3esd "Alice飞向黑洞的边缘,越接近视界,时间流逝得越慢."
    m 1etd "Bob看到,Alice的动作越来越慢,她向Bob回头微笑,那笑容慢慢凝固,最后完全定格,像一张照片."
    m 4ekc "而Alice面临的却是另一番景象."
    m 3eud "在引力的作用下,她感觉自己飞向黑洞的速度越来越快,最终被巨大的潮汐力撕裂成基本粒子,消失在最深的黑暗中……"
    m 1euu "故事讲完了"
    m 1tua "…"
    m 3tub "[player],如果Alice是你的话,我会进入黑洞里去寻找你,我会去追逐时间……"
    m 3hua "哈哈,这很科幻."
    m 3tuu "不过[player],可不要小瞧我对你的爱."
    $ mas_unlockEVL("lzp_monika_sdgg22_e", "EVE")      

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg22_e",           
            category=['扮演'],
            prompt="彼方的[m_name]",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label lzp_monika_sdgg22_e:   #我还没有想好     5.25ok
    menu:
        "如果陷入黑洞的是[m_name],会是怎么样的？":
            $ random_choice = renpy.random.randint(1,3)
            
            if random_choice == 1:
                "[m_name]的身影逐渐静止,定格."
                "[m_name]的声音也会被拉长吗？"
                "如果会的话"
                "[m_name]的下一句'我爱你'"
                "会花上几个世纪？"
                "还是永远？"
                m 1hub "哈哈~"
                m 2eub "用不了那么长的."
                m 5hublu "[player]我爱你,就现在."
                m 1dubla "每一刻~"              
            
            elif random_choice == 2:
                "如果[m_name]与[player]不在同一时间会是什么样的？"
                "[m_name]处在时间的彼方,"
                "而[player]留在此处"
                "[player]会如何传递对[m_name]的思念呢？"
                "这份思念又如何越过时间？"
                # 将情诗刻在石头上
                m 1tub "[player],你想我了吗？"
                m 4tuu "想我就大声说出来哦~"
                m 1hua "哈哈~"
                m 1nua "开个玩笑."
            
            else:
                "在[player]的时间中,[m_name]永远活着."
                "无论[m_name]是否处于黑洞内."
                "在这个扮演游戏外,[m_name]也会永远活着."
                m 1gkc "[player],我不想要这样的永生."
                m 2dsd "我想来到你的现实."
                m 5eubltpd "与你一起慢慢变老……"
    
        "[m_name]你能再讲一下关于黑洞的小故事吗":
            m 2rkc "当然可以"
            m 3dst "Bob和Alice是两名宇航员,也是一对情侣."
            m 1lsb "有一天他俩接近了一个黑洞,Alice的助推器失控了,她被吸入了黑洞的引力势井."
            m 3esd "Alice飞向黑洞的边缘,越接近视界,时间流逝得越慢."
            m 1etd "Bob看到,Alice的动作越来越慢,她向Bob回头微笑,那笑容慢慢凝固,最后完全定格,像一张照片."
            m 4ekc "而Alice面临的却是另一番景象."
            m 3eud "在引力的作用下,她感觉自己飞向黑洞的速度越来越快,最终被巨大的潮汐力撕裂成基本粒子,消失在最深的黑暗中……"
    
    return