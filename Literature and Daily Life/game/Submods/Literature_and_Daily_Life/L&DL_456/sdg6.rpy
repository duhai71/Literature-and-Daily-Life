init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg6",     
            category=['扮演'],                         
            prompt="恋爱中被依赖的一方",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg6:                       
    m 1eub "哦,[player]~"
    m 1wsb "你是想向我撒娇吗？"
    m 1ssb "真可爱啊,我怎么可能拒绝."
    menu:  
        "我一直想让你帮我清理耳朵":
            $ persistent.player_choice = 1
            jump route_one_sdg6_1

        "可以夸我一下吗":
            $ persistent.player_choice = 2
            jump route_two_sdg6_2

        "告诉我[m_name].你最爱谁？":
            $ persistent.player_choice = 2
            jump route_Three_sdg6_3

label route_one_sdg6_1:
    m 1dssdlc "唔…"
    m 1hssdld "这个好像只能等到我“出来”之后才能帮你了."
    m 1gsblu "如果可以的话,我真想摸摸你的耳朵啊."
    m 1esblu "在这之前还是只能靠你自己了."
    m 1tsblb "也许未来我会让你枕在我的腿上帮你…"
    m 1tsblb "…"
    m 1tsblu "……"
    m 1hsblu "别害羞[player]."
    m 1hsbla "嗯哼~"

    return

label route_two_sdg6_2:
    m 1eub "当然"
    menu:
        "嘿嘿~":
            $ random_choice = renpy.random.randint(1,3)
            
            if random_choice == 1:
                m 1tublb "[player],你的眼睛."
                m 3sublb "对我而言,比星海更深."               
            elif random_choice == 2:
                m 1tublu "[player],{w=0.5}住在我的心房里."
                m 3tubla "我是不会收房租的~"
            else:
                m 1tublb "[player],你就是我的完美另一半."
                m 4tubla "我们就是天生的一对！"
    
    m 1hubla "[player],无论你过的怎么样."
    m 1eublb "你都可以来找我,我想成为你的依赖."
    m 3eublb "我想成为你心中的一股力量."
    m 5hublu "我永远会支持你."    
    return 

label route_Three_sdg6_3:
    m 1mublb "哈哈~"
    m 1dublb "我想这个我们都知道."
    m 4dublb "当然是..."
    m 4eublo "[player],{w=0.5}[player],{w=0.5}{b}[player]{/b}！"
   
    return 