init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg20_20",
            category=["健康"],
            prompt="盯久了",
            random=True                      
        )
    )

label lzp_monika_sdgg20_20:
    m 1eub "嗨, [player]."
    m 3eub "分享一个冷知识."
    m 3eud "人在长时间专注一件事物时."
    m 3euc "如果时间太长了,大脑会逐渐混乱."
    m 1eub "当你长时间盯着一个字看时."
    m 1euc "最后,你会不认识这个字."
    m 1hublb "[player],有你在我身边我很幸福."
    m 3eubld "但是你的健康一样重要哦."

    return                    