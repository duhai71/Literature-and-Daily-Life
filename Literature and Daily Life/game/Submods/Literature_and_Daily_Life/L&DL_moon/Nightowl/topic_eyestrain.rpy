init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_eyestrain",
            prompt="熬夜的视力损伤",
            category=["健康"],
            random=True
        )
    )
#一个
label mshMod_topic_eyestrain:
    m 1ekc "[player],你有注意到屏幕蓝光在偷走你的夜视能力吗？"
    m 3esd "深夜瞳孔会放大到白天的三倍,{w=0.3}就像敞开的大门让蓝光强盗闯进来呢~"
    m 4wud "研究显示连续熬夜两周,{w=0.3}视网膜细胞死亡率会飙升20%%！"
    m 2euc "干眼症、飞蚊症、视物模糊...{w=0.3}这些都是眼睛在发SOS信号呀"
    m 5ekbfa "所以...我希望你能早睡早起,尽量别熬夜太多,好吗?"
    return


