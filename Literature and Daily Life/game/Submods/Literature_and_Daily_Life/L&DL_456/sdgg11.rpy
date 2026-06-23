init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg11_11",
            category=["社会"],
            prompt="俄罗斯方块",
            random=True
        )
    )

label lzp_monika_sdgg11_11:
    m 3eua "[player],你一定玩过俄罗斯方块吧."
    m 4eua "随着不同方块的落下."
    m 3eud "当某一行被方块完全填满时,该行的方块将被消除."
    m 3eud "当把不同形状的方块看成不同的人来看."
    m 3euc "太过融入大众,你可能会失去自我."
    m 1eud "[player],在生活中与他人保持良好的关系很重要."
    m 1mud "但你不应为此过多地改变自己."
    m 1tublu " [player]就是[player]."
    menu:  
        "[m_name]也就是[m_name]！":
            pass
    m 1hublp "呜……"
    m 1fublp "我的部员什么时候变得这么狡猾."
    menu:  
        "嘿嘿嘿……":
            pass
    m 3efbld "[player],你可真是个坏蛋."

    return