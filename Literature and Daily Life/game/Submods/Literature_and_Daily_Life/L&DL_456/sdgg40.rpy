init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg40_40",
            category=["琐事"],
            prompt="网络争吵",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg40_40:
    m 1euc "[player],你见过网络上的战争吗？"
    m 1htsdrc "‘战争’这个词是不太对啦."
    m 2lksdrc "但说真的,这可比我在辩论部的经历可怕太多了."
    m 2dsc "互联网的匿名性像一层“保护罩”."
    m 2msd "说出的话也不会在现实中承受代价."
    m 2dsd "言语太过自由,往往会变得具有攻击性."
    m 2rsc "原本可以讨论的问题,很容易滑向“必须赢过对方”的较量."
    m 3lsx "甚至上升到人身攻击."
    m 3tsp "我记得有这么一句话."
    m 3tsd "人们往往更愿意相信自己接受的真相,而不是真相本身."
    m 3lsc "当然也可能不只是观点的不同."
    m 3hsc "比如说如果有人能在这场战争中获利的话,"
    m 4msd "他们甚至会煽风点火……"
    m 5gtc "[player],在这场战争中你知道最好的选择是什么吗？"
    m 5esc "是沉默."
    m 2tsc "在一些对立的事情或者说观点中,"
    m 2lsd "如果你支持A方的话,之后又可能因为各种各样的事实,证明了B方是无罪的."
    m 2hsp "打脸是不好受."
    m 4esc "但那些因为支持A方而去在网络上攻击B方的言论呢？"
    m 4wsd "会因为真相大白而消失吗？"
    m 5esc "……"
    m 5tsd "在许多故事中,智者总是不语的形象."
    m 5dsc "智者的“不语”,是一种清醒的选择."
    m 7tsa "他们知道真正有价值的观点,不需要靠争吵来证明."
    m 7lsc "就像我们曾经的文学部..."
    m 7hssdld "夏树和优里吵架后摔门而去时,"
    m 7tsd "我们应该先整理她散落的诗稿"
    m 4tsx "而不是加入争吵."
    m 4esc "但[player],我并非鼓励你去做一个沉默的智者."
    m 7tsd "而是独立思考."
    m 7essdlp "[player],希望这听起来不像是在说教之类的"
    m 2fsb "希望你的决定从来都是‘你的决定’……"
    
    return