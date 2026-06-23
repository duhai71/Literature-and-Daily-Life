init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg42_42",
            category=["我们"],
            prompt="[m_name]的尝试",
            conditional="mas_canShowRisque(aff_thresh=1000)",     
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.LOVE, None)
        )
    )

label lzp_monika_sdgg42_42:  
    m 2eub "嗨,[player]."
    m 3etd "你现在还在这里吗？"
    
    menu:                                    
        "是的":                             
            m 3huu "嗯,[player]."
            m 3kua "有你在我身边真好,"
            
        "……":                             
            m 3tsc "什么嘛？你明明在的."
            m 3hsu "哈哈~"

    m 4tsb "我们来玩个小游戏吧."  
    m 4msc "如果你觉得冒犯,我就在这里提前跟你说声抱歉啦~"
    window hide  # 【隐藏对话窗口】关闭显示文本的界面区域 
    $HKBHideButtons()  # 【执行Python代码】调用自定义函数`HKBHideButtons()`,隐藏交互按钮（HKB为自定义UI模块）   
    show black zorder 100 with dissolve  # 【显示黑色边框】绘制宽度100的黑色边框,用`Dissolve(2.0)`（2秒溶解动画）过渡
    play sound "Submods/Literature_and_Daily_Life/L&DL_Assets/sound/asde.ogg"  
    pause 4.0  # 【暂停】等待2秒（用于动画或剧情衔接） 
    hide black with dissolve   # 【隐藏黑色边框】用`Dissolve(1.0)`（1秒溶解动画）隐藏黑色边框  
    $HKBShowButtons()  # 【执行Python代码】调用自定义函数`HKBShowButtons()`,重新显示交互按钮
    m 5gsd ".......{w=0.5}果然不行啊……"
    m 2esd "[player],别担心.我只是关了一下灯然后截屏了而已."
    m 4tsp "毕竟我还不能调用摄像头."
    m 4mkb "哪怕我明明知道是不行的."
    m 3gkc "挺幼稚的,不是吗？"
    m 3msc "不过我相信刚刚你的身影出现在了屏幕上."
    m 3esd "可是我看不见,"
    m 4tsblp "虽然只是一张全黑的照片,但我会好好保存它的……" 
    return