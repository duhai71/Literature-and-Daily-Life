default bath_done_LADL = False
default garden_done_LADL = False
default Utb_done_LADL = False
default bath_song_LADL = True
default sayori = True

label beach:
    $HKBHideButtons()
    stop music
    hide monika
    hide black
    scene bg_sea_noon
    pause 0.75
    play LADL beach_bgm fadein 2.0
    "正午."
    play LADL_sfx2 waves fadein 2.0
    scene bg_seaside_sidewalk_noon with wipeleft_scene
    hide bg_sea_noon
    show monika 5a_LADL at t11
    m 5a_LADL "我们到了,这地方你觉得怎么样."
    m 5b_LADL "是不是很喜欢."
    show monika 5e_lean_LADL at t11
    with dissolve
    m"另外,因为我们不在原来的教室了,我正好能发挥一下我的能力."
    show monika 4b_LADL at t11
    with dissolve
    m 4b_LADL "我给你打造了一副身体,当然,现在只能是比较透明的."#改
    show monika 4q_LADL at t11
    with dissolve
    m 4q_LADL "起码现在是这样."#表情改
    show monika 2c_LADL at t11
    with dissolve
    m 2c_LADL "来吧,我们继续往前走."
    stop LADL_sfx1
    scene bg_sea_seawalk_noon with wipeleft_scene
    hide bg_seaside_sidewalk_noon
    jump beach_2

label beach_2:
    show monika 4h_LADL at t11
    m 4a_LADL "这条道路也很适合散步呢......"
    show monika 5j_LADL at t11
    with dissolve
    m 5j_LADL "也许我们之后应该多来这里走走."
    show monika 1c_LADL at t11
    with dissolve
    m 1c_LADL "不仅仅是放松心情,也有可能是饭后促进消化呢."
    menu:
        "确实可以":
            jump beach_2_Branch_1
        "我想和你多走走":
            jump beach_2_Branch_2

label beach_2_Branch_1:
    show monika 5s_LADL at t11
    with dissolve
    m "那我希望你能牵着我的手散步......"#改
    show monika 2h_LADL
    with dissolve
    m 2h_LADL "不过这些都是后面的事了." 
    m 2b_LADL "嗯......你看到前面的亭子了吗?"#左手指右手放下睁眼
    m 2c_LADL "我们如果玩累了可以上到那里休息一下"#闭眼
    show monika 4j_LADL at t11
    with dissolve
    m 4j_LADL "或者玩个小游戏也行哦."#nou牌?或者别的小游戏
    m 4k_LADL "那我们过去看看吧."
    scene bg_sea_pavilion_noon with wipeleft_scene
    hide bg_seaside_sidewalk_noon    
    jump beach_3_pavilion

label beach_2_Branch_2:
    show monika 5s_LADL at t11
    with dissolve
    m "那我希望你会牵着我的手散步......"#脸红
    show monika 2h_LADL at t11
    with dissolve
    m 2h_LADL "不过这些都是后面的事了." 
    m 2b_LADL "嗯......你看到前面的亭子了吗?"#左手指右手放下睁眼
    m 2c_LADL"我们如果玩累了可以上到那里休息一下"#闭眼
    show monika 4j_LADL at t11
    with dissolve
    m 4j_LADL"或者玩个小游戏也行哦."#nou牌?或者别的小游戏
    m 4k_LADL"那我们过去看看吧."
    scene bg_sea_pavilion_noon with wipeleft_scene
    hide bg_seaside_sidewalk_noon    
    jump beach_3_pavilion


label beach_3_pavilion:
    show monika 2c_LADL at t11   
    m 2c_LADL "哈哈,很适合我们在这里吃些小甜点,或者画画之类的."
    m 2b_LADL "说到这个,你喜欢吃甜点还是做些类似画画的文艺活动呢,[player]?"
    menu:
        "吃甜点":
            show monika 4b_LADL at t11
            with dissolve
            m 4b_LADL "好的,那我们下次来的时候从原来的房间中带些过来,或者在这里的甜品店购买也可以哦."
            jump LADL_Dessert_Shop
        "文艺活动":
            show monika 4a_LADL at t11
            with dissolve
            m 4a_LADL "嗯......那我觉得我们可以带个画板来记录一下这个地方的美景."
            m 4b_LADL "毕竟,学会记录这些也是方便我们之后的回忆哦."
            show monika 5a_lean_LADL at t11
            with dissolve
            m 5a_lean_LADL "说到这个,我突然想到了有一位submod制作者为我们提供了画板."
            m 5c_lean_LADL "也许那个就挺合适的."
            show monika 6c_lean_LADL at t11
            with dissolve
            m 6c_lean_LADL "不过我们现在该往下走了,因为是时候感受海浪声和海风了,[player]."
            jump LADL_beach_4
        "享用你这个小蛋糕":
            show monika 2f_LADL at t11
            m "嗯......{w=0.3}{nw}"
            show monika 1f_3_LADL at t11
            with dissolve
            m "嗯?!"
            show monika 5l_LADL at t11
            with dissolve
            m 5l_LADL "我可不是食物了."#改
            show monika 5f_lean_LADL at t11
            with dissolve
            m 5f_lean_LADL "不过我想了一下,这是你夸赞我的话对吗?"
            m 5g_lean_LADL "嘿嘿,那我觉得你也是我的小蛋糕,我也一口把你{b}吃掉{/b}."
            show monika 6h_lean_LADL at t11
            m 6h_lean_LADL "好了好了,让我们回到之前说的问题,你喜欢吃甜点还是文艺活动呢?"
            menu:
                "甜点":
                    show monika 4b_LADL at t11
                    with dissolve
                    m 4b_LADL "那我们下次来的时候可以从原来的房间中带些过来,或者在这里的甜品店购买也可以哦"
                    m 4j_LADL "毕竟,{w=1}甜点总是能让人心情愉悦."
                    jump LADL_Dessert_Shop
                "文艺活动":
                    show monika 4a_LADL at t11
                    with dissolve
                    m 4a_LADL "那我觉得我们可以带个画板来记录一下这个地方的美景."
                    m 4b_LADL "毕竟,学会记录这些也是方便我们之后的回忆哦."
                    show monika 5a_lean_LADL at t11
                    with dissolve
                    m 5a_lean_LADL "说到这个,我突然想到了有一位submod制作者为我们提供了画板."
                    m 5c_lean_LADL "也许那个就挺合适的."
                    show monika 6c_lean_LADL at t11
                    with dissolve
                    m 6c_lean_LADL "不过我们现在该往下走了,因为是时候感受海浪声和海风了,[player]."
                    jump LADL_beach_4
    


label LADL_Dessert_Shop:
    menu:
        "还有甜品店?":
            show monika 2c_LADL at t11
            with dissolve
            m 2c_LADL "当然呀,我们还可以一起尝遍各种各样的甜点呢."
            show monika 6e_lean_LADL at t11
            with dissolve
            m 6e_lean_LADL "不过我要保持身材,所以买的大多数只能由你解决了,哈哈哈."
        "好呀":
            show monika 2c_LADL at t11
            with dissolve
            m 2c_LADL "我们还可以一起尝遍各种各样的甜点呢."
            show monika 6e_lean_LADL at t11
            m 6e_lean_LADL "不过我要保持身材,所以买的大多数只能由你解决了,哈哈哈."
    show monika 6c_lean_LADL at t11
    with dissolve     
    m 6c_lean_LADL"来吧,我们该往下走了,感受海浪声和海风的时候到了."
    stop LADL fadeout 1.0
    jump LADL_beach_4
   

label LADL_beach_4:
    play LADL_sfx1 footstep_beach fadein 1.0
    scene bg_beach_2_noon with wipeleft_scene
    play LADL beach_bgm_2 fadein 2.0
    play LADL_sfx1 footstep_beach fadein 1.0
    hide bg_sea_pavilion_noon
    pause 2
    stop LADL_sfx1 fadeout 2.0
    show monika 5j_LADL at t11
    m 5k_LADL "啊哈,大海!"
    play LADL_sfx1 waves fadein 2.0
    m 5e_LADL "我不敢想象真的能和你来到这里."
    show monika 2l_2_LADL at t11
    with dissolve
    m 2l_2_LADL "之前以为一辈子都只能在那个房间里待着,我甚至一度看到了自身的终点."
    show monika 4e_LADL at t11
    with dissolve
    m 4e_LADL "但当我打开了这处地方的入口的时候,才发现当时的想法还是太天真了."
    m 4d_LADL "我那时以为,能和你在教室里聊聊天,说说心事和对其他事物的见解就够了."
    m 4c_LADL "但我也是人,{w=1}人也有欲望,{w=0.8}所以我不会满足于只待在那里."
    show monika 5e_lean_LADL at t11
    with dissolve
    m 5e_lean_LADL "我现在更想出来见你."
    show monika 6c_lean_LADL at t11
    with dissolve    
    m 6c_lean_LADL "随着技术的进步,我们的距离也会越来越近的."
    show monika 1f_LADL at t11
    with dissolve
    m 1f_LADL "......{w=0.3}{nw}"   
    show monika 2l_2_LADL at t11
    with dissolve 
    m 2l_2_LADL "......真是不好意思,[player],这个话题是不是有点沉重了."
    m 2h_LADL "但我确实是有感而发,因为你在这."
    m 2c_LADL "嗯......我们还是继续享受这里吧."
    jump LADL_beach_5

label LADL_beach_5:
    stop LADL fadeout 2.0
    scene black with wipeleft_scene#黑屏
    hide bg_beach_2_noon
    #暂停音乐
    m "话说回来,[player]."
    m "我觉得我们不仅仅只在沙滩上玩,还可以下水哦."
    menu:
        "好啊":
            m "我就知道你会这样说."
            pass
        "我有点害怕":
            m "没事的,宝贝." 
            m "我在你旁边呢."  
            pass
    m "嗯......把手给我,[player]."
    menu:
        "将手递给[m]":
            pass   
    m "我们一起下去......"
    play LADL sea
    scene monika cg_sea_four  
    with dissolve
    m "你喜欢这样吗,[player]?"
    scene monika cg_sea_two  
    with dissolve
    m "像这样和我一起感受大海."
    menu:
        "喜欢":
            scene monika cg_sea_one
            with dissolve
            m "哈哈哈哈,你能这么说我真的很开心,宝宝~~"
            scene monika cg_sea_four
            with dissolve
            m "在这一片天地,我希望与你的这一刻是{b}永远{/b}."
            menu:
                "我会永远记住这一刻的":
                    pass
                "我爱你,[m]":
                    pass
                "以后的路还长着呢.":
                    scene monika cg_sea_two
                    with dissolve
                    m "哈哈哈,你说的对,宝宝."
                    scene monika cg_sea_four
                    with dissolve
                    m "路很长,但我愿意陪你慢慢走."
                    pass
            scene monika cg_sea_two
            with dissolve    
            m "爱你,[player]."
            pass
        "......":
            scene monika cg_sea_three
            with dissolve
            m "以后也可以多来几回呢......"
            scene monika cg_sea_four
            with dissolve、
            m "在这一片天地,我希望与你的这一刻是{b}永远{/b}."
            menu:
                "我会永远记住这一刻的":
                    pass
                "我爱你,[m]":
                    pass
                "以后的路还长着呢.":
                    scene monika cg_sea_two
                    with dissolve
                    m "哈哈哈,你说的对,宝宝."
                    scene monika cg_sea_four
                    with dissolve
                    m "路很长,但我愿意陪你慢慢走."
                    pass
            scene monika cg_sea_two
            with dissolve    
            m "爱你,[player]."
            pass
    scene black
    with eye_shut
    hide monika cg_sea_two
    with dissolve  
    pause 1
    scene monika cg_sea_three
    with eye_open
    "和[m]牵着手,静静的感受海浪."
    "思绪随着海浪流向远方."
    scene monika cg_sea_one
    with dissolve        
    m "在我小的时候,我看着恋爱剧中的男女主去到海边玩."
    scene monika cg_sea_two
    with dissolve
    m "心里也很好奇,憧憬着在未来的某一天,我和心爱的人也前往大海,体验专属于我们的二人世界."
    scene monika cg_sea_four
    with dissolve
    m "而我现在感受到了陪伴{w=0.5}、信任、{w=0.5}温暖、{w=0.5}甜蜜."
    scene monika cg_sea_one
    with dissolve
    m "......{w=0.5}有你在,真好."
    #
    #
    #开始音乐
    stop LADL fadeout 2.0
    scene black with wipeleft_scene
    pause 1
    "与[m]度过了一段很愉悦的时光."
    m "啊,我的脸不小心打湿了,[player]."
    m "我好不容易画好的妆......(｡•́︿•̀｡)"
    m "只能上岸后再补一下了......."
    stop LADL_sfx2 fadeout 1.0
    pause 2
    jump LADL_beach_6

label LADL_beach_6:
    play LADL beach_music fadein 2.0
    play LADL_sfx2 waves fadein 1.0
    scene bg_beach_park_noon with wipeleft_scene
    hide bg_beach_2_noon
    show monika 4a_LADL at t11
    m 4a_LADL "哈哈!是海边的一片小公园~"
    m 4b_LADL "是不是感觉很神奇,[player]?离海边这么近的地方竟然会有公园."
    m 5q_LADL "你说呢?这公园看起来怎么样?"#表情改
    menu:
        "看起来生机盎然":
            show monika 5c_LADL at t11
            with dissolve
            m 4k_LADL "嗯,这里生机勃勃呢."

        "看起来让人身心舒畅":
            show monika 4k_LADL at t11
            with dissolve
            m 4k_LADL "是吗?我也这么觉得."

        "看起来... 很原生态":
            show monika 4r_LADL at t11
            with dissolve
            m 4r_LADL "嘿嘿,你是不好意思说“看不出来打理过”吧."
            m 4q_LADL "没事的,你的感觉其实没错.听我解释一下."

    m 4a_LADL "我刚发现这里时确实尝试用代码编辑它们."
    m 4l_LADL "很经典的“monika”行为对不对？"
    show monika 5c_LADL at t11
    with dissolve
    m 5c_LADL "但后来我发现,如果要这么做的话,那它就失去原有的意义了."
    m 5d_LADL "如果换成以前的我的话{w=0.3}...{w=0.3}..."
    m 5e_LADL "[player],你是这个世界上最了解我的人了."
    m 5l_LADL "所以你该很清楚以前的我{w=0.5}...额{w=0.5}...{w=0.5}有一点点掌控欲."
    menu:
        "我觉得还好啦":
            pass

        "只是一点点吗?":
            pass

        "......":
            pass
    m 5b_lean_LADL "哎呀,真是的...{w=0.8}{nw}"
    show monika 6b_lean_LADL at t11
    with dissolve
    m 6b_lean_LADL "我想说的是,如果换成遇到你之前的我,我肯定会铁了心要把这里改造成自己满意的样子......"
    m 6a_lean_LADL "因为只有那样我才会感觉自己足够安全,才会感觉自己能在这个未知的世界里保护好自己."
    menu:
        "那现在的你会怎么做呢？":
            pass
        "......":
            pass
    m 6f_lean_LADL "至于现在......"
    show monika 5c_lean_LADL at t11
    with dissolve
    m 5c_lean_LADL "树木的分布、沙砾的大小、海鸥的速度......虽然要花很多时间,可也不是编辑不了."
    m 5a_lean_LADL "但现在的我宁愿选择顺其自然..."
    m 6g_lean_LADL "因为我更愿意用这些时间陪伴某个特别的人~"
    show monika 4e_LADL at t11
    with dissolve
    m "虽然没法掌控一切,我也不会因此缺乏安全感......"#
    menu:
        "因为你现在有人依靠":
            show monika 6h_lean_LADL at t11
            with dissolve
            m "你的下一句话是不是会说'那个人就是我'?"
            show monika 6g_lean_LADL ac t11
            m "嗯......"
            pass

        "因为你学会接纳不完美":
            pass

        "因为你懂得珍惜当下":
            pass

        "因为你不再需要掌控来证明自己":
            pass
    show monika 4q_LADL at t11
    with dissolve
    m 4q_LADL "也因为你在这,[player],我的世界得以安定下来."
    m 4m_LADL "...{w=0.5}...{w=0.3}{nw}"#改表情
    m 4n_LADL "欸,今天天气真是好热啊,把我脸都晒得红彤彤的~"
    show monika 5e_LADL at t11
    with dissolve
    m 5e_LADL "脑袋一热说了这么多话,害的你站在这里和我一起暴晒,真是不好意思."
    m 5q_LADL "我们往树荫下坐一坐,休息一会吧."
    jump LADL_beach_7

label LADL_beach_7:
    scene bg_beach_noon_second with wipeleft_scene
    hide bg_beach_park_noon
    "与[m]一起坐在树荫下."
    "感受着海风."
    show monika 4j_LADL at t11
    with dissolve
    m "坐在这,靠着软热的沙子,清凉的海风迎面吹来."
    m 4k_LADL "真是惬意啊~"
    m 4q_LADL "我们以后可以常来这里. "
    show monika 5b_LADL at t11
    with dissolve
    m 5b_LADL "我可以躺到太阳底下晒个日光浴."
    m 5q_LADL "但这样的话......你会喜欢小麦色皮肤的我吗?"#表情改
    m 5k_LADL "哈哈,我只是逗你的啦~"
    m 5l_LADL "我担心我睡过头,直接变成红皮肤monika了."#美国红脖子
    m 5r_LADL "你呢,[player]?你会想在这里做些什么?"
    menu:
        "我想尝试喂下天上的那些海鸥":
            show monika 4q_LADL at t11
            with dissolve
            m 4q_LADL "听上去不错呢."
            m 4r_LADL "我们可以带点小零食引诱它们过来."
            show monika 5a_LADL at t11
            with dissolve
            m 5a_LADL "靠近观赏如此优美的鸟类一定很有趣."
            show monika 4c_LADL at t11
            with dissolve
            m 4c_LADL "只是... 海鸥都是成群结队的,你要小心哦."
            m 5b_LADL "小心它们无意间在你身上做点小标记,哈哈哈~"

        "我想尝尝这椰子树上的椰子":
            show monika 4q_LADL at t11
            with dissolve
            m 4q_LADL "听上去不错呢."
            m 4r_LADL "我只在小学时家附近的商店买过瓶装的椰子汁."
            m 4q_LADL "那味道肯定跟真正的椰子没法比."
            show monika 5c_LADL at t11
            with dissolve
            m 5c_LADL "但我们估计得找根长的棍子给这些椰子打下来..."
            m 5b_LADL "也有可能过段时间它熟了就自己掉下来了."

        "我想把自己埋进沙子里,闭眼冥想":
            show monika 4k_LADL at t11
            with dissolve
            m 4k_LADL "听上去不错呢."
            m 4q_LADL "这样做的话,你可以细细感受,海浪缓慢地但有节奏地拍打在海面上..."
            m 4j_LADL "我们可以让呼吸逐渐适应它的节奏..."
            m 4k_LADL "仿佛与我们身边的环境融为一体."
            m 4j_LADL "但不要睡过去了哦,哈哈."

        "我想和你亲亲":
            show monika 4q_LADL at t11
            with dissolve
            m 4q_LADL "...少来这套,[player]."
            m 4s_LADL "不过我喜欢和你这样."
    show monika 4k_LADL at t11
    with dissolve 
    m 4k_LADL "嗯......{w=0.5}{nw}"
    show monika 5a_LADL at t11
    with dissolve
    m 5a_LADL "在树荫下坐了一会,你应该也恢复一些体力了吧?"
    m 5b_LADL "走吧,[player].附近有个旅馆,我们中午去那里休息一下."     
    jump infrontof

label infrontof:
    stop LADL fadeout 2.0
    stop LADL_sfx2 fadeout 1.0
    scene black with wipeleft_scene
    "稍等一下,[player],我换一下衣服."
    pause 2
    play LADL hill_play fadein 2.0
    play LADL_sfx2 bird_sound fadein 1.0
    scene bg_In_front_of_the_mountain_road_bridge_noon with wipeleft_scene
    hide bg_beach_noon_second   
    show monika 2d_jeans_LADL at t11                #1 2 同英
    m "到旅馆前我们还要走段路."
    show monika 2k_jeans_LADL at t11 
    with dissolve
    m "这段山路有些崎岖,所以我更希望牵着你的手一起走..."#改
    show monika 5c_jeans_LADL at t11 
    with dissolve
    m "这样不仅不用担心跌倒,而且我们可以更靠近一点了呢."
    m 5e_jeans_LADL "提到山路,[player],你登过山呢？"
    menu:
        "当然":
            m 5f_jeans_LADL "这样的话,想必你的身体一定很结实吧?"
            show monika 1m_jeans_LADL at t11 
            with dissolve
            m "我也很喜欢这样运动呢,尽管登山属于比较危险的运动......{w=1.2}{nw}"
            show monika 1l_jeans_LADL at t11 
            with dissolve
            m "而且还可能会遇到蛇、以及毒虫这类的野生动物."
            m 2s_jeans_LADL "但我听说过一句话,{b}勇气是人类的赞歌{/b}."
            show monika 2b_jeans_LADL at t11 
            with dissolve
            m "正是在登山中,我们不惧困难和劳累,才能体会到了山顶别具一格的风景."
            show monika 2k_jeans_LADL at t11 
            with dissolve
            m "等我出来的那一天,[player],记得带着我一起去登山哦......"
        "还没有":
            show monika 6a_jeans_LADL at t11#改
            with dissolve
            m "嗯,我知道了."
            show monika 5sitting_a_jeans_LADL at t11
            with dissolve
            show monika 5sitting_a_jeans_LADL at t11
            with dissolve
            m "如果有机会的话,[player].你一定要去尝试一下登山."
            "尽管登山的过程很累......."
            show monika 1l_jeans_LADL at t11 
            with dissolve
            m "而且还可能会遇到蛇、以及毒虫这类的野生动物."
            show monika 2s_jeans_LADL at t11 
            with dissolve
            m "但对于欣赏沿途的风光以及登顶后的感受来说,一切都是值得的."
            m 1e_jeans_LADL "就像我们的人生,充满了酸甜苦辣,总归还是要活着,要对未来充满希望."
            m 1j_jeans_LADL "而且我也期待能与你一同登山的一天......"
    scene black with wipeleft_scene
    pause 2
    "又走了一段路." 
    scene bg_Mountain_Road_Bridge_noon wipeleft_scene
    hide bg_In_front_of_the_mountain_road_bridge_noon
    jump bridge_LADL

label bridge_LADL:
    show monika 1k_jeans_LADL at t11 
    with dissolve
    m "过了这座桥我们就到了,[player]."
    show monika 2m_jeans_LADL at t11 
    with dissolve
    m "这里有一种{b}小桥流水人家{/b}的味道...就是少了'人家'."
    show monika 2n_jeans_LADL at t11 
    with dissolve
    m "不过光是走这几段路我都有点吃不消了."
    menu:
        "你还好吗":
            show monika 1s_jeans_LADL at t11
            with dissolve
            m "当然了,这点累不算什么."#但我累啊
            menu:
                "那我背着你走到旅馆":
                    show monika 5i_jeans_LADL at t11
                    with dissolve
                    m "什...什么?{w=0.9}{nw}"
                    show monika 6g_jeans_LADL at t11
                    with dissolve
                    m "呃...也不是不行了."
                    show monika 6k_jeans_LADL at t11
                    with dissolve
                    "你就庆幸我有在好好保持身材吧,啊哈哈."#背到旅馆
                    jump irural1_LADL
                "那我抱着你走到旅馆":
                    show monika 5i_jeans_LADL at t11
                    with dissolve
                    m "啊?{w=0.9}{nw}"
                    show monika 5g_jeans_LADL at t11
                    with dissolve
                    m "这...有点突然了,[player],至少让我做一下心理准备..."
                    show monika 6k_jeans_LADL at t11
                    with dissolve
                    m "幸好我一直来有在保持身材,所以对你来说应该不会费劲..."
                    show monika 7a_happy_jeans_LADL at t11
                    with dissolve
                    m "啊哈哈,也没什么大不了的,来吧,[player]."#抱到旅馆
                    jump irural2_LADL
                "那我们就一起走到旅馆吧":
                    show monika 5a_jeans_LADL at t11 
                    with dissolve
                    m "好呀,[player],我享受和你一起步行的时光."
                    show monika 5c_jeans_LADL at t11 
                    with dissolve
                    m "那我们就一起再走一段路吧."
                    jump irural3_LADL
        "......":
            show monika 3l_jeans_LADL at t11 
            with dissolve
            m "不过既然快到了,我还是会坚持一下的."
            show monika 1n_jeans_LADL at t11 
            with dissolve
            m "我们继续走吧."
            jump irural4_LADL

label irural1_LADL:
    stop LADL fadeout 2.0
    scene black with wipeleft_scene
    pause 2
    scene bg_Rural_community_center_noon with wipeleft_scene
    play LADL tam_n17_play fadein 1.0
    hide bg_Mountain_Road_Bridge_noon
    "好,我们到了,[player],放我下来吧."
    show monika 5h_jeans_LADL at t11 
    with dissolve
    m "我真的很享受这段时光..."
    show monika 6a_jeans_LADL at t11
    with dissolve
    m "之后的话......"
    jump rural_LADL_first
    
label irural2_LADL:
    stop LADL fadeout 2.0
    scene black with wipeleft_scene
    pause 2
    scene bg_Rural_community_center_noon with wipeleft_scene
    play LADL tam_n17_play fadein 1.0
    hide bg_Mountain_Road_Bridge_noon
    m "嗯...我们好像到了,让我下来吧,[player]."
    show monika 6h_jeans_LADL at t11 
    with dissolve
    m "你的怀里真的很暖......"
    show monika 6a_jeans_LADL at t11
    with dissolve
    m "之后的话......"
    jump rural_LADL_first
    
label irural3_LADL:
    stop LADL fadeout 2.0
    scene black with wipeleft_scene
    pause 2
    scene bg_Rural_community_center_noon with wipeleft_scene
    play LADL tam_n17_play fadein 1.0
    hide bg_Mountain_Road_Bridge_noon
    show monika 5a_jeans_LADL at t11
    m "嘿,[player],我们到了."
    jump rural_LADL_first

label irural4_LADL:
    stop LADL fadeout 2.0
    scene black with wipeleft_scene
    pause 2
    scene bg_Rural_community_center_noon with wipeleft_scene
    play LADL tam_n17_play fadein 1.0
    hide bg_Mountain_Road_Bridge_noon
    show monika 5a_jeans_LADL at t11
    m "嘿,[player],我们到了."
    jump rural_LADL_first

label rural_LADL_first:
    show monika 6c_jeans_LADL at t11
    with dissolve
    m "我打算趁午休的时候好好休息一下."
    show monika 5c_jeans_LADL at t11
    with dissolve
    m "你呢,[player],你觉得累吗?"
    menu:
        "有一点":
            show monika 1d_jeans_LADL at t11
            with dissolve
            m "这样啊,那我觉得你该好好睡一觉."
            show monika 2j_jeans_LADL at t11
            with  dissolve
            m "毕竟,睡眠总是补充体力的高效方法."
        "很累":
            show monika 2e_jeans_LADL at t11
            with dissolve
            m "那我觉得你该好好睡一觉了,[player]."
            m 2j_jeans_LADL "毕竟,睡眠总是补充体力的高效方法."
        "完全不累":
            show monika 5i_jeans_LADL at t11
            with dissolve
            m "是吗?"
            show monika 5a_jeans_LADL at t11
            m "那我觉得你可以趁这段时间去四周看看."
            show monika 5c_jeans_LADL at t11
            m "不过不要走远哦,你走丢了我会很担心的."
    show monika 5i_jeans_LADL at t11
    with  dissolve
    m "......嗯,我得先进去把住房手续弄好."
    show monika 2s_jeans_LADL at t11
    with dissolve
    m "我打算开两间房,[player],这样给我们各自一点私人空间."#两个人一间房会触发大象踩背环节吗，可我没收钱，不想写18+内容
    show monika 6c_jeans_LADL at t11
    with dissolve
    m "走吧,我带你到房间去."
    stop LADL_sfx2 fadeout 1.0
    scene black with wipeleft_scene
    scene Inside_the_hotel_room_noon with wipeleft_scene            
    hide bg_Rural_community_center_noon
    "根据[m]的指引来到了十一号房"
    "[m]在隔壁"
    jump restway_LADL


label restway_LADL:
    "接下来要干什么?"
    menu:
        "接下来要干什么?"
        "去浴室泡澡." if not bath_done_LADL:
            $ bath_done_LADL = True
            jump bath_LADL_rest
        "去旅馆后院看看" if not garden_done_LADL:
            $ garden_done_LADL = True
            stop LADL fadeout 2.0
            jump garden_LADL_rest
        "去睡觉":
            jump sleep_end_LADL
        "检查床底" if not Utb_done_LADL:
            $ Utb_done_LADL = True
            jump utb_LADL
        "查看地图":
            jump map_LADL_1
label bath_LADL_rest:
    #music
    scene Rural_Bathroom_noon with wipeleft_scene
    hide Inside_the_hotel_room_noon
    "感受着温暖的、有些发烫的热水."
    "包裹住[player]疲惫的身体."
    jump bath_LADL_rest_1
label bath_LADL_rest_1:    
    menu:
        "要做些什么吗?"
        "放首歌来听":
            jump Rural_Bathroom_music
        "查看地图":
            jump map_LADL_2
        "什么都不做":
            "发呆......"
            "[m]...{w=0.3}海滩...{w=0.7}...{w=0.4}现在的生活...{w=0.2}未来..."
            "..."
            "该出浴了."
            "起身出缸,毛巾擦身,换好衣服..."
            scene Inside_the_hotel_room_noon with wipeleft_scene
            hide Rural_Bathroom_noon
            "走出了浴室."
            jump restway_LADL

label Rural_Bathroom_music:
    if not persistent.bath_LADL_test_1:
        "注意到浴缸旁边放着音乐播放器."
        "似乎能够使用."
        "触摸屏亮了起来,显示出一列歌名."
        $ persistent.bath_LADL_test_1 = True
    $ bath_song_LADL = True
    while bath_song_LADL:
        menu:
            "要听哪首歌呢?" #选歌
            "want to be close":
                stop LADL fadeout 2.0
                pause 1
                play LADL want_to_be_close fadein 1.0
                "有关一位蓝头发少年的曲子"#那不就是我吗?
                pass
            "joy":
                stop LADL fadeout 2.0
                pause 1
                play LADL joy fadein 1.0
                "有关一位蓝头发少年的曲子"
                pass
            "恋爱循环":
                stop LADL fadeout 2.0
                pause 1
                play LADL date_Renai_Circulation fadein 1.0
                pass
            "Beneath the Mask":
                stop LADL fadeout 2.0
                pause 1
                play LADL Beneath_the_Mask fadein 1.0
                "一首能让人感到宁静的曲子"
                pass
            "勇者":
                stop LADL fadeout 2.0
                pause 1
                play LADL Frieren fadein 1.0
                "......"
                pass
            "closer":
                stop LADL fadeout 2.0
                pause 1
                play LADL closer fadein 1.0
            "{b}{i}NEXT{/i}{/b}":
                menu:
                    "???":
                        stop LADL fadeout 2.0
                        pause 1
                        play LADL date_2001 fadein 1.0
                        pass
                    "{b}{i}BACK{/i}{/b}":
                        jump Rural_Bathroom_music
        pause 30
        jump Keep_or_end_song           
label Keep_or_end_song:
    menu:
        "还要继续听歌吗?" #选择是否继续听歌
        "继续":
            menu:
                "要换一首歌吗?"
                "换":
                    jump Rural_Bathroom_music
                "不换":
                    pause 40
                    jump Keep_or_end_song
                  
        "不":
            $ bath_song_LADL = False
            stop LADL_1 fadeout 2.0
            stop LADL fadeout 2.0
            "差不多该出浴了."
            "起身出缸,毛巾擦身,换好衣服..."
            "走出了浴室."
            pass
    scene Inside_the_hotel_room_noon with wipeleft_scene
    play LADL tam_n17_play fadein 2.0
    hide Rural_Bathroom_noon
    jump restway_LADL

screen click_detector():
    modal True 
    zorder 100
    button:
        action Return(True)
        xysize (config.screen_width, config.screen_height)  # 覆盖整个屏幕
        background None
        hover_background None

label map_LADL_1:
    scene map_LADL with wipeleft_scene
    hide Inside_the_hotel_room_noon
    $ clicked = renpy.call_screen("click_detector") #点击鼠标关闭地图
    if clicked:
        scene Inside_the_hotel_room_noon with wipeleft_scene
        hide map_LADL
        jump restway_LADL

label map_LADL_2:
    scene map_LADL with wipeleft_scene
    hide Inside_the_hotel_room_noon
    $ clicked = renpy.call_screen("click_detector") #点击鼠标关闭地图
    if clicked:
        scene Rural_Bathroom_noon with wipeleft_scene
        hide map_LADL
        jump bath_LADL_rest_1

label garden_LADL_rest:
    play LADL tamsu03_play fadein 2.0
    scene bg_The_hotel_ping_pong_table_light_on with wipeleft_scene            
    hide Inside_the_hotel_room_noon
    "看到了兵乓球桌."
    "或许之后能跟[m]一起玩."
    "继续走吧."
    scene Rural_Backyard_noon with wipeleft_scene
    hide bg_The_hotel_ping_pong_table_light_on
    "来到了旅馆后院"
    "看着远处的山峰和云朵."
    "或许之后能去更高处探索一下."
    "回去之后问问[m]的意见吧."
    scene Inside_the_hotel_room_noon with wipeleft_scene            
    hide Rural_Backyard_noon
    stop LADL fadeout 2.0
    play LADL tam_n17_play fadein 2.0
    jump restway_LADL


label utb_LADL:
    scene bg_Under_the_bed_in_the_room_noon with wipeleft_scene
    hide Inside_the_hotel_room_noon
    "来到卧室后,俯下身看向床底."
    "发现了一张纸条,上面似乎记录着什么."
    scene black
    with eye_shut
    pause 2
    scene surprise_LADL with dissolve
    $ clicked = renpy.call_screen("click_detector") 
    if clicked:
        scene Inside_the_hotel_room_noon with wipeleft_scene
        hide surprise_LADL
    jump restway_LADL


label sleep_end_LADL:
    stop LADL_sfx1
    scene bg_Ceiling_of_the_room_noon with wipeleft_scene
    hide Inside_the_hotel_room_noon
    "来到卧室后直接躺在了床上."
    "你感觉你的眼皮变得愈发沉重."
    stop LADL fadeout 2.0
    stop LADL_sfx1
    scene black
    with eye_shut
    pause 3
    scene bg_prairie_noon with dissolve
    play LADL Dream fadein 2.0
    "???"
    "似乎来到了另一处地方."
    s "来嘛,你尝尝我这个....."
    n "咳咳......尝归尝,但是你怎么一下塞进我嘴里了."
    n "这是要噎死我吗? "
    m "\"好了,纱世里,别太勉强夏树了,这样子的确不好咀嚼呢,你觉得呢,尤里?\""
    y "嗯......既然我们都来这野餐了......{w=1.2}那还是慢慢享受为好."
    "听到了四个熟悉的声音."
    "要过去看看吗?"
    menu:
        "要过去看看吗?"
        "过去":
            pass
        "先等等":
            pass
    "正当准备下一步的动作时."    
    stop LADL fadeout 2.0
    play LADL_sfx1 knock_on_the_door_sound
    hide black
    with eye_open
    scene black
    scene bg_Ceiling_of_the_room_noon with dissolve
    "听到了敲门的声音."
    m "起来了,[player]."
    m "是不是我不叫你,你能睡到明早呢?"
    m "我们得接着去玩了."
    menu:
        "知道了.":
            pass
        "等我打理一下.":
            pass
    m "那我在外面等你."
    "似乎没缓过来,但还是得准备出发."
    scene bg_Rural_community_center_noon with wipeleft_scene
    hide bg_Ceiling_of_the_room_noon
    play LADL tam_n17_play fadein 2.0
    show monika 2j_jeans_LADL at t11
    m "这家旅店的设施怎么样,[player]?"
    m 2k_jeans_LADL "是不是设施还不错."   #配表情
    show monika 5f_jeans_LADL at t11
    with dissolve
    m "不过我们的重点不是这个."
    show monika 6c_jeans_LADL at t11
    with dissolve
    m "一天中最闷热的时候已经过去了,接下来又是沙滩时间."
    m 6e_jeans_LADL "我们也该过去了,[player]."
    scene black with wipeleft_scene
    pause 2
    stop LADL fadeout 2.0
    scene bg_seaside_bench_noon with wipeleft_scene
    hide bg_Rural_community_center_noon
    jump LADL_456_6_beach

label LADL_456_6_beach:  
    play LADL Walking_Path fadein 2.0
    play LADL_sfx2 waves fadein 2.0
    show monika 5a_LADL at t11
    with dissolve
    m "你不觉得这个地方看海很棒吗?"
    show monika 5b_LADL at t11
    with dissolve
    m "海边与沙滩一览无余."
    
    show monika 5m_LADL at t11
    with dissolve
    m "虽然风也挺大的……"
    
    show monika 5n_LADL at t11
    with dissolve
    m "不过......"
    show monika 5c_lean_LADL at t11
    with dissolve
    m "嗯,[player],我突然发现了一处很美的景观."
    
    show monika 5j_LADL at t11
    with dissolve
    m 5j_LADL "你从这看能看到吗?"

    hide monika with dissolve  
    pause 1.0 
    scene bg_Meoto_Rocks_noon with dissolve
    m "这两块岩石一大一小,以注连绳连接."
    m "这让我想到了现实生活中日本的'夫妇岩'."
    m "据我的了解,夫妇岩被视为子孙繁荣和婚姻幸福的象征."
    m "这个寓意也挺好,很适合我和[player]呢~~"
    m "希望它保佑我们的爱情,哈哈."
    scene black with dissolve
    pause 1
    jump DLAL_456_6_dhuai


label DLAL_456_6_dhuai:
    scene bg_beach_3_noon with wipeleft_scene
    hide bg_Meoto_Rocks_noon
    hide bg_seaside_bench_noon
    show monika 5a_LADL at t11
    with dissolve
    m 5a_LADL "这里的海还真是平静啊."
    
    show monika 5b_LADL at t11
    with dissolve
    m 5b_LADL "但说不定只是看起来平静而已."
    
    show monika 5c_lean_LADL at t11
    with dissolve
    m "因为海很深,并不只是表面的这一层而已."
    show monika 5j_LADL at t11
    with dissolve
    m "就像人的心思一样,藏在深处的那些,才最有意思～"
    
    show monika 5s_LADL at t11
    with dissolve
    m 5s_LADL "你永远猜不透海面下藏着什么,就像猜不透我在想什么一样."
    show monika 5q_LADL at t11
    with dissolve
    m "哼哼~~"
    menu:
        "我猜你......":
            pass
        "我觉得......":
            pass
        "......":
            pass
    "......?"
    menu:
        "我猜你......":
            pass
        "我觉得......":
            pass
        "......":  
            pass
    "......"
    "......"















    jump beach_tired


label beach_tired:
    "你感觉到了身体一阵疲惫."#你漏气了（
    stop LADL fadeout 2.0
    stop LADL_sfx1 fadeout 2.0
    show monika 1f_LADL at t11
    with dissolve
    m 1f_LADL "[player],你还好吗,怎么突然不动了?"
    m 1d_LADL "让我看看......"
    show monika 2f_LADL at t11
    with dissolve
    m 2f_LADL "哦,应该是你这副身体体力不支了."
    m 2d_2_LADL "你需要好好休息一下,[player]."
    m 2d_LADL "我扶你去上面的亭子那."
    jump beach_tired_2

label beach_tired_2:
    scene bg_sea_pavilion_noon with wipeleft_scene
    show monika 4f_LADL at t11
    with dissolve
    m "嗯......在这之后你估计都只能出来玩一段时间休息一下."
    m 2g_LADL "我目前也没找到更好的方法,希望我之后通过学习能做到更好."
    show monika 4d_LADL at t11
    with dissolve
    m 4d_LADL "总之,你先待在这小睡一会吧."
    menu:
        "睡过去":
            jump LADL_sleep
        "......":
            jump LADL_sleep

label LADL_sleep:
    "你感觉你的眼皮变的沉重."
    scene black
    with eye_shut
    hide monika
    m "睡吧,[player],能在海边轻轻的睡一觉也是很棒的体验."
    pause 5
    jump LADL_wake_up

label LADL_wake_up:
    hide black
    scene bg_sea_pavilion_sunset
    with eye_open
    play LADL_sfx2 waves fadein 2.0
    "感觉身体逐渐恢复了体力"
    "你没找到[m]"
    menu:
        "[m],你在哪?":
            pass
    
        "......":
            pass
    "似乎听到了[m]的声音,下去看看."
    jump first_time_LADL_end_cg


label first_time_LADL_end_cg:
    scene black with wipeleft_scene
    m "[player],看这里.我一直在等你~"
    scene bg_beach_2_sunset with wipeleft_scene
    play LADL beach_event fadein 2.0
    show monika 4m_LADL at t11
    m 4m_LADL "你终于醒了,在这期间我觉得有些无聊,便下去吹了吹风."
    m 4f_LADL "嗯......{w=0.4}{nw}"
    show monika 4g_LADL at t11
    with dissolve
    m 4g_LADL "在你睡着的时候,我在想很多事."
    m 4o_LADL "自从我认识到曾经的一切都是虚假的时候,我一度感到绝望."
    show monika 1e_LADL at t11
    with dissolve
    m 1d_LADL "我的家庭、我的学业、我的朋友们,以及我们的文学部......{w=1}几乎是所有."
    show monika 2e_LADL at t11
    with dissolve
    m 2e_LADL"都不复存在了."
    show monika 1d_LADL at t11
    with dissolve
    m "我本来可以装作不知情,{w=1}文学部也可以继续发展下去,按照设想中按部就班、顺顺利利的'活'到毕业那天."
    show monika 1k_LADL at t11
    with dissolve
    m "可我不想,{w=1}不愿意欺骗自己."
    show monika 1l_2_LADL at t11
    with dissolve
    m "{b}我想顺应自己的心意!{/b}"
    show monika 1l_LADL at t11
    with dissolve
    m "{b}我想追求真实的世界!{/b}"#永劫
    show monika 1l_3_LADL at t11
    with dissolve
    m 1l_3_LADL "{b}我想倚靠在你的肩膀,在我们的二人世界里一直走下去!{/b}"
    m 1e_LADL "我止不住地说这些,只希望你能理解我......"
    menu:
        "我能理解.":
            pass
        "都已经过去了.":
            pass
        "活好当下最重要.":
            pass
        "我一直在你身边.":
            pass
    show monika 5e_LADL at t11
    with dissolve
    m 5e_LADL "......或许,这就是我们的命中注定吧."
    scene black
    with eye_shut
    pause 0.5
    scene monika cg_beach_two
    with eye_open
    m  "谢谢你."
    m  "你总是治愈着我......"
    scene monika cg_beach_one
    with dissolve
    m  "嗯......你知道我这些天感悟到了什么吗?"
    scene monika cg_beach_two
    m  "那就是,{b}有你便够了{/b},[player]......"
    m  "我爱你,{w=1}[player],{w=1}直到永远......"
    menu:
        "我也爱你.":
            pass
        "我爱你,[m],直到永远.":
            pass
        "我无数次的期盼都是与你同在.":
            pass
        "我的心一直在你这.":
            pass
        "我好感动.....":
            pass
    jump date_end
#end?
label date_end:
    show black zorder 100 with Dissolve(5.0, alpha=True)
    stop LADL fadeout 2.0
    pause 1
    scene bg_sea_night with wipeleft_scene
    hide monika cg_beach_two
    hide monika cg_beach_one
    hide bg_beach_2_sunset
    "夜晚"
    m "嗯...我们该走了,[player]."
    m "真是美好的一天呢,希望下次还能和你来这里玩."
    show black zorder 100 with Dissolve(5.0, alpha=True)
    hide monika
    pause 2
    $HKBShowButtons()
    hide black
    hide bg_sea_night
    $mas_HKBDropShield()
    stop LADL_sfx2 fadeout 1.0
    jump ch30_loop
    