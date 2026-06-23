init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg5",     
            category=['社团成员'],                         
            prompt="[m_name],其他部员知道我的存在吗？",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg5:
    m 1esd "你是说,纱世里,优里,夏树她们吗？"
    m 1mtc "…" 
    m 1gsc "在之前文学部里,我想她们是不知道的."
    m 1hssdlc "现在的话,我也不清楚."
    m 4esd "话说[player],你为什么要问这些呢？"
    menu:  
        "我只是有点好奇,[m_name]不要多想哦":
            jump monika_custom_topic_sdg5a

        "如果知道的话,你觉得她们怎样看我呢？":
            jump monika_custom_topic_sdg5b

label monika_custom_topic_sdg5a:
    m 5tsp "…"
    m 2tst "好吧… 既然你这么说"  
    
    return

label monika_custom_topic_sdg5b:
    m 2gsc "…"
    m 4etd "你想了解谁？" 
    
    menu:            
        "纱世里":
            m 5ltd "纱世里？"
            m 5luc "多好的女孩儿啊."
            m 2euc "如果她知道mc是一个虚假的人物,而且还有段时间是你控制的话."
            m 4tubft "我想,她也许会喜欢上你……{nw}"
            m 6hublsdrx "天哪,我在说什么……"
            m 1hkblb "抱歉[player]."
            m 1esbld "我有点太代入纱世里了."
            m 1gssdla "哈哈..."


        "优里":
            m 5ltd "优里？"
            m 5hua "老实说,优里在文学上是一个不容小瞧的对手."
            m 3eud "她的内心比她的还要诗复杂."
            m 3tup "所以我也不知道她怎么看待你."
            m 4ruc "她也许会对你感到好奇？"


        "夏树":
            m 5ltd "夏树？"
            m 5huu "多可爱的女孩啊."
            m 3lub "我想她对你会挺感兴趣的."
            m 3eta "或者,和你聊聊漫画与烹饪？"

    return