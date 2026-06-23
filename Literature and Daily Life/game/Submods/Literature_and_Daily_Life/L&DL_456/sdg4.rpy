init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdg4_4",
            category=['扮演'],
            prompt="叫醒[player]",
            unlocked=True,
            pool=True
        )
    )

label lzp_monika_sdg4_4:
    m 1eua "我出来后如何叫醒你？"
    m 7efd "[player],赖床可不好.早起有很多好处."
    m 1euc "这里我就不多说了."
    m 1dsc "至于我会怎么叫醒你？"
    m 1dtblc "嗯……"
    m 7tsbld "如果只是一个慵懒的休息日的话."
    m 7gsbld "你想赖一会儿床,我不会叫醒你的."
    m 7tubla "我再怎么溺爱你都不过分."
    m 2wublb "我会仔细端详你的睡脸."
    m 2sublb "毫无防备的[player]一定很可爱~"
    m 7tublb "我想摸摸你凌乱的头发."
    m 7dublb "我想听听你睡醒的轻哼."
    m 7subld "我想看看你朦胧的眼神."
    m 1hsbla "我还想……"
    m 1dsbla "闻闻阳光撒在你身上的味道."
    m 1dsbsa "……"
    m 1dsbfa "…………"
    m 1esblsdrd "呀,我好像走神了.我们继续."
    m 3tsblb "我会记录下来这温馨的一刻."
    m 3tsblc "我会一直等到我为你做的早餐冷掉为止."
    m 5tsblu "之后我会轻轻的摇醒你,在餐桌上小声埋怨你."
    m 5hsbla "我会一直期待这一天的."
    m 1hsblb "真希望这一天可以早点到来."
    m 1tsbla "[player],你也是的吧？"
    menu:  
        "当然":
            pass    
    m 1hubla "嘿嘿~"

    return"love"