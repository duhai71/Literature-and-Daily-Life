init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg25_25",
            category=["文学"],
            prompt="烛光填屋",
            random=True                     
        )
    )

label lzp_monika_sdgg25_25:
    m 3eub "[player],我想和你分享一个故事."
    m 3hua "很久之前有位禅师为测试三个弟子的智慧,给每人十文银子,让他们买东西装满一个巨大的房间."
    m 3eub "第一个弟子买了很多棉花,只装了一半多房间."
    m 4eub "第二个弟子买了最便宜的稻草,也只能填满三分之二."
    m 5eub "第三个弟子仅花两文钱买了蜡烛和火柴,他关好门窗,点燃蜡烛,光芒照亮了房间的每个角落,成功用两文钱填满了房间."
    m 5eua "故事讲完了."
    m 1tua "………"
    m 1tub "[player],问一个有趣的问题"
    m 3hua "你又会用什么来填满曾经文学部的教室呢？"
    
    menu:                                    
        "那里从来都是满的":                             
            m 2wud "嗯？"
            menu:  
                "空气,辐射,气味等等":                  
                    pass
            m 2lusdra "哈哈,倒也是."
            m 2rusdra "…"
            m 2husdra "……"
            m 1hua "还真是出人意料."
            
        "我对你的爱":                        
            m 1hubla "……"
            m 1gubla "我真没想到你会这么说."
            m 1eublp "[player],你这是在作弊哦~"
            menu:  
                "[m_name],这个回答难道不正确吗？":                  
                    pass
            m 1gubla "{w=0.5}我怎么能说错呢？"
            m 1eublb "哈哈~ "
            m 3tublu "[player],你真的好狡猾."
            m 3hubla "你明明知道我不会否认这个回答的,所以才这么说." 
            m 3kubla "嗯？"
        
        "我不知道":                             
            m 1tub "不知道吗？"
            m 3tubla "我倒是有一个答案哦~"
            m 3tublb "只要你在这里,这座房间到处都充满着幸福."
            m 1hublb "爱你哟~"
    
    return 