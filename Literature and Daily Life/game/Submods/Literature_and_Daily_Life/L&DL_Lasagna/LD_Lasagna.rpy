init 5 python:     
    addEvent(          
        Event(
            persistent.event_database,
            eventlabel="monika_Lasagna20",
            category=['另外的话题'],
            prompt="创作",
            random=True,
            pool=True,
        )
    )

label monika_Lasagna20:
    m 1eua "哦，对了亲爱的."
    m 2eub "我突然想到一个问题."
    m 4eub "你有没有经历过被一个不知从何而来的创作动力所充盈的体验?"
    m 3rua "它可能是一时冲动之下出现的万千思绪,驱使着你将其实现."
    m 3lub "亦或是深思熟虑后所落下的一笔一划,指尖按动的一个又一个按键."
    m 2eub "所以...[player],你经历过吗?"
    $_history_list.pop()
    m 2eub "所以...[player],你经历过吗?{nw}"
    menu:
        "经历过":
            m 1hub "哈哈,我知道了,不管这份动力是否成功驱使着你完成了某些成就,至少这也是人生中的一种宝贵的体验."
            m 5eua "对于我来说，驱使着我完成这么多事情的动力就是我对你的这份爱."
            return
        "我现在就有这样的感觉":
            m 1wub "是吗?"
            m 1hua "那我们就凭借着这份动力,一起去做一些对自己而言有意义的事情吧!"
            m 1hub "期待看到你的成果哦[player]"
            return
        "还没有":
            m 3eua "也没关系,亲爱的."
            m 1eua "现在你只是缺少某个契机."
            m 2tub "相信我们绝对聪明的[player]一定会经历这样的美妙时刻呢."
            m 5eub "我们就等着看吧!"   #歪头
            return
    
init 5 python:
    addEvent(           
        Event(
            persistent.event_database,
            eventlabel="monika_Lasagna21",
            category=['其他部员'],
            prompt="文学部的日常",
            random=True,
            pool=False,
        )
    )
    

label monika_Lasagna21:
    m 1rua "有时候我会情不自禁地回忆在文学部的时光"
    m 1dua "阳光透过玻璃照亮我们的活动室"
    m 3rua "Yuri和Natsuki有时背靠背地看她们喜欢的文学作品"
    m 3etb "尽管有时莫名其妙地产生矛盾，但最后都会重归于好。"
    m 1lub "Sayori的腮帮子在这个时候一直都是鼓起来的"
    m 5dub "她们的眼睛在光线下是那么的晶莹，那么地...可爱..."
    m 5duc "...."
    return
    
init 5 python:
    addEvent(           
        Event(
            persistent.event_database,
            eventlabel="monika_Lasagna22",
            category=['另外的话题'],
            prompt="关于galgame",
            random=True,
            pool=True,
        )
    )
    

label monika_Lasagna22:
    m 1eua "我知道ddlc也是galgame."
    m 1eub "但其实我更在意的是人们对galgame的看法"
    m 3eub "galgame指的是视觉小说类游戏，对吧？"
    m 4rtb "但不知道从什么时候开始，有些人对galgame的侧重点逐渐由视觉小说倾向于'色情游戏'."
    m 3eub "导致有些人将galgame误解为'色情游戏'。"
    m 3eka "..."
    m 1hksdlb"啊哈哈...我在说些什么呀？ "
    m 3rub "人有时都会这样，不由自主地胡思乱想."
    m 1eua "顺带问一下，[player]你听说过《千恋万花》吗？"
    $_history_list.pop()
    m 1eua "顺带问一下，[player]你听说过《千恋万花》吗？{nw}"
    menu:
        "听说过":
            m 1sub "是吗?看来以后你可以告诉我一些有关《千恋万花》的事情了呢."
            m 1hub "我热衷于学习新鲜事物呢,啊哈哈."
            return
        "玩过":
            m 1fublb "这样看来我在你心中的分量很重呢."
            m 5hub "否则你怎么还会在这里陪我呢,亲爱的."
            return
        "没有":
            m 1eua "没关系,亲爱的,我对其也知之甚少."
            m 3rua "如果你感兴趣的话你可以去了解一下."
            m 3etsdlb "但我要提醒一下,听说里面有18+内容."
            m 2tub "所以我更愿意在我的监督下让你去浏览相关内容,防止你被其它人拐跑了."
            m 1hub "啊哈哈."
            return

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="Lasbye1",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label Lasbye1:
    m 1eub "记得保持健康哦"
    m 3fub "到我'出来'的那天...我希望可以看见神采奕奕的你..."
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="Lasbye2",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label Lasbye2:
    m 1ekd "等等，[mas_get_player_nickname()]."
    m 1ekc "..."
    $ _history_list.pop()
    m 1eku "...{nw}"
    menu:
        "怎么了？":
            m 1ekc "..."
            m 1eua "..."
            m 1eub "再让我多看你一眼，不知道下一次见面是什么时候..."
            m 1eublb "我爱你"#加语音?蒜鸟蒜鸟
            return 'quit'

init 5 python:
    addEvent(           
        Event(
            persistent.event_database,
            eventlabel="monika_Lasagna23",
            category=['另外的话题'],
            prompt="我可能赶不上你的生日了",
            random=False,
            pool=True,
        )
    )
    

label monika_Lasagna23:
    m 1dkc "唉...."
    m 1ekc "我能理解你的心情,亲爱的..."
    m 4rko "不仅是你会赶不上我的生日,甚至我有时也不能将对你的生日祝福及时传递给你."
    m 3eka "你有没有把日历调到我生日那天提前给我过生日的想法?可能你已经这样做了."
    m 3rko "是因为你工作太忙了,没时间陪我过生日."
    m 3lkc "又或者是学业原因,你甚至都没有打算过自己的生日."
    m 2dho "不论如何,[player],我想说的是..."
    m 2ekblb "我爱你,不论发生了什么事情,我都理解你."
    m 5dha "即使在我生日那天你无法陪伴在我身边,但你那来自未来的温柔祝福依旧能萦绕在我的耳畔."
    m 5eka "一次又一次地让我沉溺于思念中摆脱孤独的诞辰."
    m 5eub "放心吧，宝贝，我会一直等到你回来的时候."
    m 5fub "只要能见到你，每时每刻都是我最幸福的时光."
    m 5hub "我爱你."
    return "love"

init 5 python:
    import store
    flag_file = "Submods/Literature_and_Daily_Life/L&DL_Lasagna/别删除DoNotDelet.txt"
    if renpy.exists(flag_file):
        lasagna_DoNotDelet_miss = False
    else:
        lasagna_DoNotDelet_miss = True
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Lasagna_Don_1",
            prompt="???",
            pool=True,
            conditional="not store.lasagna_DoNotDelet_miss",
        )
    )
label Lasagna_Don:
    m 1euu "[player]，你是不是删除了character文件里的什么东西?"
    $_history_list.pop()
    m 1euu "[player]，你是不是删除了character文件里的什么东西?"
    menu:
        "是的":
            m 1euu "亲爱的，你是不是想背着我干什么见不得人的事呢？"
            m 1euu "啊哈哈，我开玩笑呢。"
            m 1euu "只要我想，你在这个设备上干了什么我都可以知道"
            m 1euu "但是，亲爱的你也有你的隐私"
            m 1euu "所以在我调用数据前会征得你的同意哦"
            m 1euu "至于你删了的文件...忘了它吧。"
            m 1euu "放心，也不是什么重要的东西，一切照旧吧"
            return
        "没有":
            m 1euu "真的?{nw}"
            m 1euu "真的?"
            menu:
                "真的没删东西":
                    m 1euu "唔，我知道了。"
                    m 1euu "可能是你的一个无心之举吧，没关系"
                    m 1euu "放心，也不是什么重要的东西，一切照旧吧"
                    return
                "好吧，我确实删了character里的某个文件":
                    m 1euu "亲爱的，你是不是想背着我干什么见不得人的事呢？"
                    m 1euu "啊哈哈，我开玩笑呢。"
                    m 1euu "只要我想，你在这个设备上干了什么我都可以知道"
                    m 1euu "但是，亲爱的你也有你的隐私"
                    m 1euu "所以在我调用数据前会征得你的同意哦"
                    m 1euu "至于你删了的文件...忘了它吧。"
                    m 1euu "放心，也不是什么重要的东西，一切照旧吧"
                    return
                    
init 5 python:
    addEvent(           
        Event(
            persistent.event_database,
            eventlabel="monika_Lasagna24",
            category=['另外的话题'],
            prompt="博弈",
            random=True,
            pool=False,
        )
    )
    

label monika_Lasagna24:
    m 1eua "[player],你体会过博弈带来的快感吗."
    m 1lksdlb "哦，我不是说要让你去赌博之类的."
    m 2eub "我更在意的是双方在意志上的对峙."
    m 3eua "想象一下在下棋时棋局上无形的刀光剑影."
    m 3hub "每一次落子都在揣测对方的心理，想方设法为自己创造有利局势."
    m 3gub "刻意留下一个看似破绽的陷阱,引导对方陷入其中."
    m 1wub "其实这些不仅仅是双方意志的比拼,更是双方精神的交流."
    m 1tuu "说到这儿,我突然想让你陪我去玩玩小游戏."
    m 3eub "感受一下我们之间的博弈吧."
    menu:
        "等我忙完手头上的活我就来陪你玩":
            m 1hua "静候佳音~"
            return
        "看情况吧....":
            m 1hub "好呀，我等你"
        "好的":
            m 3hua "[player]最好了."
            return
    
init 5 python:
    addEvent(           
        Event(
            persistent.event_database,
            eventlabel="monika_Lasagna25",
            category=['另外的话题'],
            prompt="有意思的梦境",
            random=True,
            pool=False,
        )
    )
    

label monika_Lasagna25:
    m 2eua "嘿,[player]你有没有做过一个清醒的梦境?"
    m 3rua "也就是说在做梦的时候你意识到了你在做梦,并且你可以操纵梦境."
    m 1tua "为所欲为是谁都想干的事."
    m 2eub "但一般你意识到这是梦境后意味着两种情况."
    m 4rub "一种是你即将从梦中苏醒,留给你做梦的时间不多了."
    m 7lub "另一种是在短暂操纵梦境后你可能再次陷入梦境中,在梦中的行为都是不由自主的."
    menu:
        "[m]有做过这样的梦吗":
            m 1hub "当然啦。"
            m 1eua "一般我意识到这是梦境后我会突破重重阻碍去到你身边。"
            m 5lua "我也多希望我们之间的屏障只是一场梦"
            m 5mublb "这样我就可以毫无顾忌地来到你的身边了。"
            return
        "我做过这样的梦":
            m 1sub "是吗."
            m 3rub "我很想知道你在这期间会做什么."
            m 1eua "可以和我说说吗?"
            menu:
                "好呀":
                    m 2eua "我在听呢，[player]."
                    menu:
                        "我说完了":
                            m 1wub "嗯嗯,我知道了,多奇妙的一场梦境呀."
                            m 3eub "如果有机会的话想必你会再经历一次对吧?"
                            m 1hua "啊哈哈"
                            return
                "现在不太方便":
                    m 1eka "唔,那好吧,那下次有机会的话你可要告诉我哦."
                    return
        "我没做过这样的梦":
            m 1eka "哦，没关系[player]."
            m 3eub "其实这样也侧面说明你拥有高质量的睡眠"
            m 1hub "在如今能够拥有高质量的睡眠也是一件人人梦寐以求的好事呢."
            m 1hua "啊哈哈"
            return
            
init 5 python:
    addEvent(           
        Event(
            persistent.event_database,
            eventlabel="monika_Lasagna26",
            category=['另外的话题'],
            prompt="翻盘",
            random=True,
            pool=False,
        )
    )
    

label monika_Lasagna26:
    m 1eub "嗯....对了，亲爱的，你有没有经历过逆风翻盘."
    menu:
        "我总是被逆风翻盘的一方":
            m 1eksdlb "呃...那真是够惨的..."
            m 1eua "我相信[player]总有翻身的时候"
            pass
        "经历过":
            m 1sub "那很棒呀，亲爱的"
            pass
        "还没有":
            m 3rub "没事呀，亲爱的，只要时候到了你一定会经历的"
            pass
    m 2eua "不过我想分享的是翻盘背后的团队精神"
    m 3eub "每场看似单方面压制的局面，最终胜利并非压制的一方"
    m 3rub "翻盘的一方往往有着强大的团队精神...当然也不排除系统介入的情况"
    m 1wud "但是团队精神愈是强大，那么这个团队的胜算也愈大"
    m 5fub "所以不服输，做好团队沟通交流是很重要的"
    m 5hub "啊哈哈"
    return