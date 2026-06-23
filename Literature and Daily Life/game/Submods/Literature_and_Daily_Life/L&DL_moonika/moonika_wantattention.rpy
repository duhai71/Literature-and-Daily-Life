init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_wantattention",
            category=["莫妮卡","浪漫"],
            prompt="看看我",
            random=True                      #这里表示是个随机话题其他部分不再赘述
        )
    )

label moonika_wantattention:
    m 1eubla "{w=2}..."
    menu:                                   
        "怎么了？":                             
            m 1hubla "{w=2}..."
            menu:                                   
                "什么事这么开心呀~":                             
                    m 1hublu "{w=2}..."
                    menu:                                   
                        "是今天有什么不一样吗？":                             
                            m 1lublu "{w=2}..."
                            menu:                                   
                                "昨天做了一个美梦？":                             
                                    m 5hublu "{w=2}..." 
                                "今天天气不错？":                             
                                    m 5hublu "{w=2}..." 
                                "吃了什么好吃的？":                             
                                    m 5hublu "{w=2}..."   
                            menu:                                   
                                "怎么,变成小哑巴了？":                             
                                    m 1kubla "{w=2}..." 
                                "告诉我啦,你都快憋不住了.":                             
                                    m 1kubla "{w=2}..." 
                                "一脸坏笑,肯定没安好心！":                             
                                    m 1kubla "{w=2}..."     
                            menu:                                   
                                "再不说我可要开始担心了哦~":                             
                                    m 1fubla "{w=2}..." 
                                "我要生气了~":                             
                                    m 1fubla "{w=2}..." 
                                "我的时间很宝贵的知不知道,快说~":                             
                                    m 1fubla "{w=2}..." 
                            m 1tubla "{w=2}..."
                            m 1tublb "就是想让你好好看看我啦~"
                            m 1hubfb "嘻嘻~"
    return              