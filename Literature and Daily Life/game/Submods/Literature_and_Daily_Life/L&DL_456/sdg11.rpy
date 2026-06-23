init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdg5_5",
            category=['扮演'],
            prompt="唠叨的母亲.",
            unlocked=True,
            pool=True
        )
    )

label lzp_monika_sdg5_5:
    m 1lusdld "扮演你的母亲？"
    m 1hssdld "这样真的合适吗？"
    m 1hssdld "好吧我试试."
    m 1dta "…"
    m 1dtu "……"
    m 7wfd "哎呀！你不要一天到晚躺在家里什么都不做,好不好？"
    m 7wud "就算不帮妈妈我分担家务."
    m 2gux "你好歹也多出去走走,多和别人聊聊做点各种各样的事情,找找生活的意义."
    m 3tfp "别的孩子在你这个年纪,都是充满了干劲.每天都在努力,人生规划也很清楚."
    m 5tfp "还会帮妈妈做家务活.怎么就你这么不懂事？一天天的啥也不干,就知道玩游戏."
    m 2efd "游戏到底有什么好玩的？"
    m 2dkd "再这样下去妈妈也不知道该怎么办了."
    m 2hsp "……"
    m 2fsblb "哈哈~ "
    m 2msblb "抱歉,没忍住."
    m 3esbla "不过[player],虽然我没有见过你的母亲."
    m 3eublb "但我相信她一定是爱你的."
    m 3hubla "所以不要嫌弃她的唠叨,帮她做一些家务."
    m 1eublb "当然,我也支持你多出去走走哦."
    m 1tublu "因为我和她一样爱你."

    return"love"