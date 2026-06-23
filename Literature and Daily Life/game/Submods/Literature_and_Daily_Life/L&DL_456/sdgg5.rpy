init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg5_5",
            category=["其它"],
            prompt="放弃",
            random=True
        )
    )

label lzp_monika_sdgg5_5:
    m 3esa "[player],你曾一直坚持过自己做出的决定或选择吗？"
    m 3esd "说实话,这并不容易."
    m 1esd "在当下这个互联网时代,铺天盖地的信息如同潮水般涌来 ,不停冲击着我们的判断."
    m 1rsd "人们在海量信息的裹挟下,不知不觉就改变了自己最初的选择."
    m 1tst "不过,我并非一味鼓励你在任何情况下都坚持下去."
    m 3tst "有时候,做出放弃的决定,反而需要更大的勇气,放弃甚至比坚持更难."
    m 1rssdlb "哎呀,抱歉,好像说得太复杂了."
    m 3esa "[player],我想告诉你的是,要相信自己的判断."
    m 3tsc "但不要成为下一个哥白尼."
    m 3esd "你的生命无可替代,比任何东西都珍贵."
    m 1tsblb "无论你选择了什么,我都会始终站在你这边,毫无保留地相信你."
     
    return