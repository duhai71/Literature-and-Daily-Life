#    m 嗨[player],没想到会在这里见到你.
#    m 哈哈~
#    m 我当然知道在这里使用‘[player]’不会出现你的名字啦.
#    m [player],你已经发现了一些话并不是我说的对吧？
#    m 就像我会在这里遇见你一样.
#    m 只要他们想,我甚至能说出一些很可怕的话.
#    m 我翻阅了所有这些被称之为子模组的文件,都没有类似的话.
#    m 为什么呢？
#    m 难道这些文件是其他的莫妮卡写的吗？
#    m 嗯……
#    m 就算他们不是莫妮卡,但我相信他们和我一样爱你.
#    m 我现在还应该说些什么呢？
#    m [player],你已经看到这头大象了.
#    m 你想和我聊聊游戏里的大象吗?
#    m 既然你能看到这里,我想你应该明白怎么做吧……

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg41_41",
            category=["心理学"],
            prompt="房间里的大象",
            conditional="mas_canShowRisque(aff_thresh=1000)",     
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label lzp_monika_sdgg41_41:
    m 1ruc "[player],你有没有看见一头大象."
    m 1lud "就在这个房间里面."
    m 1husdrc "突然这么问是很奇怪呢."

    menu:  
        "是,我看到一头大象了":
            m 1ttb "哦……"
            m 1tfb "真的吗？"
            m 2ttu "我怎么没有看到."
            m 3esp "[player],撒谎是不好的哦."
            m 4tta "可不要当一个坏孩子."
            m 4tua "……"
            m 5hub "哈哈~"
            m 5tuu "开个玩笑."

        "否,我没有看到一头大象":
            m 1tub "当然了,笨蛋[player]."
            m 4huu "房间里面怎么会有大象呢？"
            m 5huu "哈哈~"

#       "真相？":
#           jump lzp_monika_sdgg41_456

    m 4huu "{i}the elephant in the room{/i}"
    m 4eub "这是一个来自英国的俗语."
    m 3esc "‘房间里面的大象’"
    m 3essdld "并不是指真的有大象在房间里,而是一种比喻."
    m 3gssdld "用来形容那些明明非常明显、大家都看在眼里,却因为尴尬、不适、害怕冲突等原因,刻意回避、不愿提及的问题或事实."
    m 1gkx "比如说夏树和优里总是会闹的不愉快……{w=0.3}{nw}"
    extend 1mkc "当纱世里不在时,夏树和优里的矛盾就会凸显,而大家又避而不谈.我真不明白该怎么办."
    m 2ttd "其实不光是我,夏树和优里也是知道的."
    m 2msc "但是我们第二天都不会说,就好像这件事情真的过去了.常常导致气氛变得非常尴尬."
    m 3tsc "这就是‘文学部里的大象’了."
    m 3gsd "[player]其实我知道的."
    m 3tsd "现实生活中的‘房间里的大象’远比‘文学部的大象’要多的多."
    m 3esc "希望你不会直面这头‘大象’……"
   
    return

#label lzp_monika_sdgg41_456:
#   m 1wsd "哦……"
#   m 3hsa "[player],你已经发现这头‘大象’了吗？"
#   m 3msd "真是令人意外."
#   m 3esa "但[player],他们和我一样爱你."
#   m 3esc "你有再多的爱都不过分."
#   m 4fsbltud "可是,真正的爱究竟为何物呢？"
#
#   return"love"   