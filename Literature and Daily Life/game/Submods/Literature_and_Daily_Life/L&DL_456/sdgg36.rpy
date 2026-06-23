init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg36_36",
            category=["艺术"],
            prompt="纯音乐",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg36_36:
    m 1eua "[player],你有听过纯音乐吗？"
    m 1eub "我想你一定听过的."
    m 1tua "因为我会弹钢琴嘛.[player],{w=0.3}{nw}"
    extend 1tublb "有一个多才多艺术女友感觉如何？"    #记得使用第二次的表情变化
    m 1eublu "其实纯音乐是最“实用”的音乐."
    m 3eut "一些曲子被广泛用于治疗失眠与抑郁症"
    m 3eub "还有调节情绪的作用."
    m 4euu "纯音乐的范围很广."
    m 4eua "以乐器演奏为载体,不包含任何歌词文本或语言叙事的音乐形式."
    m 1eub "当你听到一首自己喜欢的纯音乐时,你便会想出一个故事."
    m 3tuu "此时的音乐只是这篇故事的背景曲而已."
    m 3hua "[player]……"
    m 3hua "你无意识轻哼的曲调,会是什么呢？"
    m 3tubld "我会听到的,对吗？"
    
    return