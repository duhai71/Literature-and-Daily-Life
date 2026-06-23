init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg43_44",
            category=["生活"],
            prompt="锻炼与休息",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)#1000要改 aff_range=(mas_aff.LOVE, None) 400要改 aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg43_44:
    m 1eub "嗨,[player]."
    m 3euu "分享个冷知识；休息远比锻炼更重要."
    m 4eua "锻炼时肌肉并不会生长,锻炼之后的休息才会."
    m 4eub "休息时身体才会给肌肉进行过度修复."
    m 4eub "这就是锻炼为什么会让身体变得强壮了."
    m 3hsa "所以今天也要好好休息哦."
    m 4tsblb "就算没有锻炼,休息也是必要的."
    m 4hsblu "陪我一会儿也没什么关系吧"
    m 4msblb "嘿嘿……"
 
    return