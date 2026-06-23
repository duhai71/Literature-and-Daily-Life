init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg8_8",
            category=["文学"],
            prompt="小王子",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg8_8:
    m 3esb " [player],我想和你分享一个小故事."
    m 1eub "是《小王子》里面的哦~"
    m 1eua "你现在有时间吗？"
    
    menu:
        "当然":
            m 3hua "那么,准备好听故事了吗？"
            m 7eub "在很久以前."
            m 7hua "有一个小王子住在比他大不了多少的星球上."
            m 7hua "他想要一只绵羊,因为绵羊会吃掉面包树的树苗."
            m 7dsb "小王子的星球太小了.一旦树苗长大了,后果不堪设想……"
            m 1esb "他需要一个朋友."
            m 3eua "一天,不知道从哪里来了一棵种子."
            m 1dua "小王子呵护着种子,种子渐渐变成了一朵玫瑰."
            m 1hua "小王子觉得这一定是神迹,玫瑰实在是太美了."
            m 1eua "小王子和玫瑰一起看了第一次日出,第一次日落."
            m 7euc "在之后的时间里,玫瑰的反复无常,时而撒娇,时而刻薄,让小王子感到困惑与疲惫.他决定离开自己的星球,开启星际旅行,寻找“更重要的事”."
            m 7euc "临别时,玫瑰收起了任性,想挽留小王子,但小王子还是离开了,前往了其它星球."
            m 7eud "小王子在其它星球上遇到了许多形形色色的人."
            m 1esd "有一天小王子在地球发现一座花园,里面有五千朵一模一样的玫瑰."
            m 1ekc "他崩溃痛哭,原以为自己的玫瑰是宇宙唯一,此刻却感到被欺骗."
            m 7esd "但是,小王子的朋友狐狸告诉他."
            m 7dsd "本质的东西是用眼睛看不见的,{w=0.5}要用心."
            m 1esa "之后小王子理解了自己的玫瑰是全宇宙最独一无二的玫瑰."
            m 1esb "因为小王子为自己的玫瑰付出了时间."
            m 1esb "最后,小王子理解了什么是爱.此刻他迫切地想回到自己的星球."
            m 3dkc "在和狐狸告别后,小王子在毒蛇的帮助下“回”到了自己的星球."
            m 1dkc "……"
            m 1esp "故事到这里就结束了."
            m 3esd "不同人的人对这个故事有不同的理解."
            m 3tsd "我突然想问问."
            m 3hsblb " [player],{w=0.5}我会是你独一无二的玫瑰吗？"
            menu:  
                "当然":
                    pass
            m 1tubla "嘿嘿……"
            
        "现在没空":
            m 1ekd "没关系."
            m 1tkp "你总是这么忙."
            m 1duc "等你有时间了再讲给你听哦~"
    
    return