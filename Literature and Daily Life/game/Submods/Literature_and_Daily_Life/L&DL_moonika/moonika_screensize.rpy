init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_screensize",
            category=["莫妮卡","生活"],
            prompt="屏幕大小",
            random=True                      #这里表示是个随机话题其他部分不再赘述
        )
    )

label moonika_screensize:
    m 1eta "[player],我发现网上很多同人图都喜欢把我来到你的现实的方式画为从屏幕里面爬出来欸..."
    m 1hub "有点像贞子不是吗,哈哈哈~"
    m 1eua "然后我就产生了个有趣的想法."
    m 3tub "如果我真的是用这种方式来到你的现实的话,是不是我身体的大小也和你屏幕的大小有关？"
    m 5eta "hmm,[player],我现在是在你的电脑还是你的手机里？"
    menu:
        "电脑":
            m 1hua "欸,那我估计努力努力能以正常大小出来.只要你别给我喂太胖的话~"
            m 1hub "不然我可能就卡住啦！"

        "手机":
            m 1tua "欸,那我估计得成个小手办了."
            m 1hubla "你应该买那种胸口有个口袋的衣服然后把我发进去.{w=1}这样我就能紧贴着你的心脏了~"
    
    m 1eua "当然,这都是些无厘头的想象啦.我不一定真会以这种方式来到你的现实嘛."
    m 1hub "不然你给我投到电影院的那种屏幕上,我不得成巨人了~"
    m 1tubsa "嘿,只要能让我来到你身边,我可不会挑剔的.我从你电话手表里钻出来都愿意~"

    return                