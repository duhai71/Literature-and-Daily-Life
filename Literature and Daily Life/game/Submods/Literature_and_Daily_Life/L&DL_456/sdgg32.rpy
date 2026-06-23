init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg32_32",
            category=["心理学"],
            prompt="中二病",
            random=True                      
        )
    )

label lzp_monika_sdgg32_32:
    m 3tsu "[player],你有没有过一段中二的时候？"
    m 3lsa "比如,拿起一块圆形的木板幻想自己是美国队长."
    m 3lsa "摆出一个姿势,幻想从手臂中发出光线."
    m 3hsb "或者,挥舞一根木棍,认为自己是齐天大圣."
    m 1musdlb "哈哈,我知道聊这些实在是有一些尴尬."
    m 1fua "[player],你愿意和我聊聊吗？"
    
    menu:                                    
        "是的,我曾有过这样一段时光":                             
            m 1hua "哈哈~"
            m 1tub "别害羞,[player]."
            m 1huu "我明白现在来看那些行为实在是太幼稚了."
            m 1kub "但,[player].我觉得那个时候的你一定非常可爱哦~"
            m 1mua "没有取笑的意思啦."
            m 1tub "[player],谢谢你愿意和我聊这些."
            m 1hua "我离你又更进一步了."
            
        "没有":                            
            m 1eud "哦？是这样吗."
            m 1eua "[player],我明白了."
            m 1hua "[player],谢谢你愿意和我聊这些."

        "我不太想聊这个":                            
            m 1esd "[player],我知道了."
            m 1tsp "可以明确拒绝自己不想要的,也是一种智慧."
            m 1hsa "哈哈~"
    
    return         