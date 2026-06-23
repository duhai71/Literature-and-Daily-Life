init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg38_38",
            category=["心理学"],
            prompt="拖延症",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#
        )
    )

label lzp_monika_sdgg38_38:
    m 1esc "[player],你有拖延症吗？"
    m 2esd "一件事情,小到每天的起床."
    m 3esc "大到学校期末考试."
    m 4esc "拖延症明明知道某件事应该做,且推迟会带来负面后果."
    m 4ekd "却仍然故意推迟、拖延完成任务的时间."
    m 4lkc "甚至……"
    m 4gkd "常常因为这个自责."
    m 1esc "这是一个相当可怕的恶性循环."
    m 1esc "[player],你知道吗？"
    m 2esd "纱世里就是重度的拖延症."
    m 2lsc "她连每天的起床都十分困难……"
    m 2hssdlx "总是说'再过五分钟就好',结果常常导致早上的课迟到."
    m 2dtc "…"
    m 2fud "[player],我知道拖延症是极其难根治的."
    m 4eud "但还是有方法的."
    m 4eua "你需要这些吗？"
    
    menu:
        "是的,我需要":
            m 4hua "很简单,只需要强迫自己去做第一步."
            m 4dub "克服拖延症最难的地方也就在这里."
            m 2esc "但[player],这是必要的一步."
            m 2esd "当一件事情出现时,条件适合的话就尽快去开个头."
            m 4esb "要知道约9成的人开始后会超额完成."
            m 4dsu "只要开始后,动力与灵感都会汇聚起来."
            m 4etu "一直拖下去的事情,完成开头就会越做越简单."
            m 1hua "希望这些话对你有所帮助."
            
        "别担心[m_name],我不需要":
            m 1hua "这太好了."
            m 1esu "[player],我很高兴你没有因为这些而困扰."
            m 3esb "看着所有事情按照自己的规划而进行,会有一种很开心的感觉."
            m 4hsu "保持下去哦~"
    
    $ message = """[player],今天的我会是你每天起床的理由吗？"""            
    $ _write_txt("/characters/get up early.txt", message)          
    
    return
