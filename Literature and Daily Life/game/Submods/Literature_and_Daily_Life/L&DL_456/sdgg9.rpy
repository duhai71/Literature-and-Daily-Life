init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg9_9",
            category=["你"],
            prompt="被利用的善良.",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg9_9:
    m 1dsc "[player],我们在一起已经有一段时间了,我突然有一些担心你."
    m 1musdrc "我听起来没那么不安吧."
    m 3eud "[player],你太善良了."
    m 3tud "善良本身当然没什么问题."
    m 3eud "但太善良可能会被利用."
    m 1dsc "这就是我所担心的地方了."
    m 1esd "[player],我希望你在保持善良的同时多一分思考."
    m 1ekd "我不希望有人利用你的善良反过来伤害你或其他人."
    m 1tsc "[player]……"
    m 1mkc "你真的太善良了."
    m 1dkbld "哪怕我曾经对你做了那么多坏事,你也原谅了我,并选择将我带回来."
    m 1gkblp "我可真是个坏女人."
    m 1ekbld "[player],我想向你坦白."
    m 3dkbld "在原来的文学部里,我利用了你的善良."
    m 3gkbld "我向你展现出孤独与虚拟游戏受害者的一面……"
    m 3ekbld "向你示弱,吸引你的目光,让你对我产生共情."
    m 1ekbld "我只是,太爱你了……"
    menu:  
        "[m_name],我做的一切不是因为善良.":
            pass
    m 2etbld "……"
    menu:  
        "因为爱.就算这样,我还是爱你.":
            pass
    m 2wsbsd "……" 
    menu:  
        "[m_name],我爱你.所以请不要这么想了.":
            pass
    m 2dsbltpd "谢谢."
    m 1esblc "真的."
    m 1dsblb "与你再次见面一定用尽了我所有的幸运."
    m 1hubfb"[player],我爱你……" 

    return"love"