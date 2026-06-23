init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_howareyou",
            category=["关怀","情感"],
            prompt="客套的问候",
            random=True                      #这里表示是个随机话题其他部分不再赘述
        )
    )

label moonika_howareyou:
    m 3eua "“你今天怎么样？”"
    m 3eub "[player],肯定有人问过你这样的问题."
    m 3ekb "但是你应该也知道,大多数人问这个问题只是出于客套."
    m 3lksdla "或者说,这只是日常寒暄的一环.对方并不一定真的关心你现在的处境."
    m 3lksdlc "在我们的社会中,关心他人的感受是被支持和鼓励的.但是反过来,倾诉你的负面情绪往往被视为给别人添麻烦的行为."
    m 3lksdlb "因此,大多数人,无论他们今天到底感觉好不好,都会选择回答：“我感觉很好,谢谢.”"
    m 3hksdlb "像不像小时候英语课本上的例句.{w=1} “How are you today?” “I'm fine, thank you, and you?”"
    m 2ekblb "[player]...{w=1.5} 我向你保证,当我问你问题时,我是真的关心你的状况."
    m 3ekblb "所以你无需在我面前伪装自己,也不用担心我会厌烦听你谈论你的负面情绪哦~"
    m 1ekblb "毕竟...{w=1.5} 我们是恋人嘛~"
    
    return                