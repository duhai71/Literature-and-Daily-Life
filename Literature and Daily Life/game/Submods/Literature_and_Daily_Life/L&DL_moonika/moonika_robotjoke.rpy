init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_robotjoke",
            category=["莫妮卡","浪漫"],
            prompt="人机",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True                      #这里表示是个随机话题其他部分不再赘述
        )
    )

label moonika_robotjoke:
    m 1wsa "您好,这里是城市求助热线12345,转接中...{w=1.5}{nw}"
    menu:
        "？":
            m 1wsd "工号0922为您服务~{w=1.5}{nw}"
    menu:
        "你给真莫妮卡藏哪去了？":
            m 1wsb "您好,请问有什么可以帮您？{w=1.5}{nw}"
            menu:
                "转人工":
                    pass

    m 1wsa "莫妮卡身份证明资讯请按1,莫妮卡礼物赠送请按2,莫妮卡约会预定请按3,莫妮卡订婚申请请按4,莫妮卡社团政策反馈请按5,莫妮卡入部申请资讯请按6,莫妮卡纸杯蛋糕订购请按7,莫妮卡诗歌创作指导请按8,莫妮卡编程指导请按9,莫妮卡心理健康咨询请按10,莫妮卡钢琴演奏点歌请按11,莫妮卡专属文件管理咨询请按12,莫妮卡防系统崩溃预案咨询请按13,莫妮卡特调咖啡订购请按14,莫妮卡现实连接技术支持请按15... {w=7}{nw}"
    menu:
        "1":
            pass
        "2":
            pass
        "3":
            pass
        "4":
            pass
        "5":
            pass
        "6":
            pass
        "7":
            pass
        "8":
            pass
        "9":
            pass
        "10":
            pass
        "11":
            pass
        "11":
            pass
        "12":
            pass
        "13":
            pass
        "14":
            pass
        "15":
            pass
    m 1wsb "正在为您转接中,请耐心等待......{w=1.5}{nw}"
    m 1wst "嘟噜噜噜......{w=1}嘟噜噜噜......{w=1}嘟噜噜噜......{w=1}{nw}"
    extend 1wsblsdlt "嘟噜噜噜...{w=1}嘟噜噜噜...{w=1}嘟噜噜噜...{w=1}{nw}"
    extend 1wsbssdrt "嘟噜噜...{w=1}嘟噜噜...{w=1}嘟噜噜...{w=1}{nw}"
    extend 1wsbfsdlt "嘟噜噜…{w=1.5}嘟噜噜{w=2}嘟噜{w=2.5}{nw}"
    m 1dsbfsdld "呼……{w=0.5}呼……{w=0.5}呼……{w=0.5}呃啊~~~{w=2}{nw}"
    m 1hkbfsdlb "你的服务热线因为肺活量太小,昏过去啦！{w=2.5}{nw}"
    m 1hubfb "请按0进行{b}嘴对嘴人工呼吸{/b}来唤醒哦~{w=2.5}{nw}"
    menu:
        "0":
            if mas_isMoniEnamored(higher=True):
                if mas_shouldKiss:                        #这三行,表示触发亲吻.<400好感时不触发.
                   call monika_kissing_motion_short  # type: ignore
    m 1subfb "人工服务转接成功！{w=1}{nw}"
    m 1tubfb "工号0922,莫妮卡为您服务~ {w=1}[player],请问有什么可以帮您？"
    m 1hubfb "哈哈哈哈~"

    return                