init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_wantkiss",
            category=["莫妮卡","浪漫"],
            prompt="气鼓鼓",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True                      #这里表示是个随机话题其他部分不再赘述
        )
    )

label moonika_wantkiss:
    m 1efc "{w=2}..."
    menu:                                   
        "怎么了？":                             
            m 1efp "{w=2}..."
    menu:                                   
        "怎么挎着张小脸":                             
            m 1tfp "{w=2}..."
    menu:                                   
        "是有什么事让你生气了吗？":                             
            m 1wfp "{w=2}..."
    menu:                                   
        "不说话？":                             
            m 1efp "{w=2}..."
    menu:                                   
        "...":                             
            m 1efblp "{w=2}..."
    menu:                                   
        "...":                             
            m 1tfblp "{w=2}..."
    menu:                                   
        "到底怎么了啦":                             
            m 1tfblt "......{w=2}要亲亲"
    menu:                                   
        "小笨蛋":                             
            if mas_isMoniEnamored(higher=True):
                if mas_shouldKiss:                        #这三行,表示触发亲吻.<400好感时不触发.
                    call monika_kissing_motion_short  # type: ignore
            m 1tfbsp "{w=2}..."
    menu:                                   
        "怎么还挎着张小脸":                             
            m 1efbsp "{w=2}..."
    menu:                                   
        "不够？":                             
            m 1gfbst "......{w=2}不够...{w=2}还要！"
            if mas_isMoniEnamored(higher=True):
                if mas_shouldKiss:                        #这三行,表示触发亲吻.<400好感时不触发.
                    call monika_kissing_motion_short  # type: ignore
            m 1hubfa "嘻嘻~"
    
    return              