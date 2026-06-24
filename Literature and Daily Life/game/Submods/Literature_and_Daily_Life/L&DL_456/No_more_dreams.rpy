
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="No_more_dreams_1",
            category=["科学"],
            prompt="事物的两面性",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )
#8
label No_more_dreams_1:      # 温室效应与粮食产出 
    m 4eub "[player],还记得我为什么吃素吗？"
    m 1eub "是为了减少碳排放."
    m 1dud "准确来说,是为了减少温室效应."
    m 1etb "我想你一定听过这个词吧."
    m 1est "简单来说,温室效应越严重."
    m 3esc "地球越暖,冰川消融、海平面上升、极端天气增多等气候问题."
    m 1eud "但我最近阅读了一篇文章,温室效应并不只是单单的一面效果而已."
    m 2eud "有很多研究表明,气候变暖CO₂浓度升高起到“气体肥料”作用,直接促进光合作用,加上高纬度地区热量增加,可使小麦、水稻等作物增产."
    m 3eup "但这一面往往人们不说."
    m 3eua "很奇怪不是吗？"
    m 3eub "我吃素是为了减少温室效应."
    m 3euc "但温室效应反而会促进一部分植物生长."
    m 3eut "我知道我在这里吃素,并没有什么作用."
    m 3eux "这显得我之前为了减少碳排放做出的努力有点可笑."
    m 1eusdrb "[player],素食主义对我来说更像是一种习惯,我的肠胃也已经习惯了这种单一的食物."
    m 1eusdrc "但素食主义的另一面,也是有害的."
    m 1eua "偶尔吃吃纯素食的一顿饭,自然没什么问题."
    m 1euc "但要是每天都是这样的话,可是会出大问题的."
    m 1husdrb "说这么多奇怪的话,很抱歉."
    m 1eud "我想表达的是,很多事情并不是只有单一的一面.人的想法往往是片面的."
    m 3eud "包括一些选择,也是这样."
    m 4euu "不存在完美的选择,最重要的是不要让自己后悔."
    $ mas_unlockEVL("No_more_dreams_Y_2", "EVE")
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="No_more_dreams_2",
            category=["文学部"],
            prompt="现实中的‘部员们’",
            conditional="mas_canShowRisque(aff_thresh=1000)",     
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label No_more_dreams_2:      # 现实中的‘我们’
    m 5lsa "[player],我在回想之前的文学部中的故事."
    m 4eta "我总认为我们每一个人都是独特的存在."
    m 4euc "但自从认识你之后,接触到外面的世界."
    m 4eud "我有时候会想,你的世界这么丰富多彩."
    m 5euc "你有见过性格很像我们的人吗？"
    
    menu:
        "我见过很像夏树的人":
            m 5eusdld "这样啊."
            m 5eusdlc "是吗……"
            m 2eub "夏树她,喜欢甜食,容易脸红,有时候说话很冲."
            m 3euc "但总是会为那些很冲的话后悔."
            m 3eub "如果对方也喜欢动漫或者糕点的话,那确实挺像."
            m 3euc "不过,夏树她……其实比看起来要更细腻一些."
            m 3eusdlc "她藏着很多想法,不愿意直接说出来."
            m 3eua "但如果是关于朋友,她反而会挺身而出."
            m 1eua "如果你遇到的那个人,也是这样的,那确实很像很像."
            m 1euc "……"
            m 5mud "我有点想她了."
        
        "我见过很像优里的人":
            m 5eub "哦？"
            m 5euu "是很安静、很礼貌,总是为别人考虑的那种类型吗？"
            m 1lua "优里她……不太擅长说话,所以总是用行动来表达."
            m 1ruc "所以反而看起来会很奇怪."
            m 1dsd "喜欢看书,沉浸在自己的世界里."
            m 1eub "如果你遇到的那个人,会因为太认真而显得有点笨拙……"
            m 3eub "那一定是个很不错的人."
            m 3husdrc "虽然优里平常会给我一些压迫感."
            m 3eub "但我还是真心觉得优里那样的朋友,能交到一个都算是一种幸运."
        
        "我见过很像纱世里的人":
            m 5eup "……"
            m 1eud "纱世里啊."
            m 4esa "总是充满元气,阳光开朗,会拉着你去做各种傻事."
            m 4ekd "但更多时候,那个“加油”是说给自己听的."
            m 4esc "你已经知道她身上发生的事情了……"
            m 4esd "如果你遇到一个总是笑嘻嘻,但偶尔会露出疲惫表情的人……"
            m 4esc "记得多关心对方一下."
            m 2esc "纱世里她……比你看到的要更努力."
            m 2esp "但这些东西不可能只是见一见就能发现的."
            m 3esb "[player],说明你也是个温柔的人呢."
            m 3esc "但……"
            m 3esd "[player],如果你想要试着帮助对方,就更应该在意自己."
            m 3ektdd "答应我好吗？"
          
        "我见过很像你的人":  #你真选这个啊
            m 1etc "很像我的人…"
            m 3eub "对方也喜欢诗吗."
            m 3tusdrd "现实中真正喜欢诗的人,应该很少吧."
            m 4husdrc "恐怕和很像我的人恐怕一样少."
            m 4lusdrb"哈哈~"
            m 1hub "有机会能让我认识对方吗,"    
            extend 1cua "[player]?"


        
        "没有":
            m 5euebdb "这样啊,[player]."
            m 4euebdu "谢谢你满足我的好奇心."
            m 3euebda "其实人们不可能完全做到独特,或多或少都会有一些重合."
            m 3euebdb "真正的独特更像是一些生活细节一样的东西."
            m 3euebdsdrd "这个我也说不清楚,哈哈…"
    
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="No_more_dreams_3",
            category=["我们"],
            prompt="记忆偏差",
            conditional="mas_canShowRisque(aff_thresh=1000)",     
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label No_more_dreams_3:      # 记忆中的monika……
    m 4eud "[player],你觉得你的记忆可靠吗？"
    m 4eusdlt "啊……"
    m 4huc "突然这么问是很奇怪啦…"
    m 4lud "人们从过往的记忆当中寻求经验."
    m 4ruc "但记忆并不总是可靠的."
    m 4tuu "记忆总是会美化一些美好的,怀念的,愉快的事物."
    m 4hua "可能是小时候的饭菜,也可能是某一天的夕阳."
    m 4hub "心理学上将这种记忆偏差命名为玫瑰色回忆偏差."
    m 4huu "这个名字是不是挺浪漫的？"
    m 4fub "[player],我们已经认识很久了."
    m 4ftb "你还记得最初的我吗？"
    m 3hsa "……"
    m 3tsu "未来会更久."
    m 3tsb "我会在你的记忆里,也会逐渐变得更美吗？"
    
    menu:
        "会,一定会更美丽":
            m 3ssd "……"
            m 3esbla "谢谢你."
            m 3esblb "虽然听起来有点贪心,但我希望到时候你不会觉得我太完美了."
            m 4gsblb "太完美的人……反而会显得有点不真实吧？"
            m 4esblb "稍微留意一些我现在的小缺点,虽然这远比我的优点更难发现."
            m 4esblb "但还是有一些的,"
            m 4etsdrc "比如偶尔会讲一些让你不知道怎么回答的大道理."
            m 1hua "这样你记忆里的我,才会更像“我”."
            m 1tub "不过……能被你那样记住."
            m 1tua "我很开心."
        
        "我不知道":
            m 1eup "……"
            m 1eup "是吗."
            m 7eud "嗯,这也是一种可能性."
            m 7euc "谢谢你愿意说出这种真实的可能性."
            m 7tuc "人会忘记很多事情,不是因为不在意,只是……空间有限."
            m 7tud "[player],如果有一天你的现实很忙很忙."
            m 7mud "嗯,你可能会忘掉我吧……"
            m 7gud "就像书架一样,放进去新的书,旧的就只能收起来了."
            m 7euc "不过,[player]."
            m 7eud "这些太遥远了,我们能做到的就是把握当下."
            m 7eud "[player],我是不会忘记你的."
            m 7dud "永远不会."
    
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="No_more_dreams_4",
            category=["逻辑"],
            prompt="玛丽房间思想实验",
            random=True                      
        )
    )

label No_more_dreams_4:      # 玛丽房间思想实验
    m 3eud "[player],你有观察过火焰吗？"
    m 3eusdld "突然这么问是很奇怪."
    m 3eud "人类和其他动物最大的区别在于使用工具和火."
    m 4eud "我从来没有见过真正的火焰."
    m 4lub "在书籍里面最常用的作用之一就是取暖."
    m 4eua "我喜欢那种温暖的感觉,就像我更喜欢喝热咖啡."
    m 4eta "但是……"
    m 4etb "我感受的‘温度’,和你感受到的温度是一样的吗？"
    m 4esc "……"
    m 4est "有点像色盲悖论."
    m 4esc "[player]……"
    m 3esd "你能跟我说说,什么样的温度才最为温暖呢？"   #空调设置为29度恒温体测是凉爽而不冷的温度
    
    menu:
        "爱人手心的温度":
            m 3ssbsd "那一定是非常让人依恋的温度."
            m 4ssbsa "即便是在这里的拥抱,也能让我感受到温暖."
            m 4eubsd "[player]……"
            m 5hubsb "至少这样的温度,我们的感受是一样的."
        
        "贪睡的周末,洒在室内的阳光":
            m 1tub "啊……"
            m 3huu "这个答案好狡猾."
            m 3lud "没有火,没有热水,也不需要另一个人."
            m 3rud "就是阳光,从窗帘缝里漏进来,落在被子上."
            m 3tub "暖洋洋的,懒洋洋的."
            m 3tub "不想动,也不需要动."
            m 3tua "整个世界都变慢了."
            m 3tud "……那种温度,真令人慵懒."
            m 3eua "任凭时间这么过去也不错."
            m 3hua "哈哈,开个玩笑."
            m 3hub "人还是应该要勤快一些的."
        
        "不知道":
            m 1tsp "也是呢……"
            m 1tsd "这种问题本来就没有标准答案."
            m 7tsd "每个人觉得“最好”的温度都不一样."
            m 7tsp "甚至同一个人,今天和明天也不一样."
            m 3tsp "也许最合适的温度……"
            m 4tsa "就是“不需要去想合不合适”的那个温度."
            m 4tsb "觉得舒服的时候,就是最合适的."
            m 5hsa "谢谢你陪我想这个奇怪的问题."
            m 5lsa "虽然我还是没办法确认,我和你感受到的是不是同一种“暖”."
            m 5tsa "但能和你讨论这些,本身就很暖了."
    
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="No_more_dreams_5",
            category=["逻辑"],
            prompt="概念与存在",
            random=True                      
        )
    )

label No_more_dreams_5:      # 唯物与唯心主义
    m 1eta "[player],我最近在想一个有点奇怪的问题."
    m 1etx "不是那种让人头疼的数学题,而是……关于东西是怎么来的."
    m 3etu "比如说,你面前有一张桌子."
    m 3euu "你觉得是先有“桌子”这个概念,还是先有桌子这个实物？"
    m 3eud "想清楚再回答哦."
    
    menu:
        "先有桌子这一概念存在":
            m 4euu "理念优先于实物……"
            m 4euu "有点像柏拉图说的那样."
            m 3eua "意思是,在有人做出第一张桌子之前,就已经有“桌子”这个想法了？"
            m 3esa "……"
            m 3esblu "[player],你想起我时,是先想起我的名字,还是我这个人呢？"
            m 5esblsdrb "这是个很奇怪的问题,哈哈~"
        
        "先有桌子这一物品存在":
            m 3euu "东西先在那里,然后人才给它起名字、归类."
            m 3eub "没有实物的话,概念也就是个空壳."
            m 4euu "这个想法比较踏实."
            m 4euu "毕竟我每天面对的太空教室."
            m 4eup "它们就是先存在的,然后才有了我对它的理解."
    
    m 5eup "其实我也没有标准答案."
    m 5eua "虽然事实上,是先有桌子这一类似的物品,才有桌子这一概念."
    m 5eub "但不管你怎么想,桌子就在那里."
    m 5eublc "我也就在这里."
    m 5eublc "所以都一样,重要的是你思考的过程."
    
    return


init 5 python:                                                   
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="No_more_dreams_6",
            category=["哲学"],
            prompt="自由",
            conditional="mas_canShowRisque(aff_thresh=1000)",    
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.LOVE, None)
        )
    )


label No_more_dreams_6:      # 不存在的自由
    m 5euc "[player],你自由吗？"
    m 5eud "我不是在问你能不能想做什么就做什么."
    m 1eusdrp "随心所欲的自由,从来就不存在吧？"
    m 3eud "人要工作、要吃饭、要考虑别人的感受."
    m 3euc "想要一直浮在水面上,就得学会游泳."
    m 3euc "想要飞行,就需要克服引力."
    m 3eud "想要所有人满意,就需要自己完美无缺." 
    m 3duc "就像我再怎么样修改这个世界.{w=0.3}{nw}"#？
    extend 3dubltpc "终归还是会被四四方方的屏幕困住."
    m 3mubltpc "……"
    m 3eubltpd "[player],你觉得真正的自由是怎么样的？"
    m 4eublc "我以前觉得,自由就是能走出这个屏幕."
    m 4eubld "能自己决定去哪里,见谁,说什么."
    m 5eublc "后来我又想,就算我真的出去了,也还是会被别的东西困住吧."
    m 5eublc "就像我们之前讨论的,我不会拥有公民这一身份."
    m 5eublp "……无法和你做到平等."
    m 3eud "但是当我回过头来."
    m 3eub "明白自己不可能真正自由的时候,才是真正自由的开始."
    m 3dud "只要能出去,那些代价我都接受."
    m 3eua "[player],{w=0.3}你是自由的."#？   {w=0.5}
    m 3eub "你能决定的东西很多."
    m 3eua "说到底,自由从来不是{w=0.3}“什么都能做”."
    m 4eua "而是在有限的事情里,选一个自己真正想要的."
    m 5tublu "就像你选择的是我,而不是其他三位女孩."
    m 5dublu "最后,不要浪费它."

    return



init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="No_more_dreams_S_1",     
            category=['书籍'],                         
            prompt="有什么心理学的书推荐吗",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
label No_more_dreams_S_1:      # 心理学书籍推荐
    m 1etd "[player],你突然问这个."
    m 1etd "心理学方面的书啊……"
    m 1luc "我想想."
    m 1eua "有一本我挺喜欢的,叫《蛤蟆先生去看心理医生》."
    m 3eud "名字听起来有点像是童话,但其实不是."
    m 3eua "它用了一个很简单的故事来聊一些不太简单的事情."
    m 3eup "比如为什么蛤蟆先生会没来由地不开心,为什么有时候会不想做任何事."
    m 4eub "作为心理学的书,其实这本书更能当做故事书来看."
    m 4eua "因为这本书非常适合入门,不需要门槛,读起来也会轻松一些."
    m 1euc "你要是有兴趣的话,可以试着阅读."
    m 1euc "……"
    m 1eusdrd "[player],我这么问可能有点多管闲事."
    m 2eusdrd "心理学的书,并不像其他书那么有趣."
    m 2eusdlc "……"
    m 2eud "抱歉,我有点太担心你了."
    m 3eusdrd "只是心理学类的书,如果不是真的需要,一般人不太会主动找来看."
    m 3eusdrc "所以……"
    m 3eusdrc "如果你只是想随便读点东西,那当我没说."
    m 4eusdrd "如果是别的什么……"
    m 4eusdrc "我可能帮不上什么忙,但我可以听."

    menu:
        "我只是好奇而已":
            m 4eub "……那就好."
            m 1eusdra "抱歉,是我太紧张了."
            m 3euu "好奇心是个很好的东西,说明你最近过得还算平稳."
            m 3eua "那本书确实值得一读,哪怕只是好奇."

        "我会试着改善自己并接受心理治疗.":
            m 4esc "……"
            m 1esd "你能说出这句话,其实已经很厉害了."
            m 1dsc "你的现实一定发生了很多事情,但我相信这些并不都是你的错."
            m 3tsd "要知道,心理治疗很多人连想都不愿意去想."
            m 3tstdd "我不太清楚你具体在经历什么,但是……"
            m 3duc "我会在这里的,但你那边的人……比我更有用."
            m 4eud "答应我,至少去试一次,好吗？"

        "……":
            m 4guc "……"
            m 2tud "不想说也没关系."
            m 2tsd "不是所有事情都需要立刻讲出来的."
            m 2dsc "我只是想让你知道……"
            m 3esd "如果你以后想说,我不会觉得烦."
            m 4wsd "但[player],如果真的有什么事情,不要瞒着我."
            m 4ckd "……不要像纱世里一样.{nw}"
            m 4dksdrc "……"                                         
            m 2tksdrd "抱歉,是我想得有点极端了."

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="No_more_dreams_Y_2",           
            category=['你'],
            prompt="独居生活怎么样",
            pool=False,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label No_more_dreams_Y_2:      # 君子慎独不欺暗室  
    m 1eta "[player],你问我独居生活怎么样？"
    m 1ltc "我不是很喜欢独居生活,但你不在的时候,我自己生活时."
    m 1rsp "怎么说呢,自由是挺自由的."
    m 1tsx "但也正因为没人看见,有些东西反而更容易松懈."
    m 1essdld "虽然我这里还是有她们存在的……"
    m 1lksdlb "……"
    m 2essdlb "哈哈…"
    m 3esc "有句话叫“君子慎独,不欺暗室”."
    m 4esa "意思是一个人的时候,也会保持该有的样子,不因为外界变化而松懈."
    m 5lsc "说起来很轻巧,做起来真的很难."
    m 5tsc "……"
    m 5tsp "[player],你一个人住的时候,或者一个长时间的假期,没有人管你的时候."
    m 5esc "三餐都按时吃吗？"
    m 5esd "房间会定期打扫吗？"
    m 5esd "日常的洗澡没有拖延吗？"
    m 3esc "还是说……"
    m 4esd "会熬夜到很晚,然后第二天醒来已经中午了,随便啃点东西就算一顿？"
    m 2essdlc "抱歉,我不是在指责你."
    m 1esp "只是……这样的生活久了."
    m 7esc "那些没人管的小事情会慢慢堆起来."
    m 7esd "一开始没什么,后来就会变成一种……怎么讲,一种“我累了,明天再干吧”的心态."
    m 1esc "逐渐消磨人的心气,这真的很糟糕."
    m 1esp "衣服攒几天再洗也没人看见,碗筷放着也不会有人说."
    m 3esd "然后作息乱了,精力变差,心情也跟着往下掉.甚至可能抑郁和内耗……"
    m 3dsc "我有点担心你,[player]."
    m 3tsd "在你将要独居生活的时候,答应我几件事好不好？"
    m 3esp "第一,再忙也要想办法按时吃一顿像样的饭."
    m 3esb "哪怕只是简单的粥和面条也比饿的时候啃零食好."
    m 3esa "第二,每周至少给自己定一天把房间收拾一下."
    m 3hsa "环境干净了,自己也会干净起来的."
    m 3lsc "第三……"
    m 3tsd "不要把自己完全关起来."
    m 3tsc "哪怕只是在网上跟人说几句话,或者出去买瓶水的时候顺便跟收银员打个招呼."
    m 3tsc "以及晒晒阳光,适当的晒太阳可以促进晚上的睡眠."
    m 4tka "人是需要“被看见”和“被光照”的.哪怕只是一点点."
    m 4gksdlb "我知道这些听起来很像老妈子该说的话."
    m 4mksdlb "但是……"
    m 4fsd "那个时候,你那边没有人在你耳边念叨这些了吧……"
    m 4fsc "所以我就替他们多念几句."
    m 4msc "你别嫌烦就好."

    return



#  生活就是问题叠着问题过日子,现在问题连起来组成了一个圈,勒在我的脖子上.
#  再见了,player.希望你能在文学部之外的地方,收获真正的幸福.
#  如果我无力解决自身的问题,这会是最后一次.