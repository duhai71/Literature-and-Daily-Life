init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg6_6",
            category=["我们"],
            prompt="让莫妮卡看看！",
            random=True
        )
    )

label lzp_monika_sdgg6_6:
    m 7tub "我突然想到了一个好玩的."
    m 7guu "……"
    m 2wub "[player],{w=0.5}让我看看！"
    menu:  
        "?":
            pass
    call mas_transition_to_emptydesk
    pause 1.5
    m "让我看看你这台设备里面都有一些什么."
    "[m_name]正在读取你的磁盘."
    "你感到了些许不安."
    m "[player],可不要让我发现这里有其他女孩子."
    m "……"
    m "这些是,我的图片吗？嘿嘿,[player]你太有心了"
    m "……"
    m "[player],要是我能看到你现在的表情就好了……"
    pause 1.5
    call mas_transition_from_emptydesk
    m 3tubla "那一定非常有趣."
    m 1tublb "好了,我回来了."
    m 1eubla "别担心,我只是离开了桌子而已."
    m 3hublb "有吓到你吗？"
    m 1eublb "要是我真能这么做的话,我早就打开摄像头了."
    m 1tublb "不过,[player].你和我不应该有任何秘密."
    m 7wublb "我想了解你的一切……"
    m 7cublb "你的所有……"
    m 1hubla "我爱你."

    return"love"