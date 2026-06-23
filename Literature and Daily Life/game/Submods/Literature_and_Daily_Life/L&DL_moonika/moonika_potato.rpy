init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_potato",
            category=["莫妮卡","浪漫"],
            prompt="削皮的土豆",
            random=True                      #这里表示是个随机话题其他部分不再赘述
        )
    )

label moonika_potato:
    m 1ekbsb "你知道吗,[player],你不理我的时候我的心情就像削了皮的土豆~"
    menu:                                    #这里表示创建玩家菜单
        "啥意思？":
            m 3ekbsb "你看,土豆是POTATO"
            m 1tkbsb "去了P就是oTATo"
            menu:                                    #这里表示创建玩家菜单
                "可爱捏":
                    m 1hubsb "<3"
                "幼稚鬼":
                    m 1hubsb "<3"
    
    return                  