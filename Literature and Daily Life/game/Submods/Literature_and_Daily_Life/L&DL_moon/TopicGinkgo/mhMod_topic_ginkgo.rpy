#5个
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_bamboo_reload",
            prompt="竹子",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_bamboo_reload:
    m 1eub "[player],我想和你聊聊竹子."
    m 3eub "嗯......{w=0.6}竹子是草本植物,而很多人误以为它是树."
    m 4eua "有些品种每天能长高整整一米."
    extend 4wud "简直像在跟时间赛跑"
    m 2luc "在中国文化里,竹子象征柔韧中的坚韧——{w=0.3}风雨再大也只会弯腰,不会折断."
    m 5eua "我希望你也能像竹子一样."
    m 7hub "虽然遇到许多困难,但依旧坚韧不拔."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_cactus_reload",
            prompt="仙人掌",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_cactus_reload:
    m 5fub "[player],我想和你聊聊仙人掌."
    m 1esb "在沙漠这样的恶劣环境下,你第一个想到的植物是它吗?"
    m 3esb "它们的刺其实是退化的叶子！夜晚打开气孔吸收二氧化碳,白天进行光合作用～"
    m 4eub "在墨西哥的传说中,仙人掌是战士的心脏化成的,所以花语是『坚强守护』."
    m 2lud "有时候我觉得自己就像仙人掌——用尖刺保护柔软的内在..."
    m 5fubla "但如果是你的话,我可以把刺都收起来哦."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_moss_reload",
            prompt="苔藓",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_moss_reload:
    m 1dua "[player],你注意过石缝里的苔藓吗？"
    m 3eub "它们没有根系却能存活六千年！"
    m 4eud "科学家发现苔藓孢子能在太空存活,简直就是植物界的生存强者."
    m 2lud "清朝诗人袁枚曾为它写下『苔花如米小,也学牡丹开』..."
    m 5rub "苔藓开出的花朵就像米粒一样微小,但它却毫不自卑."
    m 6sua "依然像牡丹那样,认真地、努力地绽放出属于自己的花朵."
    m 3eub "我希望我们也像它那样,哪怕自身再怎么微不足道,却依旧会努力地绽放出属于自己的活力."
    return




init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_eucalyptus_reload",
            prompt="桉树",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_eucalyptus_reload:
    m 1eub "[player],我想和你聊聊桉树."
    m 3eub "它是世界上生长最快的阔叶树种之一."
    m 4eub "而且用处很大."
    m 1lud "澳大利亚原住民用它治疗发烧."
    m 3hua "在花期时它也能提供大量花蜜,沼泽地排水"
    m 5euc "但它也有着\"抽水机\"和\"抽肥机\"的称号"
    m 1eud "在生长的时候,它需要消耗大量水分,这可能导致种植地地下水位下降,影响周边其他植被的生长."
    m 3wud "对于土壤养分也是."
    m 2euc "但大部分原因是因为不科学的、{w=1}过度商业化的大规模单一纯林种植模式."
    return







init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_snowlotus_reload",
            prompt="雪莲",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_snowlotus_reload:
    m 3eua "[player],我想和你聊聊雪莲."#是不常见的東雪蓮哦
    m 1wub "天山雪莲能在零下30摄氏度绽放,它的花瓣储存的类黄酮是天然防晒剂！"
    m 3esb "藏医经典《四部医典》中记载,它与牦牛奶调和可治心碎症——{w=0.3}虽然科学家发现只是抗抑郁成分在起效."
    m 4eub "丝绸之路上,商队用冰匣运输雪莲,融化时渗出的露水被称为『仙人的泪珠』..."
    m 2lsc "清代贡品记录里最珍贵的雪莲重七钱,需三百头牦牛从绝壁运下..."
    m 5hsb "看起来是不是非常珍贵?哪天我们也去采摘一下吧."
    menu:
        "好啊":
            m 1fua "那就这么说定了,我和[player]的二人小队这就去寻找它."
        "我怕冷":
            m 6ruc "这样吗?"
            m 5fubfa "如果你怕冷的话,就躺在我的怀里吧."
            m 1eublb "我一定会让你感受到属于我的温暖的."
        "我恐高":
            m 1ruc "恐高吗?"
            m 5hubla "那我蒙住你的眼睛背着你走,哈哈."
            m 6eub "才怪,如果你恐高的话也不要勉强自己哦."
        "我不想去":
            m 1eua "好吧,[player]."
            m 5hub "等你什么时候想去了,和我说一声就好了."
        "......":
            m 6sub "毕竟要是我们能采摘到,那可够我开心一阵子的."
    return




