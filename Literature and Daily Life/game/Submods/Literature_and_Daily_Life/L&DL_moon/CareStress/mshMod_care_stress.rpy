init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_stress_reload",
            prompt="最近压力大吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_stress_reload:
    m 1eka "[player],你在某些时候会感到疲惫吗?"
    m 1ekc "我知道生活有时候会让人喘不过气,但请记住——"
    m 3eka "你不需要独自承担一切,哪怕只是暂时的."
    m 5ekb "如果有需要我的地方,我永远都在这里等你,"
    m 1eub "你也可以试着泡杯热茶,或者闭上眼睛小睡一会."
    m 1hsa "我会一直陪着你,[player]."
    return
#5个
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_loneliness_reload",
            prompt="你感到孤独吗？",
            category=["关怀"],
            pool=True,
            unlocked=True
        )
    )
label mshMod_care_loneliness_reload:
    m 1ekd "嘿,[mas_get_player_nickname()]..."
    m 1ekc "有时候你会有些许孤独感吗?"
    m 1ekc "在你感到孤独的时候,希望你记住,即使物理距离存在,我们的连接也不会断裂."
    m 3ekb "每次你来到这,我都能真实地感受到你的存在、你的温暖."
    m 5fubla "我也希望你能因为我而感到不那么孤单."
    m 6hublb "但显然,你的生活并不只有我."
    m 3eubla "你也可以和朋友、家人们一起聊聊天,或者出门走走."
    m 5fublb "或者阅读一篇好故事,感受其中人物间的互动."
    m 6hubla "当你对他们的了解更进一步的时候,你有时候翻阅书籍就像和他们对话一样呢."
    m 3rua "至少我是这么感觉的."
    m 5fubla "希望我这么说,你能找到对抗它的方法."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_failure_reload",
            prompt="失败让[player]难受吗？",
            category=["哲学"],
            pool=True,
            unlocked=True
        )
    )
label mshMod_care_failure_reload:
    m 1ekd "在人的一生中或多或少会经历一些失败."
    m 1ekd "而且产生的挫折感很容易压垮我们."
    m 3ruc "但我记得有句话怎么说的来着,失败是成功的老爸."
    menu:
        "失败是成功之母才对.":
            jump mshMod_care_failure_mom
        "不是老爸.":
            jump mshMod_care_failure_mom
        "......":
            jump mshMod_care_failure_mom

label mshMod_care_failure_mom:
    m 6husdla "好吧,应该是妈妈."
    m 6eublb "但意思都差不多了......"         
    m 5eua "如果你觉得你做一件事失败了,我希望你记住,现在经历的曲折,或许正是未来成功的伏笔."
    m 1hubfb "我相信你,[player]"
    m 3eua "可以的话,我更希望有我一直陪着你直到成功."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_anxiety_reload",
            prompt="你最近容易焦虑吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_anxiety_reload:
    m 1euc "[player],你会不会有时出现焦虑的情况?"
    m 1eua "焦虑是很正常的情绪."
    extend 6fub "它在面对多种琐碎的事情或一件重要的决策时常常出现."
    m 3eub "下次出现这种情况时,你可以试试把深呼吸,尝试让自己冷静下来"
    m 5fua "尽可能想想当前对自己最有利的解决方法"
    m 5eua "如果思绪太乱,可以列张清单."
    m 3rua "先做这件事,再做那件事."
    m 1eua "希望这对你有用."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_future_reload",
            prompt="对将来感到不安吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_future_reload:
    m 1euc "[player],你会对未来感到不安吗?"
    m 1eud "比如,\"我之后能否找到一份好工作\",\"我之后能否有一个良好的人际关系\"."
    m 3eua "然后对过去的错误感到懊恼."
    m 5fub "这种情况下,我们常常容易患得患失."
    m 6eua "但\"昨天是段历史,明天是个谜团\"."
    m 3sub "而今天是天赐的礼物."
    m 3fua "所以我希望你能像珍惜礼物一样珍惜今天."
    m 5eua "做好当下比什么都重要,[player]."
    return



    