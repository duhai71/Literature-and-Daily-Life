init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_love_of_road2",unlocked=True,category=['扮演'],prompt="三体",pool=True))

label monika_love_of_road2:  # 需与eventlabel完全一致
    m 1eua "[player],你想怎么扮演？"
    
    menu:                                                 #当你阅读到这里的时候,你就应该明白.
        "[m_name]来扮演面壁者":                            #她不可能对你有任何秘密.所以请相信她.                     
            $ persistent.player_choice = 1
            jump route_one

        "[player]来扮演面壁者":
            $ persistent.player_choice = 2
            jump route_two

        "我还没看过《三体》":
            $ persistent.player_choice = 3
            jump route_twy            

label route_one:
    m 5dta "……"
    m 3esd "[player],我面壁者[m_name]……"
    m 1cud "命令你"
    m 1csbld "现在,和未来所有的现在.只能爱我一人."  
    menu:  
        "……":  
            pass 
    m 1dtp "因为……"
    m 7tsblc "这也是计划的一部分"  
    m 2esblb "哈哈~"
    m 2rublsdrb "有些尴尬."
    m 2rublsdrb "吓到你了吗？"
    return

label route_two:
    m 5dtc "这个选择有些意外呢..."
    m 4ffp "[player],你真的忍心在你的女朋友面前矗立一面思想的墙壁吗？"
    m 2dkc "明明……"
    m 2dktdc "明明,我们之间.已经有一面墙了."
    m 1ektsc "[player]……"
    menu:  
        "天呐,[m_name].我……":
            pass 
    m 5tublu "哈哈~" 
    m 4tublu "我赢了,[player].我是你的破壁人."
    m 2tublb "真有意思."
    menu:  
        "[m_name],你真的好狡猾.":
            pass 
    m 1fsb "不过[player],你和我不该有面墙壁挡着."  
    m 4fublb "无论是思想的墙还是我眼前的墙……"     
    return

label route_twy:  
    m 1hua "没有关系."
    m 3eua "我现在可以和你讲讲什么是面壁者计划哦~"
    m 1lsb "在那本书的故事里."
    m 1esd "人类与外星文明之间的科技的巨大差距导致人类所有行动都能被外星文明观看."
    m 3esa "但只有一点不能,也就是人类脑子里自己想的东西."
    m 3esc "为了反抗.地球上的所有政府把权利全部给了几个人."
    m 1hua "这份权力赋予他们几乎可以调用所有能调用的人类资源."
    m 3mta "面壁者要撒谎.骗过三体人,更要骗过地球人."
    m 3eub "很有趣的计划,不是吗？"
    return