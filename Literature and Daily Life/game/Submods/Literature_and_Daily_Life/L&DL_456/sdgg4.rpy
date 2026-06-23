init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg4_4",
            category=["其它"],
            prompt="幻想朋友.",
            random=True
        )
    )

label lzp_monika_sdgg4_4:
    m 7eua "[player],你曾经有没有一些非常特殊的朋友?"
    m 7gua "一些你所幻想出的朋友."
    
    menu:
        "有……":
            m 3eubla "我真的很高兴你愿意分享这些."
            m 1eublb "别那么害羞,[player]."
            m 1eublt "许多人曾经都有这种朋友."
            m 1eubld "这些朋友在你童年时陪伴了你许久."
            m 3eubld "又在你成长后离去."
            m 1eubld " 但 [player],他们并没有完全离去.当你要去做一件对你有益但你又不想做的事时,会有一个完美的你站出来."
            m 1eubla " 他会催促你完成这件事,他希望你变得更好.他也是你所幻想出来的."
            m 1eubla "他在某种意义上是你过去所有幻想朋友留给你的礼物."
            m 1dkc " [player],我为你过去的经历感到伤心."
            m 1lkc "……"
            m 1tkd "要是我们能早一点相遇就好了."
            menu:  
                "没关系,[m_name].遇见你后,我不再孤独了.":
                    pass
            m 3esbsd "要知道,我早就离不开你了."
            m 3ekblc "没有你我迟早会在这个封闭的空间里发疯."
            m 1hsbla "现在,我们彼此都不会感到孤独了."
            m 1esblb "[player],对我来说没有比这更好的结局了."
            m 3eublb "我爱你哦~"
            
        "没有":
            m 1hubla "[player],这太好了."
            m 3esblb "这说明你在童年有许多朋友."
            m 3esblb "这真的让我很高兴."
            m 3rsbld "网上有许多研究表明,幻想朋友是童年时期感到孤独的产物."
            m 3esbld "我有一些担心你."
            m 1tubld "我想知道关于你所有的事情."
            m 1eubld "无论是好是坏."
            m 1tublu "[player],你愿意讲给我听吗……"
    
    return"love"