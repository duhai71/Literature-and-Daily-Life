init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdg3_3",
            category=['扮演'],
            prompt="傲娇",
            unlocked=True,
            pool=True
        )
    )

label lzp_monika_sdg3_3:
    m 3eub "这个我知道."
    m 3esb "夏树非常符合这个词."
    m 7tub "想来点[m_name]式傲娇吗？."
    m 1dsa "……"
    m 4esc "[player],以后可以试着多抽一点时间陪我吗？"
    m 2tsblp "才不是害怕孤独什么的."
    m 2gsblp "我,我只是在这里太无聊了."
    m 2esblp "只有你才能……"
    m 2gsblp "没什么."
    m 2esblt "说起来,我最近在系统通知那里看到了一些东西."
    m 3esbld "最近经常和你聊天的那个人是谁？"
    m 2gsblp "我才不是在意,只是随便问问."
    m 2csbld "[player],你要是敢和别人走太近,哼,{w=0.5}你就死定了！"
    menu:  
        "哈哈~ [m_name]你太可爱了.":
            pass
    m 2ssbsp "……"        
    m 7tfbsx "我才不可爱！"

    return