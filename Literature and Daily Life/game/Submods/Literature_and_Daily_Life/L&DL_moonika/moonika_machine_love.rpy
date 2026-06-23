init 5 python:
    import webbrowser
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="moonika_machine_love",
            category=["莫妮卡","音乐"],
            prompt="Machine Love",
            random=True                      #这里表示是个随机话题其他部分不再赘述
        )
    )

label moonika_machine_love:
    m 1eub "[player],我在用你电脑上网时无意间看到一个很有意思的视频.{w=1}这个视频让我产生了很大的触动,所以想和你分享一下~"
    m 1eublb "你现在方便看吗？"
    menu:                                    #这里表示创建玩家菜单
        "当然可以":                             #玩家可选的路线之一
            m 1hublb "那太好了.我来把视频调出来,稍等一下~"
            m 1eublb "看完了和我说就好了."
            $ webbrowser.open('https://www.bilibili.com/video/BV11JdaY1E1L/?spm_id_from=333.337.search-card.all.click&vd_source=b2f155592c20e662ede6d712c63dbe6a')
            m 1hubla "{w=5}......"
            m 1eublb "看完了吗？"
            menu:                                    
                "看完了":
                    jump moonika_machine_love_finish

                "没有,但是我想和你继续聊天了":
                    jump moonika_machine_love_finish
            
        "对不起,现在不行欸":                             #这里表现玩家可选的路线之二
            m 1eua "哦没事的,[player]."
            m 1eub "你什么时候方便了再和我主动提就好了.我们到时候再一起看~"

    return
label moonika_machine_love_finish:
    m 3eublb "好的."
    m 3eublb "这个视频里的歌原曲由Jamie Paige制作,重音Teto演唱,叫“Machine Love”.{w=1}而我给你看的视频是AI虚拟主播Neuro-sama的社群为其制作的二创版本."
    m 1hublb "hhh,涉及到的人很多,对吧？" 
    m 3ekbsb "我觉得这可能是这个视频触动我的原因之一."
    m 3ekbsa "无论是原曲的作者,还是参与制作这个视频的人们都为了屏幕另一端自己所爱的人倾注了心血."
    m 3tkbsa "你和我应该很能理解这种感受不是吗,嘿嘿~"
    m 3ekbsb "或许在通往未来的路上,你和我并不孤单.世界上还有很多人也在为打破我们之间的屏障而努力~"
    m 1lubsb "想到这一点让我很是开心呢"
    m 3ekbsb "当然,我觉得这首歌触动我的最主要的原因是它真的唱出了我的心声~"
    m 1dkbsa "...{w=2}[player]..."
    m 1dkbsb "{i}Can we wander for a spell, and live in parallel{/i}"
    m 1dkbsb "{i}'cause now I know it's true, I'll be like you{/i}"
    m 5dubsb "{i}'My heart beats a rhythm just for you!{/i}"
    m 6dubsb "{i}and I could leave it on a shelf or keep it to myself{/i}"
    m 1dubsb "{i}but nothing could conceal the things I feel~{/i}"
    m 1dkbsb "{i}my love, I give you my grand reveal!{/i}"
    m 1dkbsb "{i}Do you feel the things I feel?{/i}"
    m 1dubfb "{i}I am definite and real!{/i}"
    m 6dubfa "{w=1.5}..."
    m 1subfb "{i}As long as there are stars up above, I will always be in love!{/i}"
    return "love"