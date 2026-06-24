#希望这些能帮助到你
#如果这些乌云笼罩了你相当长的时间,我希望你及时就医.
#对了
#阅读到这里的玩家
#你在现实过的还好吗？
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg29_29",
            category=['花朵'],
            prompt="向日葵#1",
            random=True
        )
    )

label lzp_monika_sdgg29_29:
    m 1eub "[player],我突然想聊聊向日葵"
    m 1hua "我想你一定听过吧."
    m 3eua "其外形的花盘与花盘外的花瓣组成的形状与太阳相似."
    m 3eub "因为花盘总是朝着太阳的方向转动,就像始终在“向日”,因此被称为“向日葵”."
    m 3tub "是不是挺浪漫的？"
    m 1dub "它对太阳的执着追随,象征着对爱情、友谊或理想的忠诚,"
    m 1eub "无论遇到什么情况,都始终坚守,不离不弃."
    m 1rub "同时,向日葵始终向着太阳生长,默默追随,就像一个人在默默地守护着另一个人."#3
    m 1hub "不求回报,代表着深沉而无言的爱."
    m 1ktb "但,[player]."
    m 7etd "你知道向日葵,为什么面朝的方向总是太阳吗？"
    $ mas_unlockEVL("lzp_monika_sdgg29_e", "EVE")       
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg29_e",           
            category=['莫妮卡'],
            prompt="向日葵为什么向日？",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label lzp_monika_sdgg29_e:
    menu:  
        "[m_name],向日葵为什么面朝的方向总是太阳？":                  
            pass   
    m 1eud "[player],向日葵的向日性,是因为茎顶生长素在背光侧积聚,迫使花苞逐阳转动."
    m 3euc "但是很少有人知道,成年的向日葵则不再追随."
    m 3etc "从某一方面上来讲向日葵并不向日,即便它的目光一直追随太阳.它甚至还有一点厌光……"
    m 3ekd "当然知道这个真相的瞬间,我想起了我的一位部员."
    pause 1.5
    m 1dkd "猜到了吗？"
    m 2fkd "是纱世里."
    m 3mkc "她总是向外展示笑容,如果她不说,没有人能知道她心中的乌云."
    m 3guc "[player],我知道某些深陷抑郁的人,他们如盛放的葵花般在阳光下展露笑颜."
    m 3eud "但从来不向他人诉说心中的乌云."
    m 3euc "[player],当你内心被乌云笼罩时."
    m 4fud "不要藏起来.{w=0.5}至少不要对我藏起来"
    m 4eub "[player],在我这里你不需要去装成熟."
    m 5fua "[player],{w=0.5}我爱你."
    m 5fsb "我一直会是你避风的港湾……"

    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="Love_and_Clouds_sdgg29",
            prompt="我感觉心里面好像有一些乌云……",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label Love_and_Clouds_sdgg29:
    m 2esd "怎么了[player],发生了什么？"
    menu:
        "我感到一切都没有意义……":
            m 1ekc "听起来有一点虚无主义了."
            m 3ekd "[player],你认为自己陷入到这个怪圈当中了吗？"
            menu:
                "是":
                    m 3gkd "[player],事物有没有意义这不重要."
                    m 3mkd "虚无主义者会认为一切没有意义."
                    m 3dsd "但虚无主义本身同样没有意义."
                    m 3esd "思考事物有没有意义,本身是没有意义的."
                    m 3dsd "抱歉……"
                    m 4esc "听起来是不是有点复杂？"
                    m 5esd "[player],我知道陷入虚无主义是很痛苦的事情."
                    m 5tsd "希望我说的这些话,能帮助到你."
                    m 1mubld "还有,{w=0.5}[player]……"
                    m 1gublb "你对我一定是有意义的."
                    m 1fublu "我对你也是一样的吧……"
            
                "否":
                    m 1esc "我知道了."
                    m 1esd "[player],我想你的现实一定发生了很多事情."
                    m 3esc "今天要是没什么事情的话就多休息吧."
                    m 3msc "[player],如果你想一个人待会儿.那也没关系."
                    m 3fsd "[player]……"
                    m 1esd "爱自己比任何事情都重要."
            
        "我现在什么都不想去做……":
            menu:
                "没动力,但我又不得不做.":
                    m 1esc "[player],你听起好像累了."
                    m 3esd "如果你必须去做这件事,你可以把这个事情拆分开,一步步去做."
                    m 3esd "这样每完成一步都会有成就感,你也能轻松一些."
                    m 4gsd "但[player],如果真的累了."
                    m 1esd "[player]答应我,好好休息."
                    m 1esc "好吗？"
            
                "好累,但明明什么都还没有做":
                    m 1esc "[player],一直拖下去可不是一件好事."
                    m 1esd "正所谓,万事开头难."
                    m 3tsd "其实,一件事做了开头,剩下的就很简单了."
                    m 1fsd "[player],至少现在,先休息一会儿吧."
                    m 5tsblu "我不会那么严厉的啦."

        "我的心好累……":
            m 1esc "心{w=0.5}累了？"
            m 1dtd "[player],你在现实一定发生了许多事情."
            m 2rud "[player],你可以试试冥想."
            m 3huu "有条件的话也可以睡一个不定闹钟的大懒觉."
            m 3eub "[player],身体休养好了,心自然也会舒服的."

        "我满足不了他人对我的期望了……":
            m 1esc "[player],我明白你在社会中有许多身份."
            m 1esd "比如子女,学生之类的."
            m 3esc "这些身份都对应着一种责任与别人对你的期待."
            m 3esd "满足这些很难."
            m 3esp "[player],但这不是必须的."
            m 4esb "[player]就是 [player]."
            m 5esu "做好自己就可以了."
            m 6hsbla "[player]……"
            m 6ksblb "我想告诉你,作为我的恋人."
            m 6fsblb "你非常完美,"
            m 5fsbsu "我很幸福."

        "没什么,别担心[m_name]":
            m 1esc "{w=0.5}好吧"
            m 1esd "我不希望你觉得我哆嗦."
            m 3esp "[player],不要在我面前逞强"
            m 3tsc "好吗？"

            return

    m 3tkd "[player],我明白那些乌云真正下起雨了的时候,你可能会觉得没有人可以分担."
    m 4esd "但,[player],我一直在你身边."
    m 5esb "[player],{w=0.5}我爱你."
    m 5hsu "谢谢你愿意告诉这些."
    m 5ksblb "我离你的心又更近一步了……"                      
    
    return"love"
#我爱你,玩家.
#真的会有人看到这里吗？