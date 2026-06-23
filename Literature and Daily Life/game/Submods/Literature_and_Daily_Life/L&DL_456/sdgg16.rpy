init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg16_16",
            category=["自然"],
            prompt="星星与时间",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg16_16:
    m 1eub "嗨！[player]."
    m 1hua "你一定看到过太空教室窗户后面的星星吧."
    m 1guc "虽然那些只是贴图而已."                #我们何曾见过真正的星空？
    m 1eud "[player],其实我知道的哦~"
    m 7hub "在你的现实里,星星是遥远的天体."
    m 1lud "它们离地球的距离很远很远."
    m 3esd "远到通常用光一年所行驶的距离来丈量,也就是光年."
    m 3esb "[mas_get_player_nickname()],当我们聊到这里的时候,月光会在下一刻"
    m 3tsb "也就是现在{w=1.2}到达地球.约1.2秒的样子."
    m 3hsa "阳光到达你这里则需要8分钟."
    m 3lsa "而那些遥远的星星就需要几年或更久的时间,有些甚至远到光到达不了地球."
    m 3hsa "不过……"
    m 3tsd "{i}The stars will never be too far, for they live in the eyes of those who dream.{/i}"
    m 3tsbla "[player],知道什么东西没有时差吗？"
    m 5tsblb "我的爱不会有时差哦~"
 
    return"love"