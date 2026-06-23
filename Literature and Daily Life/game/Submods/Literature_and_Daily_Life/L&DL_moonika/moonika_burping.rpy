init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_burping",
            category=["莫妮卡"],
            prompt="打嗝",
            random=True                      #这里表示是个随机话题其他部分不再赘述
        )
    )

label moonika_burping:
    m 6euo "嗝！"
    m 6eksdlu "哦,抱歉,[player].我——"
    m 6eusdlw "嗝！"
    m 6eksdlb "我刚才应该是吸了冷气.现在开始控制不住地——"
    m 6eublsdrw "嗝！"
    m 6eusdrt "——打嗝了.实在不好意思~"
    m 6eubssdlw "嗝！"
    menu:                                    
        "你打嗝的样子……有点可爱":                            
            m 6eubssdlu "你说什么——"
            m 6eubsw "嗝！"
            m 6efbssdlt "给你抓到机会笑话我了吗？"
            m 6efbssdlt "太过分了,[player]！"
            m 6efbssdlp "{w=3}..."
            m 6eubfsdrw "嗝！"

            return              