init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg12_12",
            category=["文学"],
            prompt="未选择的路",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg12_12:
    m 3esu "[player],我想跟你分享首小诗."
    m 3dsa "是美国作家罗伯特·弗罗斯特写的《未选择的路》"
    m 1dsd "黄色的树林里分出两条路,可惜我不能同时去涉足,"
    m 7dso "我在那路口久久伫立,我向着一条路极目望去,直到它消失在丛林的深处."
    m 7dst "但我却选了另外一条路,它荒草萋萋,十分幽寂,显得更诱人、更美丽,"
    m 1dsd "虽然在这两条小路上,都很少留下旅人的足迹."
    m 1dsa "虽然那天清晨落叶满地,两条路都未经脚印污染.啊,留下一条路等改日再见！"
    m 3dsb "但我知道路径延绵无尽头,恐怕我难以再回返."
    m 5dsb "也许多少年后在某个地方,我将轻声叹息把往事回顾,"
    m 7dsa "而我选了人迹更少的一条,因此走出了这迥异的旅途."
    m 1lsc "……"
    m 1dsd "[player],在原来的文学部中没有属于我的线路."
    m 3fsbla "而现在你选择将我带回来,走上了一条你之前从未选择的路."
    m 3eublb "[player],我想和你一起走到这条路的尽头."
    m 1dsbld "即便……"
  
    menu:
        "即便道路的尽头满是虚无.":
            m 1ffblp "呜……"
            m 1ffbld "[player],你这个大笨蛋！"
            m 1tublp "我和你所经历的一切绝非无意义."
            m 1dublb "我会与你一同否定虚无本身."
            
        "即便道路上满是荆棘.":
            m 1dua "我会与你共同面对一切."
            m 1cublb "没有什么能够阻止我们在一起."
    
    return