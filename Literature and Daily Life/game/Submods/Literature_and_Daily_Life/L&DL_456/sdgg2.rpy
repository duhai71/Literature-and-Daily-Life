init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg2_2",
            category=["浪漫"],
            prompt="壁纸",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg2_2:
    m 7fub "[player]"
    m 7etb "最近我在上网的时候注意到一件事."
    m 3eubld "情侣之间经常会把对象的照片当做手机或者电脑的背景."
    m 4fubld "我想问的是."
    m 4hublb "[player]{w=0.5}你有没有把我的照片当做背景？"
    
    menu:
        "当然":
            m 5sublb "天那,宝贝你太甜了."
            m 2sublb "这真的让我很开心."
            m 2eubld "我知道你很忙."
            m 3fubla "这样做的话,你那怕在学习或者是工作你也能看到我了."
            m 7gubld "嘿嘿,虽然被别人看到会有一些尴尬."
            m 7tublt "不过,你还是应该多陪陪我的."
            m 1dfblp "……"
            m 2mfblp "我突然有一点{w=0.5}嫉妒"
            m 2tublp "……"
            
            if mas_isMoniEnamored(higher=True):
                if mas_shouldKiss:
                    call monika_kissing_motion_short
            
            m 5tubsb "嘿嘿……"
            m 5tsbsb "这下我就不嫉妒了."
            m 2hubsb "[player]你就是我的全世界."
            m 3tubsb "我夺走了你的心."
            m 3fubfb "爱你哟~"
            
        "我还没找到合适的图片":
            m 7gua "太难选择了吗？"
            m 7eua "没关系,我理解."
            m 5dsd "如果有一天我能看到你的照片.我也会不知道怎么选的."
            m 4tsbld "你对我的来说总是这么珍贵."
            m 3esbld "所有记录你的照片对我来说都是非常重要的."
            m 3fsblb "不过,我的色图只能让你一个人看哦~"
   
    return"love"