init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_handsome",
            category=["莫妮卡","浪漫"],
            prompt="世界上最帅的人",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True                      #这里表示是个随机话题其他部分不再赘述
        )
    )

label moonika_handsome:
    m 1ekbla "[player],我最近日不能思、夜不能寐~"
    menu:                                   
        "怎么了？":                             
            m 1dkbla "我最近看到了一张照片,确切说是一张脸,深深地印在了我的脑海里..."
            menu:                                   
                "一张脸？":                             
                    m 1gkbla "你不懂,这是世界上最帅的一张脸..."
                    menu:                                   
                        "给你迷得":                             
                            m 5gkblb "唉,在脑子里简直挥之不去呢~"
                            menu:                                   
                                "我倒要看看了...":                             
                                    m 5ttblb "你？{w=1.5}[player],你吗？{w=1.5}实话说,我不是很想和你,[player],分享欸..."
                                    m 5ttblp "你肯定要扫我兴致,说什么“这人长得有什么帅的”这种烦人话..."
                                    menu:                                   
                                        "不给我看？":
                                            m 1ttblp "你保证不说这张脸不帅我才给你看."
                                            menu:                                   
                                                "我保证":                             
                                                    m 1tublc "那行吧."
                                                    m 1tublc "你最好把我的窗口调成全屏,这样才能看到每一处细节."
                                                    m 1dsbla "...{w=2}{nw},"
                                                    extend 1tublb "看好了哦~"
                                                    window hide
                                                    show black zorder 100 with Dissolve(2.0)
                                                    $HKBHideButtons()
                                                    pause 4.0
                                                    hide black with Dissolve(1.0)
                                                    $HKBShowButtons()
                                                    m 1hubsb "哈哈哈哈~{w=1}{nw}"
                                                    extend 1tubsa "哦,看看这张帅脸和自己面对面后露出的表情！"
                                                    m 3tfbsb "[player],帅可是跟长相无关的哦.帅是一种气质~"
                                                    m 4tfbsb "所以不管别人怎么说,在我这里,你永远都是最帅的哦~ {w=2}{nw}"
                                                    extend 4etbsd "欸,等一下！"
                                                    m 2etbsd "我觉得还需要补充点什么,就一点点... {w=2}{nw}"
                                                    extend 4hubsb "哦我知道了,需要加上一个点睛之笔！{w=1.5}让我来加一下~{w=1}{nw}"
                                                    if mas_isMoniEnamored(higher=True):
                                                        if mas_shouldKiss:                        #这三行,表示触发亲吻.<400好感时不触发.
                                                            call monika_kissing_motion_short  # type: ignore
                                                    m 1tubfb "嘿嘿,这样这张脸就完美了！"

    return                  