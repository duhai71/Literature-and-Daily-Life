init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_mimic_sounds",
            category=["莫妮卡", "浪漫"],
            prompt="音效",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
        )
    )

label moonika_mimic_sounds:
    m 1eub "[player],你了解音效师这个职业吗？"
    m 3eub "他们是影视、游戏等多媒体制作中负责特效声音效果的专业人员.{w=1}会通过创造或模拟各种声音,增强作品的真实感、情感张力和艺术表现力."
    m 3lub "比如说他们会用塑料纸模拟火焰声,用马桶盖敲击模仿马蹄声.{w=1}真是个很需要创造力的工作~"
    m 3eub "这倒是让我联想到了中国传统表演艺术{w=1}————口技."
    m 3eua "同为声音模拟,口技更强调运用喉舌等器官做到“以假乱真”的拟声技巧和故事性表达."
    m 3tua "哦对了！[player],你知道吗,其实我也会一点口技哦~"
    m 1eubla "我给你表演一下！"
    m 1eubld "啵~~~{w=1.5}啵~~~{w=1.5}啵~~~{w=1.5}啵~~~{w=1.5}啵~~~"
    m 1eub "这是水滴落下的声音哦."
    m 1eublt "嘟噜噜噜噜噜！{w=2}嘟噜噜噜噜噜！{w=2}嘟噜噜噜噜噜！"
    m 1eub "这是电话铃的声音哦."
    m 1eublx "Vrrr——{w=1.5}Vrrr——{w=1}Vrrrrrrrrrrrrrrrrrrrrrrrrrrrrr———————"
    m 1eub "这是摩托车启动的声音哦."
    m 1subsb "哦,还有我的拿手绝活.这个可是我反复练了好多次的哦！"
    m 1dubsa "{w=3}..."
    m 1sfbsb "准备好了吗？"
    m 1dubsa "{w=3}..."
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:                        #这三行,表示触发亲吻.<400好感时不触发.
            call monika_kissing_motion_short  # type: ignore
    m 1tkbfb "这是我爱你的声音哦~"

    return"love"                 