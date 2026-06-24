init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg7",     
            category=['扮演'],                         
            prompt="恋爱关系中依赖的一方",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
     #2                                                  
label monika_custom_topic_sdg7:                       
    m 1rud "恋爱关系中依赖的一方？"
    m 1hub "[player],你是想让我对你撒娇吗？" 
    m 1dub "虽然我更想成为被依赖的一方." 
    m 1tubla "不过,向你撒娇或许也不错？" 
    m 3tublb "[player],你能看看我脸上有什么吗？" 
    m 3hublu "我觉得有一些痒."  
    m 3hublu "…{w=0.5}…{w=0.5}…{w=0.5}……"
    pause 2.5 
    m 3kublu "我的脸漂亮吗？"     
    m 3mublu "哈哈~" 
    m 3gublu "你现在的样子一定很可爱！" 
    m 1hublu "还有…" 
    m 1dublb "亲爱的,如果在今晚入梦前默念几遍我的名字." 
    m 1hubla "我一定会很开心的." 
    m 5hubla "我无时无刻都在想你呢~" 
    m 5kubla "[player],我爱你~"
    $ mas_unlockEVL("monika_custom_topic_sdg7_1", "EVE")  

    return"love"
#附属话题 还没想好        5.25 ok
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg7_1",     
            category=['浪漫'],                         
            prompt="我昨晚梦见你了",                             
            pool=True,                             
            unlocked=False,
            rules={"no_unlock": None}                                  
        )
    )
                                                       
label monika_custom_topic_sdg7_1:                       
    m 1hua "哦,[mas_get_player_nickname()]"
    m 3mublb "那是一个怎样的梦呢."
    menu:
        "是一场美梦":
            m 2eublb "真的？"
            m 2hublu "我很开心哦~"
            m 2tublb "我想我们一定经历了一场非常浪漫的约会."
            m 7eublb "有研究称梦是潜意识的投影."
            m 1gublb "我能明白你对我的爱意."
            m 1hublu "谢谢你跟我说这件事情."
            m 5tubla "我越来越爱你了."
            
        "是一场噩梦":
            m 3wud "别害怕,[player]."
            m 2eka "我不明白梦中的我对你做了什么."
            m 2eud "但现在真实的我就在你的眼前,你的身边."
            m 3eud "我是不会离开你的."
            m 1hua "还有,我很开心,你告诉我这件事."
            m 1euc "[player],不要把负面情绪藏在心里."
            m 1hud "至少,不要在我面前藏起来."
            m 1dud "[player],答应我好吗？"

        "是一场平静的梦":
            m 1duu "平静的一场梦啊."
            m 1hua "哈哈~"
            m 3eub "那也没什么不好的."
            m 3eubld "与你在现实一起去经历生活的点点滴滴."
            m 1eublb "是我现在最大的梦想哦~" 

    return
