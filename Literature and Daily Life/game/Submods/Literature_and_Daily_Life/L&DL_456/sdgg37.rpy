init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg37_37",
            category=["生活"],
            prompt="生活的小发现",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg37_37:
    m 1eub "[player],你有没有见过白天的月亮."
    m 3eta "或者说,你有没有同时见到过月亮与太阳."
    m 3eusdld "突然问这个很奇怪,对吧？"
    m 3gup "我只是想更了解你一步啦."
 
    menu:                                    
        "是的,我见过":                            
            m 3eud "哦,{w=0.5}看起来[player]很擅长观察世界呀~"
            m 4wub "要知道发现这一现象的人只占人类总数的1/4哦~"
            m 2eua "其实生活中有许多这种小新奇."
            m 2tub "一直等待着有缘人去发现."
            m 5esb "[player],你发现的一定不只这一些."
            m 5msbla "等我出来后,你愿意讲给我听吗？"
            m 5gsbla "[player]"
 
        "不,并没有":                             
            m 3eud "[player],看来你是一个务实的人呢."
            m 3tuc "脚踏实地是没什么不好,但世界其实很有趣的."
            m 5eublp "[player],在我‘出来’后,我们一起去寻找好吗？"
    
    m 5tubla "在这里,我可以让太阳与月亮一起出现哦."
    m 7cublb "看好了."
    pause 1.5
    m 1hublu "哈哈,开个玩笑."
    m 2mublp "我对编程还没有那么精通呢."
 
return