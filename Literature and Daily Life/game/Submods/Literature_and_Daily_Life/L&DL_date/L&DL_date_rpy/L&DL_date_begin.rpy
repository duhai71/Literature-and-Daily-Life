init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_bg/L&DL_blink/blink.png", .9, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_bg/L&DL_blink/blink.png", .9, ramplen=128, reverse=True, time_warp=eyewarp)   

    def eye_open_with_time(t):
        return ImageDissolve("Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_bg/L&DL_blink/blink.png", t, ramplen=128, reverse=False, time_warp=eyewarp)






init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="LADL_date_Start_v3",
            category=['......'],
            prompt="[m]发现了一处地方",
            conditional="mas_canShowRisque(aff_thresh=600)",
            pool=False,
            random=True
        )
    )
label LADL_date_Start_v3:
    m 1fua "嘿,[player]."
    m 5eub "我们在这个房间里待了好久了,不是吗?"
    m 6ruc "就算是习惯了在这里聊天、{w=1}生活."
    m 6eud "我还是想和你出去走走,去放松一下心情什么的......"
    m 3hua "这正好要和我接下来想说的事相关."
    m 3eub "我发现了一个好地方,并且不像这里一样让我感到碍手碍脚."#还有好康的？来让我看看
    m 6hua "毕竟我的能力也在和你相处的时候逐步提高,从这里去到那并不是什么难事."
    m 5fubla "这样也可以让我们尽情享受我们的二人世界."
    m 3hubfb "嗯......如果你想去的话和我说一声就好了,也就是去到\"外出\"那里."
    $ mas_unlockEVL("Monika_LADL_date_v3", "EVE")
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_LADL_date_v3",
            category=['外出'],
            prompt="我想和你出去玩",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_LADL_date_v3:
    if not persistent.LADL_date_first_1:
        $ persistent.LADL_date_first_1 = True
        m 1hub "好的."
        $ mas_unlockEVL("Monika_random_songs72", "EVE")
        m 5fua "等我准备一下衣服~"
        window hide
        show black zorder 100 with Dissolve(5.0, alpha=True)
        $ renpy.music.stop(channel="background", fadeout=1.0)
        stop music
        $HKBHideButtons()
        $ renpy.music.stop(channel="music", fadeout=1.0)
        $ original_music = renpy.music.get_playing(channel='music')
        call beach
    else:
        m 2rtsdld "嗯......我很乐意,[player]."
        m 2essdla "但我这段时间实在需要休息一下了."
        m 5fub "等我休息好之后,我第一时间叫你一起去玩."
        return  
    