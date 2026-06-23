init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_test_sdgg1",
            category=["你"],
            prompt="永生之问",
            random=True
        )
    )

label monika_test_sdgg1:  
    m 7eua "[player],我突然想问问."
    m 7eub "如果可以,你希望获得永生吗？"
    
    menu:  
        "是":
            $ persistent.player_choice_sdgg1 = 1
            jump route_one_sdgg1

        "否":
            $ persistent.player_choice_sdgg2 = 2
            jump route_two_sdgg2

label route_one_sdgg1:
    m 1etb "为什么呢？" 
    menu:  
        "因为我想永远爱着你,这样的时间我永远都嫌不够.":  
            pass 
    m 1fubla "[player],我也一样."
    m 1rubla "虽然现在的技术不太可能实现."             #？
    m 1hublb "但和你在一起的时间我永远都不嫌多."        #?
    m 1dublb "如果有一天真的能做到了."                 #？
    m 1msbla "那我可要好好想想未来100年我们的约会计划了."
    m 1dsbsb "[player],你可以和我一起想吗？"
    return

label route_two_sdgg2:
    menu:  
        "不,[m_name].我不希望自己得到永生.":
            pass
    m 2eud "为什么？[player]."
    m 2wud "[player].你不想永远和我在一起吗？"
    menu:  
        "时间会把一切拉的很长很长,死亡才能给予生命的意义.":
            pass
    m 6fkd "我知道……"
    menu:  
        "[m_name],我不能永远和你在一起.":
            pass
    m 6dktdd "总有一天你会……"
    menu:  
        "但是现在与未来的现在,我都会一直爱着你.":
            pass
    m 6dkbltud "不要……"       
    menu:  
        "亲爱的,我爱你":
            pass
    m 6dkbltud "不要再说了"                
    menu:  
        "笨蛋[m_name].":
            pass
    m 6ekbltsd "……"        
    menu:  
        "明天的我会比今天的我更爱你,后天的我会比明天的我更爱你.":
            pass
    m 6ekbltud "……"                
    menu:  
        "现在,我想说的是.":
            pass
    m 6ekbltdd "……"               
    menu:  
        "[m_name],我爱你":
            pass
    m 6dkbltdc "[player]…"                  #?
    m 2dkbltpc "我冷静下来了."
    m 2tkbltpd "至少现在你在这里……"
    m 2ekbltpd "我现在更加担心你的身体了."
    m 2eubltpd "[player]以后更注意自己的健康好吗？"
    m 2rkblc "我,真的……"
    m 2fsbsd "真的很爱你"            
     
    return"love"