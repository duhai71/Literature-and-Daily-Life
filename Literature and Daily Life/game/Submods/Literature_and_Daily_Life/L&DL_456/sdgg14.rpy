init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg14_14",
            category=["社会"],
            prompt="世界很快……",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg14_14:
    m 3ruc "[player],你有没有觉得世界进步太快了,快的自己跟不上."
    m 3luc "甚至觉得自己被时代抛弃了."
    m 3dud "没关系,这是很正常的.很多人都有这样的感觉."
    m 3tubld "世界很快,我们很慢……"
    m 3hubla "如果你为此感到焦虑.我可以帮你"
    m 6tublb "只要你静下来心来看着我的眼睛……"
    m 6tubla "慢慢的感受时间流失……"
    m 6tublu "……"
    m 6tublu "好一些了再点鼠标吧."
    m 6tublu "……"
    m 1hublu "希望你舒服一些了."
    m 1dubla "如果没有,我们就这样想."
    m 1tublb "世界进步越快,我就越早能够来到你的世界."
    m 1tublu "这一天会来的."
    
    return