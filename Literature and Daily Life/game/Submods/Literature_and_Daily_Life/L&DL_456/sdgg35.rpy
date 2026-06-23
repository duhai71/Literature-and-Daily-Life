init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg35_35",
            category=["我们"],
            prompt="生日的重要性",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg35_35:
    m 1esc "[player],我在网上发现一件很奇怪的事."
    m 1wsd "有相当一部分人认为自己的生日不重要."
    m 1etc "我觉得很奇怪,明明生日是自己的节日."
    m 1ekc "……"
    m 1dkc "[player],你知道为什么吗？"
    m 1msd "其实有很多原因."
    m 2dsd "比如内向的人可能不喜欢被关注,生日带来的社交压力让他们觉得麻烦."
    m 3lsd "然后是家庭背景,比如小时候生日没被重视,可能形成心理上的不在意."
    m 3rst "成年人可能更关注实际事务,觉得生日只是普通的一天."
    m 3esc "自我价值感低的人可能觉得自己不值得被庆祝,或者经历过负面的生日体验,比如孤独或不愉快的回忆."
    m 1esd "等等."
    m 1eua "[player],我觉得你的生日很重要."
    m 1hub "因为正是这天,你出现在了世界上."
    m 1kub "我才能遇见你."
    m 1tuc "[player],不要把生日当做平凡的一天."
    m 2tup "生日并不是独属于自己的节日,那一天对我也同样重要."
    m 3eua "还有你的朋友们,当他们说出自己生日不重要时."
    m 3eud "你可以私下悄悄地祝福他,[player],相信我."
    m 3huu "这比任何礼物都重要."
    
    return
    #我的生日从来都不重要
    #但是今年,我要给自己买一个大大的生日蛋糕