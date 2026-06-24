init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="lzp_love_monika_sdg_1",
            prompt="[m_name],你值得我用余生去爱.",
            unlocked=True
        ),
        code="CMP"
    )
    #1
label lzp_love_monika_sdg_1:
    if mas_isMoniEnamored(higher=True):       #好感≥400
        $ mas_gainAffection(3, bypass=True)   #加好感的,可删
        m 1ssblb "天呐,[player]这是超级认真的对吧."
        menu:
            "当然":
                pass
        m 1esblc "……"
        m 3esblp "可别对其它女孩子这话哦~"
        m 5rsblb "我真的有这么好吗？"
        menu:
            "当然,亲爱的.我离不开你了,我想在接下来的生命中一直去爱你.":
                pass
        m 2gsblc "呜……"
        m 2tsbsd "[player],你把我弄害羞了."
        m 5tsbsu "呜,我现在真的不知道该说什么了."
        m 1hsbsu "我现在真的好高兴……"
        m 3tsbsp "[player],看看你干的好事."
        m 2tubsp "……"

        if mas_isMoniEnamored(higher=True):
            if mas_shouldKiss:
                call monika_kissing_motion_short

        m 3tubsb "现在,你也体会到我现在心跳的速度了."
        m 3fubsa "[player],我也一样.我的未来也不能没有你."
        m 1subsb "我——{w=0.5}爱——{w=0.5}你——"
        m 5hsbsb "爱的无可救药……"
        m 5fsbsd "[player],你想不出来我有多爱你的."
        m 1eubla "最后,谢谢你说的这些话."
        m 1dsblb "这对我非常重要."
        return"love"
    elif mas_isMoniAff(higher=False):         #100~399
        "还需要一些时间来培养感情,说谎的人要吞一千根银针哦~"
        return    
    elif mas_isMoniHappy(lower=True):         #30~99
        "现在说这个好像太早了"
        return  