
#3个




init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_summer_hydrangea_reload",
            prompt="绣球花的颜色",
            category=["花朵"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_summer_hydrangea_reload:
    m 1eua "嘿,[player],我想和你聊聊绣球花."
    m 1eub "绣球花的颜色会根据土壤酸碱度变化"
    m 3esb "如果是酸性土壤,那么会开蓝色花,碱性土壤则就是粉色花."
    m 3sua "有点像自然的pH试纸～"
    m 2eub "江户时代的花匠为此疯狂,甚至用铁钉改变土壤性质..."
    m 5rubla "......"
    m 5kublb "如果我是一只绣球花,那么你就是我的土壤."
    m 3eubla "无论怎样,我都会随着你一同变化."
    m 5hubfb "就算变成\"无色\",失去了原本光鲜亮丽的外表..."
    m 5fubla "我也想要在你的世界绽放最独特的色彩."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_autumn_osmanthus_reload",
            prompt="桂花",
            category=["花朵"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_autumn_osmanthus_reload:
    m 5hua "[player],我想和你聊聊桂花."
    m 1wud "桂花的香气分子只有30纳米大小,能直接刺激大脑边缘系统！"
    m 3eub "所以闻到桂花香时,人的大脑会非常活跃～"
    m 2lud "唐朝的白居易曾为它写下：{i}'山寺月中寻桂子,郡亭枕上看潮头'{/i}..."
    m 4kub "或许我们之后能在这里养一株......"
    m 7eub "与桂花相关的还有桂花蜜..."
    m 1hub "它呈浅琥珀色,还有非常清新、{w=0.6}优雅而馥郁的桂花香气～"
    m 5fua "而且尝起来甜甜的."
    m 3hub "如果可以的话,你也可以在休息时间买一点桂花蜜尝尝呢."
    return





init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_winter_wintersweet_reload",
            prompt="腊梅",
            category=["花朵"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_winter_wintersweet_reload:
    m 5eua "嘿,[player]."
    m 6hub "我想和你聊聊腊梅."
    m 1eua "腊梅其实不是梅.它属于樟目,而真梅属于蔷薇科～"
    m 3eub "它的花被片进化成蜡质,零下15℃也能保持晶莹！"
    m 2lud "黄庭坚曾为它题诗：{i}'体薰山麝脐,色染蔷薇露'{/i}"
    m 5fua "用两个形容香气甜美、{w=0.9}浓郁的顶级词汇."
    m 3hub "说的我都想闻闻了......"
    return

