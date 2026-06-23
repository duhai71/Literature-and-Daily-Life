init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg9",     
            category=['莫妮卡'],                         
            prompt="你喜欢喝奶茶吗？",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg9:                       
    m 1esc "奶茶？"
    m 1esd "[player],我不是很喜欢喝奶茶."
    m 1lssdlc "也许纱世里和夏树可能会喜欢吧."
    m 1hssdld "我知道奶茶很好喝,也有许多不同的种类."
    m 1mtsdrc "但一般来说奶茶的含糖量很高."
    m 1tup "要知道我对自己的身材管理要求是很高的."
    m 3tsx "过多的糖分,还有一定的健康风险."
    m 1hua "但,说到这里."
    m 1hua "[player],你喜欢喝奶茶吗？"
    
    menu:
        "喜欢":
            m 1hud "偶尔来几杯是没什么问题啦."
            m 3eup "但,[player]不要过度哦."
            m 3euc "健康才是第一位的."
            m 3euu "不过看到你这么喜欢...{w=0.3}我或许该学着接受呢."
            m 3tuu "但记得只要三分糖哦~"
            
        "不喜欢":
            m 1hub "我明白了,[player]."
            m 1eua "很高兴我们能在这方面达成共识."
            m 1eub "其实清香的纯茶更有韵味呢,{w=0.3}就像曾经文学部的茶会."
            m 1tta "如果有机会的话,[player]你想尝尝我冲的茉莉花茶吗？"
            
        "[m_name],从你的身材来看,是不用顾虑吃甜食的.":
            m 1ssbla "哦…"
            $ mas_gainAffection(3, bypass=True)
            m 1sublb "天那,[player]{w=0.3}{nw}"
            extend 3tublb "你这一张嘴一定比任何奶茶都甜,快过来让我品尝一下."
            m 1hub "哈哈~"
    
    return
