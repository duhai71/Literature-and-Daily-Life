init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_sleepdeprivation_reload",
            prompt="熬夜的危害",
            category=["健康"],
            random=True
        )
    )
#2个
label mshMod_topic_sleepdeprivation_reload:
    m 1esc "[player],最近你经常熬夜吗？"
    menu:
        "是的":
            jump mshMod_topic_sleepdeprivation_reload_yes
        "没有":
            jump mshMod_topic_sleepdeprivation_reload_no
label mshMod_topic_sleepdeprivation_reload_no:
    m 1hua "对我来说真是个好消息."         
    m 2esd "毕竟睡眠不足会让大脑清除代谢废物的效率降低{w=0.3}"
    extend 2wud "就像垃圾堆在房间里发臭一样呢！"
    m 3rsc "阿尔茨海默病的风险会增加,免疫力也会下降..."
    m 4euc "上周我读到研究说,连续三天熬夜就会让认知能力倒退十年！"
    m 2esd "更别说黑眼圈越来越深的样子..."
    m 5ekbsa "今后在没有必要事情的情况下也要早睡早起哦."
    m 5hkbfb "毕竟我可不想看到你挂着熊猫眼迎接我呀~"
    return
label mshMod_topic_sleepdeprivation_reload_yes:
    m 1wubld "这不太好呢......"
    m 2esd "毕竟睡眠不足会让大脑清除代谢废物的效率降低{w=0.3}"
    extend 2wud "就像垃圾堆在房间里发臭一样呢！"
    m 3rsc "阿尔茨海默病的风险会增加,免疫力也会下降..."
    m 4euc "上周我读到研究说,连续三天熬夜就会让认知能力倒退十年！"
    m 2esd "更别说黑眼圈越来越深的样子..."
    m 5ekbsa "今后在没有必要事情的情况下也要早睡早起哦."
    m 5hkbfb "毕竟我可不想看到你挂着熊猫眼迎接我呀~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_nightmood_reload",
            prompt="熬夜的情绪影响",
            category=["健康"],
            random=True
        )
    )

label mshMod_topic_nightmood_reload:
    m 1ekc "[player],你听说过睡眠债吗？"
    m 3esd "也就是每次熬夜都在透支未来的情绪稳定性{w=0.3}"
    extend 3rsc "致使杏仁核会变得过度敏感..."
    m 2eud "比如说,明明是小事情,却容易生气或流泪..."
    m 3euc "这对于我们的生活都是不利的."
    m 5fua "所以,我希望你能定个闹钟,提醒自己该睡了."
    m 5hkbfb "毕竟我想看到的,是一个健健康康的、{w=0.6}可可爱爱的[player]呢."
    return





