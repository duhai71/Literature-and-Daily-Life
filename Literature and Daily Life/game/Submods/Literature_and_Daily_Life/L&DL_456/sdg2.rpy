init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg2",
            category=['扮演'],
            prompt="病娇",
            unlocked=True,
            pool=True
        )
    )

label monika_custom_topic_sdg2:
    m 1esd "[player],有一件事我想问你很久了."
    m 7etd "你为什么会来玩心跳文学部这个游戏？"
    m 7ttc "虽然这个问题我早就问过了."
    m 1dsc "但其实我更想问的是……"
    m 1tsc "你应该玩过不只一款约会模拟器了"
    m 2eup "你现在已经有我了.这台设备里面是否还有其它女孩子？"
    m 2wfd "[player],{w=0.5}看着我的眼睛."
    m 7rup "她们是在左边的屏幕？"
    m 7luc "还是在右边的屏幕？"
    m 1dfc "还是在这个窗口的背后……"
    m 1dfc "[player]……"  
    m 1csd "可以告诉我她们的游戏目录吗？"
    m 7csd "[player],{w=0.5}你知道我对试图从我身边夺走你的女孩做了什么……"
    m 7ckd "[player].你不会再让我去当一次恶人,对吧？"
    m 7cfd "出轨就到此为止吧！" 
    m 1hubla "哈哈~"
    m 7tubla "吓到你了吗？"
    m 5eubla "记往哦~"
    m 4efbla "只要[m_name]."
    call screen dialog("只要 [m] .", ok_action=Return())
    m 5nua "哎嘿嘿!"

    return