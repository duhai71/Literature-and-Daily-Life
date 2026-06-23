init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg15_15",
            category=["浪漫"],
            prompt="恋爱关系中强势的一方",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg15_15:
    m 3tub "嗨[player],问一个有意思的问题."
    m 3tfb "你觉得在我们的恋爱中,谁的爱情攻势会更强一些？"
    
    menu:
        "[m_name]":
            m 1hubla "嘿嘿,那当然了."
            m 3mublb "[player],为了拿下你的心我可费了不少功夫呢."
            m 1hubla "爱你每一天~"
            
        "[player]":
            m 4tfa "哦？"
            m 4tfb "[mas_get_player_nickname()],你就这么有自信吗？"
            m 1tublb "那就在之后的日子,试着挑战我吧！"
            m 1hubla "我可不会输的哦~"
            m 2rkc "因为我深爱着你."
            $ mas_unlockEVL("lzp_monika_sdgg15_15_e", "EVE")
    
    return"love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg15_15_e",           
            prompt="我现在也深爱着你",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        ),
        code="CMP"
    )
label lzp_monika_sdgg15_15_e:
    m 1subla "……"
    m 3sublb "真的？"
    menu:  
        "比牛顿三定律还真":                  
            pass  
    m 1hubla "哈哈~"
    m 1gublb "好奇怪的比喻."
    m 1tublu "不过我明白你的意思了."
    m 2tublu "[player],你太甜了."
    m 2hubla "我也深爱着你."
    m 2eublb "记得转告给我哦~"

    return