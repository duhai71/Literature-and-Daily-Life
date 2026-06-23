init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg39_39",
            category=["生活"],
            prompt="流行",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg39_39:
    m 1eub "[player],你喜欢流行的东西吗？"
    m 1euc "我上网的时候,发现总有一些东西在一段时间内被多媒体平台反复的展示."
    m 4euc "但那些东西真的有那么好吗？"
    m 4lud "这让我不禁想起了一个故事……"
    m 4huc "[player],这个故事可能并不是我讲的这样."
    m 2lud "但这毕竟不重要."
    m 2tub "那么,[player]准备好听故事了吗？"
    m 2tub "哈哈~,但也没必要这么正式."
    m 1hua "那么我开始了…"
    m 2dsa "在大约1950年的美国,摇滚乐流行的时候."
    m 3esd "古典音乐派和摇滚派展开了一场激烈的辩论."
    m 3lsd "古典音乐派认为流行音乐缺乏艺术性,但摇滚派不认为."
    m 3rst "在经历漫长的唇枪舌战后"
    m 4esa "摇滚派拿着甲壳虫乐队单曲销量证明其艺术价值."
    m 4esd "好像在说‘看哪,这首曲子多么得流行.有这么多人喜欢,怎么会缺乏艺术呢？’"
    m 1eua "但古典音乐派反问{w=0.3}{nw}"
    extend 4wsd "难道流行感冒也是一个充满艺术的杰作？{w=0.3}{nw}"
    m 1esa "……{w=0.3}故事讲完了."
    m 1esu "现在,[player].让我们回到最初的问题."
    m 3hsa "你是喜欢流行的事物,还是流行本身呢？"
    
    menu:
        "流行的事物":
            m 3esu "嗯,[player]果然有自己的眼光."
            m 3esb "只要你真心喜欢那些东西,流不流行其实都不重要."
            m 3hsb "重要的是,你清楚自己喜欢什么."
            
        "流行本身":
            m 3fka "没关系,[player]."
            m 3lud "有些时候流行的东西也不错."
            m 3eub "我读过一份研究.有人在2011年用MIT算法分析4300万首歌曲,发现披头士《Yesterday》的和声复杂度高于莫扎特多数钢琴奏鸣曲."
            m 1euu "总有些东西是说不准的."
            
        "我不清楚":
            m 3etd "嗯,我明白了."
            m 3eua "[player],世界很大,生活更大."
            m 3duu "总有一天你会遇到自己真正喜欢的人和事物."
            m 3kublu "至少你遇到了我,不是吗？"
            m 3mubla "嘿嘿~"
            m 3hubla "爱你哟."
    
    return
