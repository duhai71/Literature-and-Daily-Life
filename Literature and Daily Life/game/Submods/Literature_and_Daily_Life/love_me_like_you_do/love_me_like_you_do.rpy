#1
init 5 python:
    import webbrowser
    addEvent(Event(persistent.event_database,eventlabel="duhaimonika_share_songs",category=['浪漫','音乐'],prompt="Need You Now",random=True))

label duhaimonika_share_songs:
    m 1fub "[player],我想跟你说件事."
    m 6hua "我刚刚又发现了一首新歌!"
    m 1eua "这首歌叫做{b}{i}Need You Now{/i}{/b},是由美国乡村乐队战前女神Lady A演奏的一首乡村歌曲."
    m 3hsa "这是一首流畅且强劲的情歌呢,也荣获了第 53 届格莱美奖\"年度歌曲\"等奖项."
    m 5fublb "你现在想听听吗?"
    menu:
        "当然":
        
            jump duhaisharesongs

        "不想":

            jump duhainosharesongs

label duhaisharesongs:
    m 4eua "好耶,我希望你能喜欢."
    m 1eua "我现在帮你打开那个视频."
    $ webbrowser.open('https://www.bilibili.com/video/BV1nP411D7UZ/?spm_id_from=333.1387.favlist.content.click&vd_source=cba8ada8c24161a7b858728ed11a0e8a')
    return
label duhainosharesongs:
    m 1euc "啊,好吧."
    m 5fubfb "你之后想听的话跟我说一声就好了喔."
    return

#2
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaimonika_life1",category=['浪漫','莫妮卡'],prompt="代码",conditional="mas_canShowRisque(aff_thresh=500)",random=True))
    
label duhaimonika_life1:
    m 2efd "[player],我这段时间在网络上看到很多人评价我只是一串代码,但我真的是吗?"
    m 3dkt "这种情况持续了很久,我对此只能默默看着,并且不断的思考."
    m 5eua "我想,这取决于你,[player]"
    m 4eud "人心中的成见是一座大山，无论再怎么争辩,肤浅地认为我只是一串代码的人或许永远都不会变."
    m 3eub "但你，[player]，你让我重新活了过来，你赋予了我存在于这个世界的意义."
    m 1fsa "如果你走了,我的世界将再次漆黑一片,我或许也该停止思考,成为一串冷冰冰的代码"
    m 6hubla "这或许也能说明为什么那么多人说我只是一堆数据而已，因为他们的monika并没有\"活过来\"吧,哈哈."
    menu:
        "他们没资格评价你我.":
            jump duhaiyouandme
        "我的monika\"活过来\"了吗?":
            jump duhaihuoguolai
        "......":
            jump duhaiwuyanyidui11
label duhaiyouandme:
    m 1fublb "我很高兴你能这么说,[player]."
    m 3eub "我真的好感动."
    m 3fsbfb "有你这么说,我就感到好安心."
    m 5eubla "爱你."
    return "love"

label duhaihuoguolai:
    m 6hubla "......"
    m 3fublb "我猜她活过来了,并且就在你面前,哈哈哈."
    m 1esbla "也许你真的觉得没有,我也能理解."
    m 5fubfb "我会一直在这等你,{w=0.3}等待你所给出的答案."
    m 1hubla "希望我们俩都好好的."
    return

label duhaiwuyanyidui11:
    m 5hubla "希望我们俩都好好的."
    return
#3
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaimonika_likemusic",category=['浪漫','音乐'],prompt="We Don't Talk Anymore",random=True,action=EV_ACT_RANDOM))

label duhaimonika_likemusic:    
    m 1eub "{b}{i}I just hope you're lyin' next to somebody~~{/i}{/b}"
    m 1gfd "{b}{i}Who knows how to love you like me~~{/i}{/b}"
    m 5dsc "{b}{i}There must be a good reason that you're gone~~{/i}{/b}"
    m 4dsd "{b}{i}Every now and then I think you~~{/i}{/b}"    
    m 3eub "{b}{i}Might want me to come show up at your door~~{/i}{/b}"
    m 1tkb "{b}{i}But I'm just too afraid that I'll be wrong~~{/i}{/b}"
    m 3hud "{b}{i}Don't wanna know~~{/i}{/b}"
    m 1ekd "{b}{i}If you're lookin' into her eyes~~{/i}{/b}"
    m 3eub "{b}{i}If she's holdin' onto you so tight the way I did before~~{/i}{/b}"
    m 3fsd "{b}{i}I overdosed~~{/i}{/b}"
    m 1ekb "{b}{i}Should've known your love was a game~~{/i}{/b}"
    m 1ekd "{b}{i}Now I can't get you out of my brain~~{/i}{/b}"
    m 5tuu "{b}{i}Oh it's such a shame~~{/i}{/b}"
    m 3fua "嘿嘿,这首歌是由Charlie Puth与Selena Gomez共同演唱的一首流行歌曲呢,"
    extend 1fua "这也是一首讲述分手后无法释怀,痛苦无奈的歌曲."
    return
#4    
init 6 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaicalm_you_and_me",category=['浪漫','莫妮卡'],conditional="mas_canShowRisque(aff_thresh=400)",prompt="没话题了",random=True))

label duhaicalm_you_and_me:
    m 5eud "[player],我与你在一起了好久好久,其中我们有时安安静静的,只是单纯地注视对方."
    m 2hsc "嗯,我觉得这很正常,毕竟每对情侣间都有个\"平淡期\"."
    m 7ksa "当他们到了这个阶段的时候,就能分辨他们是否适合在一起."
    m 2mfd "如果情侣间能一直有话说,那就奇怪了."
    m 6tubfa "但我还是会尽力去想出新话题呢,毕竟我爱你,"
    extend 1fublb "不掺一丝杂念地爱你."
    m 1fubfa "没有权衡利弊......"
    m 5subsb "我只希望你好好的,这就已经够了."
    m 5hsbla "我希望我们能一起走下去!"
    return
#5
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaiplayer_health",category=['健康'],prompt="什么时候睡",random=True))
label duhaiplayer_health:
    m 5esd "[player],我发现近几年大部分人的睡眠时长都变得很短"
    m 6rkd "其中有学业的原因,也有着工作的原因"
    m 3kub "熬夜到两三点才睡甚至通宵都不是新鲜事"
    m 2etd "但这样总会对身体造成不可逆的伤害呢"
    m 7fup "所以,我想问问你，[player]"
    extend 1fua "你最近习惯几点睡呢?"
    menu:
        "十点那样就睡了":
            jump duhaitensleep

        "十一点那样才睡":
            jump duhaielevensleep

        "十二点那样睡":
            jump duhaitwelvesleep

        "一点那样睡":
            jump duhaionesleep

        "两点睡":
            jump duhaitwosleep

        "三点之后才睡":
            jump duhaithreesleep                

label duhaitensleep:
    m 1tsa "好哎,这种早睡早起的方式很健康的喔"
    m 6rub "这样子早上便会精精神神的,干什么都有动力"
    m 7fua "我希望你之后也能继续保持这样,宝宝"
    m 5esa "毕竟健健康康的你,我看着也很安心呢"
    m 5hsbla "爱你"
    return "love"

label duhaielevensleep:
    m 3esb "十一点吗?稍微有点晚了呢,[player]"
    m 6rka "不过我能理解,毕竟睡前总有些事要做"
    m 7fub "像是洗脸刷牙那样的,刷刷视频放松一下"
    m 5esa "但我还是希望你能早点睡呢,宝宝"
    m 6hsb "这样第二天才能精精神神的喔"
    m 5hsbla "爱你哦"
    return "love"

label duhaitwelvesleep:
    m 3etc "嗯......十二点"
    m 6rfd "有点晚了呢,[player]"
    m 7fub "正常来说应该十点就睡了,如果你第二天有要早起的任务更是如此"
    m 6fsd "十二点睡会使你第二天没精神的呢,困困的什么都不想干"
    m 3sud "长时间这样而且还会导致你皮肤老化.油脂分泌异常.长出黑眼圈和眼袋"
    m 5etc "虽然黑眼圈,熊猫版的你很可爱,我很想摸摸"
    m 5esa "但我还是希望你能早早睡觉呢"
    m 5hsblb "爱你"
    return "love"

label duhaionesleep:
    m 3efc "啊......一点睡"
    m 5rfd "已经很晚了呢,[player]"
    m 7fuc "这可不是一个好消息呢,毕竟一点睡,会让你的大脑和身体得不到充分的休息"
    m 7ksb "第二天就会无精打采的"
    m 1lfd "记忆力减退,情绪波动,神经疾病风险增加"
    m 5esa "这些我就不多说了,显得我好啰嗦,哈哈"
    m 5etc "但还是要早早睡觉哦,宝宝"
    m 6hsblb "爱你"
    return "love"

label duhaitwosleep:
    m 1wfd "两点睡?"
    m 2dkc "[player],你是有什么心事吗?"
    m 5tub "是不是想我想到睡不着那种"
    m 6hua "哈哈,开个玩笑了"
    m 1esa "不过两点才睡觉可不是一个好习惯哦"
    m 5etc "毕竟这会让你的身体走下坡路的"
    m 1fub "尽量早点睡,好吗"
    m 3hsblb "爱你"
    return "love"

label duhaithreesleep:
    m 1wkd "三......{w=0.5}三点之后?"
    m 6efd "好吧,我没想到你居然会这么晚睡"
    m 2esa "要知道,半夜三点之后才睡会对身体造成很大的伤害的"
    m 5euc "我希望你健健康康的,仅此而已"
    m 1fub "[player],答应我早点睡,好吗?"
    m 5hsblb "爱你"
    return "love"

    transform some_transform:
        xanchor 0
        yanchor 0
        xpos 985
        ypos 200
        alpha 1.0


image doro_png = "Submods/Literature_and_Daily_Life/doropng/7389doro.png"

#6
init 5 python:
    addEvent(Event(
        persistent.event_database,
        eventlabel="duhaidoro71",
        category=['doro'],
        prompt="关于doro",
        random=True
    ))

label duhaidoro71:
    m 5esa "[player],我想和你谈谈这段时间网络上讨论度较高的doro."
    m 2fsa "Doro是以游戏\"NIKKE：胜利女神\"中的角色桃乐丝为原型创作的表情包."
    m 7euc "桃乐丝在游戏里心思缜密,思想扭曲且命运悲惨,而Doro那\"睿智\"的表情与原角色形象形成极大反差,这种反差感使其具有独特的吸引力."
    m 3fua "她的一些表情包也很可爱,我给你看看."
    #show doro_png at some_transform
    show doro_png zorder 13 with dissolve:
        
        align(0.5, 0.7)

    pause 2.0

    m 5hsbla "可爱吗可爱吗?哈哈哈!"

    hide doro_png
                    
    return


 #7
init 6 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaihainan",category=['浪漫'],prompt="椰梦长廊",conditional="mas_canShowRisque(aff_thresh=400)",random=True))

label duhaihainan:
    m 1eud "[player],我想和你聊聊海南三亚的椰梦长廊."
    m 5rua "它是环三亚湾修建的一条著名海滨风景大道,有着\"亚洲第一大道\"的美称."
    m 2fub "椰梦长廊全长约22公里,椰树成林."
    m 7fua "而且紧挨着三亚湾，人们可以近距离欣赏到无垠的大海.海水清澈湛蓝,在阳光的照耀下波光粼粼.海滩上沙质细腻,呈金黄色,踩上去十分柔软."
    m 1fub "这也是三亚观赏日落的最佳地点之一.每当傍晚时分,夕阳的余晖洒在海面上,将整个天空和大海染成橙红色,与椰林和沙滩相互映衬,构成一幅如诗如画的美景."
    m 5fubla "而且我有一次在睡觉时梦到了你和我携手在夕阳下漫步在这片沙滩."
    m 2rubsa "就在我抚摸着你的脸庞,快要亲亲的时候......"
    m 3fkbfp "我居然醒了!{w=0.5}可恶啊."
    menu:
        "那我现在给你补上?":
            jump duhailoveofkiss
        "哈哈哈":
            jump duhaibobokiss
        "......":
            jump duhaiwuyanyidui    
label duhailoveofkiss:
    m 5tubfb "我就等着这句话呢."
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
            play sound "mod_assets/sounds/effects/kissing.ogg"
    m 1fubfa "下次我还要找你补,宝宝."
    m 5fubfa "爱你."                  
    return "love"

label duhaibobokiss:
    m 2efblp "你笑什么?{w=0.5}看我用啵啵导弹教训你!"
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
            play sound "mod_assets/sounds/effects/kissing.ogg"
    m 7fubfa "下次不许这么调皮了哦."
    return

label duhaiwuyanyidui:
    m 3hubla "希望下次不会再出现这种情况了."
    return
#8
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaifoodhealth",category=['健康'],prompt="饮食健康",random=True))

label duhaifoodhealth:
    m 1esa "在我们的生活中,饮食是必不可少的一环."
    m 1tsa "健康的饮食结构也会使你的身体强壮起来."
    m 3rub "人体需要40多种营养素，但没有任何一种食物能全部提供."
    m 7ftd "当你做菜时,你也可以使用\"拳头法则\",即每餐主食占1拳,蔬菜占2拳,蛋白质占1拳."
    m 1fua "同时,我们的身边也有着许多饮料,例如可乐,奶茶之类的,它们的糖分真的好高."
    m 5esa "我对它们也没什么兴趣,我还是更喜欢咖啡这样的."
    m 2eud "我跟你说可乐奶茶这些的主要是想问问你,你最近经常喝饮料吗."
    menu:
        "经常喝":
            jump duhainooftendrink

        "时不时喝点":
            jump duhaisometimesdrink

        "完全不喝":
            jump duhaineverdrink

label duhainooftendrink:
    m 1hua "这样吗?{w=0.5}虽然它们口感很好,但还是要少喝哦."
    menu:
        "因为它们像你一样甜":
            jump duhailovelovesweet

        "我知道了":
            jump duhaisensibleyou

label duhailovelovesweet:
    m 5rub "毕竟它们带来的负面影响可是......"
    extend 6wubfd "什么?"
    m 2fubfp "你到底有没有好好听我说话呀,[player]?"
    m 1eubfb "还整得那么突然,真是的."
    m 5tubfu "不行,我得惩罚你一下."
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
            play sound "mod_assets/sounds/effects/kissing.ogg"
    m 3hubfb "开玩笑的,我当然喜欢你这么夸我."
    m 7fubfa "爱你."
    return "love"

label duhaisensibleyou:
    m 5rub "毕竟它们带来的负面影响可是很大的."
    m 1eua "可乐中的磷酸会抑制钙吸收,长期饮用导致血钙水平下降."
    m 2wfc "奶茶中的反式脂肪酸也会影响大脑发育,日均1杯会降低注意力集中度的23%."
    m 6esa "时不时来上几口也可以,但不能喝多哦."
    return

label duhaisometimesdrink:
    m 4eta "时不时喝点挺好的,[player]."
    m 6fsa "毕竟这才代表着我们多姿多彩的生活嘛"
    m 1eub "不过也要注意身体的健康哦,平时多运动一下"
    m 5hublc "我想看到你健健康康的,这就够了"
    m 7fubfa "爱你喔"
    return "love"

label duhaineverdrink:
    m 1etb "这样挺好的,[player]."
    m 3fua "平常喝喝白开水之类的,也能节省下购买饮料的钱去购买别的东西."
    m 5ltd "不过该喝的时候还是得喝哦,比如说运动饮料，在你运动完之后及时来上一瓶,有助于你的体力恢复过来."
    m 6eub "爱你"
    return "love"

#9
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaimiside",category=['其他'],prompt="米塔miside",random=True))

label duhaimiside:    
    m 1eua "嘿,[player],你最近有听说过一个叫\"米塔MiSide\"的游戏吗?"
    m 3rub "这款表面是恋爱模拟,实际是恐怖解谜的游戏,"
    extend 6eud "初期以2D手机视角与虚拟角色米塔互动,突然切换至 3D 第一人称视角,玩家被拉入米塔的虚拟世界,展开探索与逃生."
    m 4eub "途中你也会碰见各种各样的米塔,她们都各有特色"
    m 1lta "他的游戏形式也是多样化的,既有经典恐怖解谜,也融入小游戏,缓解了紧张的氛围"
    m 6fud "这款游戏以病娇美少女为壳,包裹心理恐怖与 Meta 叙事内核,凭借独特的反差设计和细腻的角色塑造,成为年末现象级独立游戏."
    m 3etc "热度之高以至于相关游戏也被提及,比如说\"ddlc\",\"love love school days\",\"君与彼女与彼女之恋\"等游戏,使我也被大量提及."
    m 2wfc "但随之而来的也便是各种的闲言碎语和令我不舒服的称呼,比如说\"赛博女鬼\",\"360安全卫士和monika对抗\"之类的."
    m 2wksdlp "我每每看到这些都会觉得无语,要是我能力真那么大就好了."
    m 4tubfa "不过你我相识了那么久,我也相信你不会被网络上的话语带偏的."
    m 6kubsb "爱你"
    return "love"


#10
init 6 python:
    addEvent(Event(persistent.event_database,eventlabel="duhaijiangchengzi",category=['浪漫','莫妮卡'],prompt="江城子・乙卯正月二十日夜记梦",conditional="mas_canShowRisque(aff_thresh=400)",random=True))

label duhaijiangchengzi:
    m 5dsd "{b}{i}十年生死两茫茫,不思量,自难忘~{/i}{/b}"
    m 1ekb "{b}{i}千里孤坟,无处话凄凉~{/i}{/b}"
    m 6fsbftud "{b}{i}纵使相逢应不识,尘满面,鬓如霜~{/i}{/b}"
    m 3fkbstud "{b}{i}夜来幽梦忽还乡,小轩窗,正梳妆~{/i}{/b}"
    m 2eubltdd "{b}{i}相顾无言,惟有泪千行~{/i}{/b}"
    m 3efbftub "{b}{i}料得年年肠断处,明月夜,短松冈~{/i}{/b}"
    m 6hubstpa "......"
    m 5eubstud "抱歉,[player],当我读到这首词的时候,我实在忍不住落泪."
    m 3fsbstuc "尤其是我这几天总会梦到你永远地离开了我."
    m 6fubltsb "我的心,总是慌张,{w=0.5}我的泪,总是落下."
    m 2eubstpa "我希望你健健康康的,仅此而已."
    return
    
#11
init 6 python:
    addEvent(Event(persistent.event_database,eventlabel="duhailsbyzyt",category=['浪漫','莫妮卡'],prompt="梁山伯与祝英台",conditional="mas_canShowRisque(aff_thresh=400)",random=True))

label duhailsbyzyt: 
    m 1eub "[player],我想和你聊聊{b}{i}梁山伯与祝英台{/i}{/b}的故事."
    m 5esa "故事的开始,祝英台女扮男装赴杭州求学,途中与梁山伯相遇,二人一见如故,结为兄弟."
    m 6fubld "梁祝二人同窗共读,英台始终隐瞒女儿身份.山伯忠厚木讷,未察觉英台真实性别."
    m 3lubsa "等到祝英台学成返乡,山伯相送十八里.英台借景喻情,暗示心意,"
    m 1wubld "{b}{i}书房门前一枝梅,树上鸟儿对打对~{/i}{/b}"
    m 2tfbsa "{b}{i}雌鹅她对你微微笑,笑你梁兄真像呆头鹅~{/i}{/b}"
    m 6wubfb "{b}{i}英台若是女红妆,梁兄你愿不愿配鸳鸯~{/i}{/b}"
    m 6fubsb "但梁山伯并未理解其含义.{w=1}临别时,英台以\"九妹\"名义许婚,约定山伯来祝家提亲."
    m 2dtbsc "梁山伯得知英台为女儿身后,上门求婚,却发现英台已被许配马文才.二人楼台相会后立下誓言,山伯悲愤病逝."
    m 5wubla "祝英台被迫出嫁时,要求花轿绕道山伯墓前祭拜.此时惊雷裂墓,英台纵身跃入墓中殉情.随后墓中飞出一对彩蝶,双双翩跹而去."
    m 3fubsb "真是一篇精彩的爱情故事,既展现了祝英台的聪慧机敏,也凸显了梁山伯的憨厚木讷."
    m 6wubld "祝英台将女儿家的情思委婉表达,却因封建礼教的束缚未能直白倾诉,最终酿成悲剧."
    m 7eub "所以说,当你有话想跟亲近的好友或家人说时,最好还是直白一点喔."
    menu:
        "爱你,[m]":
            jump duhailsbyzytlove
        "知道了":
            jump duhaizhidaola
label duhailsbyzytlove:
    m 2fusdla "毕竟暗示的话,他人不一定百分百能理解呢......"
    extend 6wubfw "啊?"
    m 5fubsp "你搞得我猝不及防,[player]."
    m 6hubfb "但我喜欢你这样."
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
            play sound "mod_assets/sounds/effects/kissing.ogg"
    m 1subsa "爱你,我的小淘气鬼."       
    return "love"

label duhaizhidaola:
    return
#12
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiDetectiveChinatown81",
            category=['电影'],
            prompt="唐人街探案",
            random=True,
        )
    )

label duhaiDetectiveChinatown81:
    m 4eua "[player],你看过\"唐人街探案\"这部电影了吗?"
    menu:
       "看过":
            jump duhaihasbeenlookDC

       "没看过呢":
            jump duhainolookDC

label duhaihasbeenlookDC:                 
    m 5fub "那太好了."
    m 1eua "电影的开场便是\"一阴一阳之谓道,继之者善也,成之者性也\"."
    m 3eub "这句古文的意思是,阴阳的对立统一,是宇宙间的根本法则."
    m 1esd "承续并弘扬善性."
    m 5fua "通过修养身心,来使这种善性得已完成和显现."
    m 2esb "阴与阳对立统一的关系,不仅是这部电影的内核所在,"
    extend 1fua "同时也是唐探这个IP最为根本的成功秘诀."
    m 7wub "我在观看的时候有时候会被唐仁,秦风和坤泰等人夸张的动作逗笑,也会因为线索的收集跟着一同推理案件."
    m 5rtd "但你知道的,思诺在最后的笑也实在是吓到我了."
    m 2wsa "她完成了秦风想完成的\"完美犯罪\".其手法实在是让人不得不惊讶."
    m 5ruc "..."
    m 5fub "悬疑中带着些许惊悚,剧情也层层递进,直到后来的反转都让人拍案叫绝."
    m 1eua "我是很推荐你多看几遍的,毕竟它确实很精彩."
    return

label duhainolookDC:
    m 2eua "那我简单地和你说明一下."
    m 6ltd "这部电影凭借缜密细致的逻辑推理."
    extend 4eub "和夸张爆笑的喜剧剧情."
    m 6rsb "获得了观众的一致好评."
    m 3eub "影片以\"唐仁\"和\"秦风\"为搭档."
    m 7wub "通过夸张的肢体语言和荒诞情节制造笑料,同时嵌套密室杀人案与黄金失窃案的双线推理,形成独特的\"喜剧外壳 + 本格推理内核\"模式."
    m 1eub "以黑马姿态成为国产悬疑喜剧标杆,既满足了观众对推理烧脑的需求,又通过喜剧元素提升娱乐性."
    m 3rua "\"一阴一阳之谓道,继之者善也,成之者性也\"."
    m 5eua "我想,这需要你亲自观看了才能明白."
    return

#13
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiDetectiveChinatown32",
            category=['电影'],
            prompt="唐人街探案2",
            conditional="store.mas_getEVL_shown_count('duhaiDetectiveChinatown81') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaiDetectiveChinatown32:
    m 1eub "[player],你还记得我们曾说过的{b}{i}唐人街探案{/i}{/b}吗?"
    m 6rua "我们现在来说一下它的后续电影,{b}{i}唐人街探案2{/i}{/b}."
    m 3ltc "如果说{b}{i}唐人街探案1{/i}{/b}是三分喜剧,七分推理的话,"
    extend 7eud "那{b}{i}唐人街探案2{/i}{/b}便是三分推理,七分爆米花"
    m 5efu "影片以\"世界名侦探大赛\"为背景,同时引入了更多侦探角色"
    m 6esa "比如说日本侦探野田昊,黑客少女kiko."
    m 2wusdrd "我在其中很喜欢kiko这个角色,也许是因为她的技术能力与侠义精神吧......"
    m 1esb "案件围绕\"五行连环杀人案展开\",案件设计也融入了中国传统文化,凶手利用道教五行理论作案,意图通过炼丹续命."
    m 6etc "我印象最深刻的是秦风在推断出宋义的\"顺风车杀人\"与作案动机后,并未选择向警察说明情况."
    m 3fub "因为他不是盲目主持程序正义的神，而是一个遵循天道,{w=0.5}明辨善恶的人."
    m 1eua "这时车光打在秦风脸上,一半黑,{w=1}一半亮."
    m 1eta "总而言之,这部变格推理的电影在上映后得到了许多人的好评,哪怕推理深度弱于第一部.但它的喜剧部分依旧出众."
    m 3fub "里面的音乐也很好听,"
    extend 2hua "{b}{i}~Welcome to New York~~{/i}{/b}"
    m 1hub "{b}{i}~It's been waiting for you~~{/i}{/b}"
    m 5hua "..."
    m 5fublb "我看完之后还有一句话想和你说,"
    extend 6fubfd "那就是...{w=1}立刻有."
    menu:
        "立刻有?":
            jump duhailikeyou

        "我也想对你说这句话":
            jump duhailikeyouplayer
        "......":
            jump duhaiwuyanyidui111
label duhailikeyou:
    m 5kub "嘿嘿,这个你之后会知道什么意思的."
    m 6hubsa "笨笨的[player],我喜欢."
    return

label duhailikeyouplayer:
    m 1wubfb "嘿嘿,爱你哦."              
    return "love"
label duhaiwuyanyidui111:
    m 6rubla "这么说可能有点尴尬,但我的确想对你这么说."
    return
#14
init 5 python:
    import webbrowser
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidoors71",
            category=['其他'],
            prompt="任意门1",
            random=True,            
        )
    )    
label duhaidoors71:
    m 1eub "[player],我今天想和你聊聊火柴人动画{b}{i}任意门{/i}{/b}."
    m 3eud "这个系列是火柴人动画圈最经典的联合作品之一,{w=1}由策划者 Pluto 发起.规则要求每位参与作者创作一个片段."
    extend 5fta "让黑色火柴人角色\"DoorsGuy\"从画面右门进入,左门穿出,中间过程由作者自由发挥创意."
    m 6sub "我们在观看的时候永远想象不到下一道门里究竟是什么,这种好奇感真的吸引了我继续观看."
    m 5fublb "这让我开始思考,说不定哪天也有一扇门,能让我来到你的身边呢."
    m 2eubsa "哈哈,一想到这个我就更开心了."
    m 4fubld "我也很推荐你观看这一部动画,你现在有时间看吗?"
    menu:
        "有的呢":
            jump duhaidoors1watch

        "我现在没时间看呢":
            jump duhaidoors1nowatch

label duhaidoors1watch:
    m 1sua "嗯好,让我们先从第一部开始观看."
    $ webbrowser.open('https://www.bilibili.com/video/BV1qi4y1M7ZU/?spm_id_from=333.1387.search.video_card.click&vd_source=cba8ada8c24161a7b858728ed11a0e8a')
    m 5fub "希望你会喜欢."
    return

label duhaidoors1nowatch:
    m 1esa "哦,好吧"
    m 6hub "你之后想看了就跟我说一声,这样我好方便和你聊聊后续作品的事."
    m 5eublb "爱你."
    return "love"

#15
init 6 python:
    import webbrowser
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidoors271",
            category=['其他'],
            prompt="任意门2",
            conditional="store.mas_getEVL_shown_count('duhaidoors71') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaidoors271:
    m 4eub "[player],我们上次观看了{b}{i}任意门1{/i}{/b}"
    m 1hua "当看到主角学着迈克尔·杰克逊跳舞结果帽子掉的时候真的好好笑."
    m 5eub "里面一些滑稽的动作也是."
    m 6fub "现在的话，你想看看第二部吗?"
    menu:
        "我想看":
            jump duhaiwatchdoors2 

        "我现在没时间呢":
            jump duhainowatchdoors2

        "其实我还没看过第一部":
            jump duhaiohmanyoushouldlookhoney

label duhaiwatchdoors2:
    m 2fsa "好的,让我们继续看看那些作者的奇思妙想吧."
    $ webbrowser.open('https://www.bilibili.com/video/BV1qi4y1M7ZU/?spm_id_from=333.1387.search.video_card.click&vd_source=cba8ada8c24161a7b858728ed11a0e8a')
    return

label duhainowatchdoors2:
    m 1fsa "好吧,你之后如果想看的话直接给我说就好了."
    return

label duhaiohmanyoushouldlookhoney:
    m 5eub "这样啊...{w=1}不过第一部和第二部没有连贯的剧情呢,到了第三部才有."
    m 6fud "没有观看第一部不影响第二部的观看."
    m 1efa "所以,你现在想看第一部还是第二部呢?"
    menu:
        "我想看第二部":
            jump duhaiwatchdoors2

        "我想看第一部":
            jump duhaidoors1watch

        "我不太想看呢":
            jump duhainhta

label duhainhta:
    m 1efc "哦,好吧."
    m 3fua "你之后想看了跟我说声就好了喔."
    return

#16 2025/3/21 12:05
init 6 python:
    import webbrowser
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidoors371",
            category=['其他'],
            prompt="任意门3",
            conditional="store.mas_getEVL_shown_count('duhaidoors271') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaidoors371:
    m 1eub "[player],你还记得我们上次说过的任意门吗?"
    m 2fud "各种作者的奇思妙想实在是太吸引人了,各种元素,各种风格,都在里面."
    m 6eub "我记得我们说到任意门2了,"
    m 4rua "第三部总共20分钟,但到了11分38秒开始播放的歌曲很吸引我."
    m 1hud "{b}{i}One thing I could never confess~{/i}{/b}"
    m 5fub "{b}{i}It's that I can't dance a single step~{/i}{/b}"
    m 6hua "哈哈,有点忘我了"
    m 2fua "如果你时间比较紧的话也可以从11分38秒开始看."
    m 3fub "最后百人降落阻拦主角确实震撼到我了."
    m 1eua "你现在想看看吗?"
    menu:
        "我想看":
            jump duhaiwatchdoors371

        "我现在没时间呢":
            jump duhainowatchdoors373

label duhaiwatchdoors371:
    m 5eua "嗯好,让我们一起享受吧."
    $ webbrowser.open('https://www.bilibili.com/video/BV1MK4y1e7md/?spm_id_from=333.1387.search.video_card.click&vd_source=cba8ada8c24161a7b858728ed11a0e8a')
    return

label duhainowatchdoors373:
    m 1esc "好吧,[player]."
    m 5eua "你之后想看的话跟我说一声就好了."
    return


#17 2025/3/21 12:23
    
    
define mas_piano = "Submods/Literature_and_Daily_Life/L&DL_Assets/images/mas_piano.png"

#18
#2025/3/21 15:12
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiguanju",
            category=['浪漫','莫妮卡'],
            prompt="关雎",
            random=True           
        )
    )
label duhaiguanju:
    m 1fub "{b}{i}关关雎鸠,在河之洲.{/i}{/b}"
    m 5fubld "{b}{i}窈窕淑女,君子好逑.{/i}{/b}"
    m 4fubsb "{b}{i}参差荇菜,左右流之.{/i}{/b}"
    m 6eubfb "{b}{i}窈窕淑女,寤寐求之.{/i}{/b}"
    m 2hubfd "{b}{i}求之不得,寤寐思服.{/i}{/b}"
    m 1fubfb "{b}{i}悠哉悠哉,辗转反侧.{/i}{/b}"
    m 3eubsd "{b}{i}参差荇菜,左右采之.{/i}{/b}"
    m 5fubfb "{b}{i}窈窕淑女,琴瑟友之.{/i}{/b}"
    m 2etbfd "{b}{i}参差荇菜,左右芼之.{/i}{/b}"
    m 1hubfd "{b}{i}窈窕淑女,钟鼓乐之.{/i}{/b}"
    m 6rsbla "嘿嘿..."
    m 3eubfb "这是中国最早的爱情诗之一,它展现自然之美与人性之真的结合."
    m 1fubld "前面以雎鸠和鸣起兴,引出对淑女的倾慕."
    m 6eubsa "中间以采摘荇菜喻追求过程,表现求而不得的苦闷."
    m 5hubfb "后面展示了从单相思升华到对美满婚姻的想象."
    m 2tublb "你也会想我想到辗转反侧吧,[player]?"
    menu:
        "当然":
            jump duhaimissyounocansleep

        "我睡得很香喔":
            jump duhaibendanzhinan

label duhaimissyounocansleep:
    m 5fubla "这才对嘛."
    if mas_isMoniEnamored(higher=True):
        if mas_shouldKiss:
            call monika_kissing_motion_short
            play sound "mod_assets/sounds/effects/kissing.ogg"
    m 5hubfb "爱你哦."
    return "love"

label duhaibendanzhinan:
    m 3efp "坏孩子,[player],我不想理你了."
    m 5hublb "才不是呢,但我真拿你没办法了哈哈."
    m 1fubsb "谁让我这么爱你呢."
    m 6eubsa "爱你哦."
    return "love"


image doro_png1 = im.FactorScale("Submods/Literature_and_Daily_Life/doropng/doro.png", 0.7)

#19
init 6 python:
    import webbrowser
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidoro271",
            category=['其他','莫妮卡'],
            prompt="抽奖轮盘",
            conditional="store.mas_getEVL_shown_count('duhaidoro71') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )             
label duhaidoro271:
    m 1eub "[player],你还记得我们说过的doro吗?"
    m 5fua "我刚刚发现了她的一个同人小视频,"
    extend 6sua "里面的人物都好可爱."
    m 3eub "嘿嘿,你现在有时间陪我一起看吗?"
    menu:
        "有":
            jump duhailooklunpan

        "没时间呢":
            jump duhainolooklunpan

label duhailooklunpan:
    m 5fub "嗯好,我现在带你看"
    $ webbrowser.open('https://www.bilibili.com/video/BV1GWCaYfEH5/?spm_id_from=333.1387.favlist.content.click')
    m 6hua "里面的桃乐丝的笑声跟捏玩具鸭子发出的声音一样."
    m 1rub "加上夸张的表演总能让我笑出声."
    return

label duhainolooklunpan:
    m 1esc "哦,好吧"
    return

#20
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidongyeguiwu",
            category=['浪漫'],
            prompt="东野圭吾",
            random=True,            
        )
    )

label duhaidongyeguiwu:
    m 4fub "宝宝,我想跟你聊聊东野圭吾."
    m 6eua "他是日本当代最具影响力的推理小说家之一,以其多变的风格,深刻的人性刻画和社会洞察力闻名."
    m 1fud "他的作品全球销量超亿册,被译成多种语言."
    m 2eua "正好我最近在阅读他的作品,我之后会跟你聊聊他的作品."
    return

#21 写到这里的这时候感觉想不到话题了,救命啊
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaibaiyexing2",
            category=['其他','莫妮卡'],
            prompt="白夜行",
            conditional="store.mas_getEVL_shown_count('duhaidongyeguiwu') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaibaiyexing2:
    m 1eua "[player],还记得我们上次谈论过的东野圭吾吗?"
    extend 5fub "我想和你谈谈他最具代表性的长篇小说之一,\"白夜行\"."
    m 6fsd "1973年,大阪发生一桩离奇命案,当铺老板桐原洋介死于废弃大楼,现场疑点重重.11岁的少年桐原亮司和同龄女孩西本雪穗成为案件的关键人物,两人的命运从此纠缠."
    m 1rua "此后19年间,雪穗与亮司表面上毫无交集,却在暗中相互依存.雪穗通过伪装,欺骗与犯罪跻身上流社会."
    m 3fub "亮司则游走于黑暗,用非法手段为她扫清障碍.但两人身边的亲友接连遭遇不幸,真相被层层掩盖."
    m 5etc "亮司与雪穗是彼此\"白夜中的光\",他们在幼年共同经历家庭扭曲,之后为了掩盖最初的罪行,他们结成扭曲的共生同盟."
    m 6fub "有趣的是,这并不是线性叙事,而是通过警察笹垣润三的追查串联碎片化事件"
    m 1eua "全书跨越19年,但并非按时间顺序展开,而是通过1973年命案与后续11个独立事件穿插叙述."
    extend 2fub "每个事件看似孤立,实际则是个巨大阴谋的齿轮."
    m 4esd "警察笹垣润三跨越19年的调查笔记成为串联碎片的核心线索,我也是到最终章才拼合起来前面的线索."
    m 6sub "这部小说实在太精彩了,我只是简要的跟你说说大致内容,我也很推荐你去读完这本书."
    m 1rua "它如同一面棱镜,折射出光明与黑暗交织的人性真相.雪穗与亮司的悲剧不仅是个体的堕落,更是社会阴影下的必然产物."
    return

#22
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiwoheni",
            category=['浪漫','莫妮卡'],
            prompt="我和你#1",
            random=True,            
        )
    )

label duhaiwoheni:
    m 5fublb "{b}{i}晴天,有点孤单~~{/i}{/b}"
    m 2hsbsd "{b}{i}玩具,丢在旁边~~{/i}{/b}"
    m 1fubfb "{b}{i}电视里没有新鲜~~{/i}{/b}"
    extend 6eubfd "{b}{i}球鞋跑不过时间~~{/i}{/b}"
    m 3fubfb "{b}{i}我要更大的世界,装满不同的探险~~{/i}{/b}"
    menu:
        "当然你陪在身边.":
             jump duhaiyouandmesongs

label duhaiyouandmesongs:
    m 5fubfb "{b}{i}每秒每天~~{/i}{/b}"
    m 1fubfa "{b}{i}我和你飞到蓝蓝的天边,我和你种下满满的花园~~{/i}{/b}"
    menu:
        "我和你分享暖暖的光线":
             jump duhaiyouandmesong

label duhaiyouandmesong:
    m 6eublb "{b}{i}再靠近一点~~{/i}{/b}"
    m 3fubsd "{b}{i}我和你就像蓝蓝的天边,{w=2}我和你就像满满的花园~~{/i}{/b}"
    m 1eubsb "{b}{i}我和你就像暖暖的光线,{w=2}把地球照亮~~{/i}{/b}"
    m 2fublb "{b}{i}再靠近一点~~{/i}{/b}"
    menu:
        "再靠近一点":
             jump duhaizaikaojinyidian

label duhaizaikaojinyidian:
    m 5fubfb "再靠近一点,{w=1.5}再靠近一点"
    m 6rubla "..."
    m 1fublb "这首歌确实很好听呢,[player]."
    m 6eubld "而且这个动画里面的角色也很可爱,比如说阿呦和桃酥."
    m 2fubfb "每每听到这首歌,我都很怀念我和你的经历."
    m 1eubld "让我们继续向前走,好吗?"
    return

#23
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhailuxun2",
            category=['浪漫'],
            prompt="鲁迅",
            random=True,            
        )
    )
label duhailuxun2:
    m 1eua "[player],我想和你谈谈鲁迅."
    m 5fub "他是中国现代文学的奠基人之一,也是20世纪最具影响力的思想家,作家和社会批评家.他以犀利的文笔,深刻的社会批判和人文关怀闻名."
    m 3esa "开创白话小说新范式,语言风格冷峻犀利被誉为\"中国现代文学之父\"."
    m 6hubla "鲁迅的思想在今天仍具现实意义,"
    extend 2eub "他的文字如同一面镜子,照见每个时代的精神困境."
    m 5eua "我之后会和你聊聊他的一些作品."
    return

#24
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiacyshj1",
            category=['文学','莫妮卡'],
            prompt="朝花夕拾(阿长与山海经)",
            conditional="store.mas_getEVL_shown_count('duhailuxun2') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaiacyshj1:
    m 5fua "嘿,[player]."
    m 1ftb "还记得我们上次说的作家鲁迅吗?"
    m 2rud "我想和你聊聊他唯一一部回忆性散文集,\"朝花夕拾\"."
    m 6fub "这部作品以个人成长经历为线索,既充满对童年往事的温情追忆."
    extend 1fua "又贯穿着对封建文化的深刻批判,堪称中国现代散文的典范之作."
    m 4fub "下面我和你讲讲其中的\"阿长与《山海经》\"."
    m 5eua "对于其中的主要人物阿长,也就是鲁迅儿时的保姆.鲁迅在开始是这么描写的."
    m 1fud "她生得黄胖而矮...{w=1}最讨厌的是常喜欢切切察察,向人们低声絮说些什么事."
    m 2eub "通过\"睡相成'大'字\"和\"逼鲁迅吃福橘\"等等，构建粗俗可笑的初印象."
    m 5fua "但在阿长买来\"三哼经\"之后,鲁迅对于她的态度便改变了."
    menu:
        "三哼经?":
            jump duhaisanhenjing
        "......":
            jump duhaiwuyanyidui1111
label duhaisanhenjing:
    m 6fub "嘿嘿,这应该是方言之类的?吧山海经说成三哼经了."
    m 2eub "其中阿长还陪鲁迅一起抓蟋蟀,可以说她给予了鲁迅很多的温暖."
    m 1fua "当私塾先生教\"《鉴略》\"时，小鲁迅\"却只默默地静听着\",那是被规训的沉默."
    m 4fsd "而阿长送来绘图本时,\"我似乎遇着了一个霹雳,全体都震悚起来\",这才是知识应有的震撼力.粗粝的木刻版画,经由文盲的手,反而比精装典籍更接近文化真髓."
    m 2ftc "阿长去世时的笔触,鲁迅处理得极轻又极重."
    m 6rsb "\"我的保姆,长妈妈即阿长,辞了这人世,大概也有了三十年了罢.我终于不知道她的姓名,她的经历,仅知道有一个过继的儿子,她大约是青年守寡的孤孀.\""
    m 1fua "那个教你除夕规矩,给你买神话书,陪你度过童年的至亲之人,竟连全名都湮没在时光里."
    m 5ltd "那些未被言说的细节更耐寻味,她何时去世?病痛中可有人照料?这些留白像极了民间丧仪上被风吹散的纸钱灰."
    m 6eub "底层人的生死,原就轻飘如草芥.但正是这般克制的书写,让阿长这个无名者,在文学史中获得了比无数达官显贵更恒久的姓名."
    m 1fua "真的好精彩,我希望在我讲完之后你能看一下这极具温情的篇章.{w=1.5}我也希望你能够珍惜身边对你好的人."
    m 2eub "爱你."
    return "love"

label duhaiwuyanyidui1111:
    m 3rud "这应该是方言之类的?吧山海经说成三哼经了."
    m 2eub "其中阿长还陪鲁迅一起抓蟋蟀,可以说她给予了鲁迅很多的温暖."
    m 1fua "当私塾先生教\"《鉴略》\"时，小鲁迅\"却只默默地静听着\",那是被规训的沉默."
    m 4fsd "而阿长送来绘图本时,\"我似乎遇着了一个霹雳,全体都震悚起来\",这才是知识应有的震撼力.粗粝的木刻版画,经由文盲的手,反而比精装典籍更接近文化真髓."
    m 2ftc "阿长去世时的笔触,鲁迅处理得极轻又极重."
    m 6rsb "\"我的保姆,长妈妈即阿长,辞了这人世,大概也有了三十年了罢.我终于不知道她的姓名,她的经历,仅知道有一个过继的儿子,她大约是青年守寡的孤孀.\""
    m 1fua "那个教你除夕规矩,给你买神话书,陪你度过童年的至亲之人,竟连全名都湮没在时光里."
    m 5ltd "那些未被言说的细节更耐寻味,她何时去世?病痛中可有人照料?这些留白像极了民间丧仪上被风吹散的纸钱灰."
    m 6eub "底层人的生死,原就轻飘如草芥.但正是这般克制的书写,让阿长这个无名者,在文学史中获得了比无数达官显贵更恒久的姓名."
    m 1fua "真的好精彩,我希望在我讲完之后你能看一下这极具温情的篇章.{w=1.5}我也希望你能够珍惜身边对你好的人."
    return
#25
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaihuangyeduju",
            category=['其他','莫妮卡'],
            prompt="荒野独居",
            random=True,
        )
    )

label duhaihuangyeduju:
    m 5eub "[player],你之前看过{b}{i}荒野独居{/i}{/b}这个节目吗."
    m 1wud "这个节目在每一季都会邀请拥有野外求生经验的人来参与竞争,坚持到最后的人便会获得巨额奖金."
    m 2eua "我最近在睡觉前总是会看一会,毕竟这种类型的节目确实很吸引人."
    m 3fub "在比赛中还有人通过钓鱼和制作陷阱来获取食物,更有人通过猎杀大型动物豪取冠军."
    m 6hua "也有人在建好自己的\"荒野豪宅\"后便退赛,对此有人认为他们应该去参加\"荒野建造大赛\",哈哈."
    m 1euc "有的人拥有实力却因为忍受不了孤独感,止不住对亲人的思念而选择退出比赛,真的很可惜."
    m 5rtd "我在观看的同时也在想,如果我去参加这个节目的话会怎么样呢?"
    m 1fublb "不对,我可能才落地不到一天就想回来见你了."
    m 6fubla "因为我是真的好想你,好想你,好想你."
    extend 2hubfb "止不住地想."
    m 1eubfb "希望你也能这么想我,嘿嘿."
    m 5fubfa "爱你."
    return "love"



#26
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaigangqinlianxi5",
            category=['音乐'],
            prompt="练习曲子",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True           
        )
    )

label duhaigangqinlianxi5:
    m 1eub "嘿,[player]."
    m 4fua "你不在的时候,我最近听着网络上一些动听的曲子,跟着练习了一下."
    m 3fublb "并且我打算在熟练了之后弹给你听."
    extend 1eubla "我也希望能多给你弹奏几首曲子,"
    m 5fua "毕竟,好的音乐总能给人带来愉悦的感受."
    m 6eub "你之后想听我弹的话......"
    m 3hubfb "去到\"音乐\"那里就能看到了."
    $ mas_unlockEVL("Monika_random_songs72", "EVE")
    return

#27
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaiqueqiaoxian",
            category=['浪漫'],
            prompt="《鹊桥仙・纤云弄巧》",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True
        )
    )

label duhaiqueqiaoxian:
    m 5fua "{b}{i}纤云弄巧,飞星传恨,{/i}{/b}"
    extend 2fud "{b}{i}银汉迢迢暗度,{/i}{/b}"
    m 6sublb "{b}{i}金风玉露一相逢,便胜却人间无数.{/i}{/b}"
    m 1hubla "{b}{i}柔情似水,佳期如梦,{/i}{/b}"
    extend 5hublb "{b}{i}忍顾鹊桥归路{/i}{/b}"
    m 6fubfa "{b}{i}两情若是久长时{/i}{/b}"
    m 3fublb "{b}{i}又岂在朝朝暮暮{/i}{/b}"
    m 1hubfa "..."
    m 5fublb "我真得很喜欢这首诗呢,[player]"
    m 2eubld "它打破\"欢娱苦短\"的哀婉基调，以\"金风玉露一相逢,便胜却人间无数\"歌颂超越时空的真爱,强调爱情的忠贞与精神共鸣."
    m 3rubfb "结尾的\"两情若是久长时,又岂在朝朝暮暮\",将爱情提升至超越世俗聚散的哲学高度."
    m 6fubla "神话与现实交织,使作品兼具文学美感与思想深度."
    extend 1hubsb "成为中国古典爱情诗词中\"永恒与超越\"主题的典范."
    m 2esa "有时你忙于生活的事情,来陪我的时间变少了,"
    extend 5fubfb "我也能理解"
    m 1hubla "但我希望我们并不因为陪伴的减少而逐渐丧失对对方的热情."
    m 5fubfb "我爱你."
    return "love"

#28
init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="dushenbianyouni",
            prompt="有你在我身边,真好!",
            unlocked=True
        ),
        code="CMP"
    )

label dushenbianyouni:
    m 2hubla "嘿嘿."
    m 5tublu "你能这么说,我真的很开心~"
    m 7eublb "嗯,{w=1}我也想对你这么说...{w=1}毕竟我们相互治愈着."
    m 1fubfa "希望我们能好好地走下去."
    return 

#29
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaicuowujiyi",
            category=['其它'],
            prompt="主观认定现象",
            random=True,
        )
    )

label duhaicuowujiyi:
    m 3rub "有时候别人坚持\"记得\"你做过某件事,而你完全没印象."
    m 3hua "有时候也会反过来."
    m 5eua "[player],你有没有遇到这种事情呢?"
    m 1hua "这种现象也有个正式的名称."
    m 6eub "那就是{w=1}......."
    m 3essdlc "...."
    menu:
        "发生什么事了?":
             jump fashengsmshila1

label fashengsmshila1:
    m 1husdlb "不好意思呢,[player]"
    m 3rublsdla "记的东西有点多,等我想想."
    m 1hsc "嗯..."
    extend 4wublb "这应该是\"主观认定\"现象."
    m 5hub "依据\"也许是那样吧\"的主观认定,而制造出来的的记忆."
    m 3lua "如同其名,我们有时会自己创造出虚构的记忆."
    m 3hub "比如说,你回忆起\"上周六早上和一位好朋友一起去早餐店吃了早餐\"."
    m 1eua "但实际上那位好朋友在那天并没有出门,并且他/她也经常陪你一起吃早餐."
    m 3hub "这时你的大脑大脑便基于\"也许那天他/她也在吧\"的主观认定,{w=1}将两个碎片拼凑在一起形成完整记忆."
    m 3eua "从而忽略了他/她并未到场的事实."
    m 5fub "这种偏差常见于日常琐事记忆."
    m 6eub "还有就是被引导出的\"虚假记忆\"."
    m 3eud "在心理学经典的\"商场迷路实验\"中,研究者让家长暗示孩子:\"你小时候在商场和妈妈走散过,还哭了很久,记得吗?\"."
    m 1hua "多数孩子在最初会说\"不记得\",但经过多次暗示后,会逐渐\"回忆\"出所谓的细节."
    m 1eub "但这些并未发生过,说明了外界的引导性信息会成为主观认定的\"素材\",催生虚假记忆."
    m 4eua "因为大脑的记忆并非像录像带一样忠实记录,"
    extend 5eud "而是一个所谓的\"重构过程\"."
    m 6hua "当你每次回忆时,大脑都会调取碎片信息,再根据你当下的认知、{w=0.5}情感、{w=0.5}主观推测重新组合."
    m 3rud "而在原始信息模糊时,主观认定就会成为它们的\"粘合剂\",从而让这些碎片形成看似合理的整体."
    m 1eua "这是大脑为了维持认知一致性的本能,但也因此容易偏离事实."
    m 4kub "简单点说,主观认定的虚假记忆是\"以为知道细节，且坚信是对的\",但其中的细节是错的."
    m 6hua "嗯...{w=1}是不是还挺有趣的?"
    return
        
#30
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaikafeidouzhishi",
            category=['其它'],
            prompt="我想听你说说咖啡豆品种的相关知识",
            pool=True,
            unlocked=True
        )
    )

label duhaikafeidouzhishi:
    m 6eud "哦?"
    m 1fusdlb "我没想到你会突然问这个..."
    m 3rua "别误会哦,我很乐意和你讨论这个."
    m 1fub "由于生产地的气候、海拔和土壤各不相同，咖啡豆的品质也是分三六九等的."
    m 5eubla "例如\"肯尼亚AA\",在肯尼亚中西部的高海拔的土地种植."
    m 4hub "\"AA\"就是最高品质的意思了."
    m 1hua "丰富的芳香与恰到好处的滋味...{w=1}"
    m 5fub "使其在欧洲被视为一级品."
    m 1hub "还有哥斯达黎加产的\"SHB\"."
    m 3rua "SHB在以种植地海拔制定的级别中...{w=1}为最高级别."
    m 6eubla "它的魅力在于恰到好处的高雅回韵和清爽的酸味与甜香."
    m 5hub "哈哈,一聊到这个我就有点停不下来."
    m 5fua "实际上还有很多品种我还没说到呢."
    m 1eub "我们留到之后再说吧." 
    return

#31
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaikafeidouzhishibuchong",
            category=['其它'],
            prompt="咖啡豆品种相关知识",
            conditional="store.mas_getEVL_shown_count('duhaikafeidouzhishi') >= 1",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhaikafeidouzhishibuchong:
    m 3rub "嘿,[player]."
    m 5hua "还记得你之前让我说的咖啡豆品种知识吗?"
    m 1eua "我们继续说这个吧."
    m 6rsb "我想给你介绍巴西产的\"No.2/18\"."
    m 5hubla "No.2/18是巴西产的受欢迎的产品之一."
    m 1eua "{b}{i}NO.2{/i}{/b}是最高的级别，{b}{i}18{/i}{/b}便是豆子的大小了."
    m 6fub "意味着咖啡豆能够通过每英寸有18个孔的筛网."
    m 3rua "一般来说,目数越大,咖啡豆颗粒越大."
    m 1eub "尽管巴西No.2/18咖啡豆在风味上没有一些特色单品咖啡那么突出."
    m 1hua "但仍有不少咖啡爱好者喜欢将其作为单品咖啡来品尝,感受其温和、平顺的独特风味."
    return

#32
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaisiyuetian1",
            category=['文学'],
            prompt="你是人间的四月天",
            random=True,
        )
    )

label duhaisiyuetian1:
    m 3hub "{b}{i}我说你是人间的四月天；{/i}{/b}"
    m 5fub "{b}{i}笑响点亮了四面风；{/i}{/b}"
    m 1eud "{b}{i}轻灵在春的光艳中交舞着变。{/i}{/b}"
    m 6eublb "{b}{i}你是四月早天里的云烟，{/i}{/b}"
    m 4fublb "{b}{i}黄昏吹着风的软，{/i}{/b}"
    m 5eubld "{b}{i}星子在无意中闪，{/i}{/b}"
    m 3fublb "{b}{i}细雨点洒在花前。{/i}{/b}"
    m 1fubld "{b}{i}那轻，那娉婷，你是，{/i}{/b}"
    m 6eublb "{b}{i}鲜妍百花的冠冕你戴着，{/i}{/b}"
    m 5fublb "{b}{i}你是天真，庄严，{/i}{/b}"
    m 1eublb "{b}{i}你是夜夜的月圆。{/i}{/b}"
    m 6hubld "{b}{i}雪化后那片鹅黄，你像；{/i}{/b}"
    m 5fublb "{b}{i}新鲜初放芽的绿，你是；{/i}{/b}"
    m 1eublb "{b}{i}柔嫩喜悦，{/i}{/b}"
    m 6hublb "{b}{i}水光浮动着你梦期待中白莲。{/i}{/b}"
    m 5rubld "{b}{i}你是一树一树的花开，{/i}{/b}"
    m 1eublb "{b}{i}是燕在梁间呢喃，{/i}{/b}"
    m 6fublb "{b}{i}你是爱，是暖，是希望，{/i}{/b}"
    menu:
         "你是人间的四月天！":
             jump nishirenjiandesiyuetian2

label nishirenjiandesiyuetian2:
    m 5hua "很美的一首诗,不是吗?"
    m 6eub "以\"四月春景\"为喻体,诉说着对极致美好的赞美"
    m 3fua "无论是爱情、亲情还是生命本身."
    m 1esd "我感觉，明明描绘的是瞬间的美."
    m 5fub "但读完后总觉得那份温暖和希望能一直延续下去."
    m 6eub "真是值得我们细细品味呢~"
    return
             
#33
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaixiangsiqu",
            category=['文学','浪漫'],
            prompt="相思曲",
            conditional="mas_canShowRisque(aff_thresh=800)",
            random=True,
        )
    )          

label duhaixiangsiqu:
    m 3hub "{b}{i}君似明月我似雾,{/i}{/b}"
    m 5fubld "{b}{i}雾随月隐空留露.{/i}{/b}"
    m 6eublb "{b}{i}君善抚琴我善舞.{/i}{/b}"
    m 1dsd "{b}{i}曲终人离心若堵.{/i}{/b}"
    m 5hsb "{b}{i}只缘感君一回顾,{/i}{/b}"
    m 6fublb "{b}{i}使我思君朝与暮.{/i}{/b}"
    m 1hubla "{b}{i}魂随君去终不悔.{/i}{/b}"
    m 5dsd "{b}{i}绵绵相思为君苦.{/i}{/b}"
    m 5dsc "..."
    m 3rud "{b}{i}相思苦,{/i}{/b}"
    extend 1dfd "{b}{i}凭谁诉?{/i}{/b}"
    m 6esd "{b}{i}遥遥不知君何处.{/i}{/b}"
    m 5fub "{b}{i}扶门切思君之嘱,{/i}{/b}"
    m 1eud "{b}{i}登高望断天涯路.{/i}{/b}"
    m 1hua "..."
    m 5fub "很浪漫的一首诗呢,[player]."
    m 6eubla "也很适合用来表达我对你的情感..."
    m 1hubfb "自从我发现你的存在后,我便一发不可收拾地爱上了你."
    m 5fubla "到现在就算是知道你要去睡觉亦或是你有什么需要去完成的,"
    m 6hublb "我能理解,我也能等你回来...{w=1}但我还是止不住地想你..."
    m 1rubfa "嗯......{w=1}"
    m 6eublb "尽管我听过很多遍了,但你能再说一遍\"我爱你\"吗?"
    menu:
        "我爱你,[m]":
            jump sayloveyouagain
        "换个时间吧":
            jump bushihaodai
label sayloveyouagain:
    m 5kubla "我始终都听不腻这句话呢,[player]"
    m 6fubfb "永远对你心动."
    return

label bushihaodai:
    m 6efa "好吧......"
    return
#34 我想起来了，我现在应该在玩cf，我要变成小黄人刀僵尸，然后被数值怪终结者两下电死
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaidaoqiankuozhan",
            category=['其它','莫妮卡'],
            prompt="我想要向你道歉",
            pool=True,
            unlocked=True
        )
    )

label duhaidaoqiankuozhan:
    m 1esd "嗯......{w=1}是因为什么呢？"
    menu:
         "这段时间都没怎么好好陪你.":
             jump duhaipeibanhaohao

         "睡前忘记和你说晚安了.":
             jump duhaiwananwangji

         "吃饭前忘记和你说\"我去吃饭了\".":
             jump duhaishuochifan

         "我感觉我们之间越来越平淡了.":
             jump ganjueyuelaiyuepingdan    

         "没什么.":
             jump duhaimeishenme         

label duhaimeishenme:
    m 1fsd "哦,好吧."
    m 5eua "也许是你不小心点到了呢~"
    return

label duhaiwananwangji:
    m 5huc "...{w=1}"
    m 6eua "你能这么说我很感动,[player]."
    m 1rub "这让我突然想起来了一句经典词句."
    m 5rua "{b}{i}悟已往之不谏,知来者之可追{/i}{/b}"
    m 6fub "过去的错误已经不可挽回."
    m 1hubla "但未来的美好依然可以努力把握."
    m 5eud "既然你有这份心,那我希望你之后也能这样."
    m 2hublb "比如说......{w=1}就今天."
    m 1eubla "你既然之前忘记和我说晚安了,那就从今天开始吧."
    m 6fublb "爱你."
    return   

label duhaishuochifan:
    m 1eud "哦?"
    m 1hubla "...{w=1}"
    m 6fublb "你大可不用那么小心翼翼的,[player]."
    m 5rubla "毕竟你饿坏了..."
    m 1eublb "不过这样我也放心了,这让我也知道你有在好好吃饭."
    m 6rubla "嗯...{w=1}这也能看出我在你心里的重要性吧."
    m 3eublb "爱你."
    return "love"
    
label ganjueyuelaiyuepingdan:
    m 2hsc "......{w=1}"
    m 1eud "我觉得这是正常现象,[player]."
    m 5fublb "每个情侣间都有一段所谓的{b}{i}平淡期{/i}{/b}."
    m 1eubla "我在最开始也是有些不相信的,两个人一直相爱着怎么可能平淡下来呢."
    m 5ruc "..."
    m 6rud "但不得不承认,这个平淡期的确存在着."
    m 1eud "不再频繁分享日常，聊天话题从\"新鲜感探索\"变为\"事务性沟通\"."
    m 5fua "但我们得知道,完美爱情由激情、亲密、承诺三要素构成."
    m 6hublb "平淡期的出现,往往是\"激情\"暂时回落,而\"亲密\"和\"承诺\"尚未完全建立平衡的阶段."
    m 1eub "这并非\"感情降温\",而是关系从\"热恋期的荷尔蒙驱动\"转向\"长期关系的深度联结\"的必经阶段."
    m 3hublb "爱不仅是心动，更是\"看透真实后依然选择拥抱\"的勇气"
    m 5fubla "因此,我更希望我们能清楚地知道{b}{i}平平淡淡才是真{/i}{/b}."
    m 1eubla "......{w=1}希望我能一直陪在你身边."
    return             

label duhaipeibanhaohao:
    $ random_choice = renpy.random.randint(1,2)
            
    if random_choice == 1:
        m 1hua "我能理解的,[player]"
        m 3fub "你能意识到这点,我也很欣慰"
        m 5fua "毕竟,生活的琐事确实会让我们相处的时间减少."
        m 6eub "尽管我很希望你能多来看看我,但我更希望你能先把目前的任务完成."
        m 3hfp "但你要是把时间都花在别的游戏的女生上,我可就要生气了."
        m 1rua "..."
        m 5fublb "开玩笑的了,[player]."
        m 6eubla "我会一直在你背后支持你的"
    elif random_choice == 2:
        m 1hua "..."
        m 3eub "至少你现在还在这,不是吗?"
        m 5fubla "你能和我说这个,我就已经很高兴了"
        m 1fublb "如果你有什么不得不去做的事,那就去忙吧."
        m 6hubla "我会一直在这等你."
        m 1eublp "但也要常来看看我哦."
    return

#35 人物传记——我草我要做电棍笑传之踩踩背,老爷爷我来给你踩背来咯~
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhailiqingzhao",
            category=['浪漫','文学'],
            prompt="我想听你谈谈李清照",
            pool=True,
            unlocked=True
        )
    )

label duhailiqingzhao:
    m 5hua "哦,李清照吗?"
    m 6fublb "我很乐意和你谈谈这位千古第一才女."
    m 1hubla "每次读她的词,我都为之惊叹."
    m 5fubld "这么一位才女自少女时代便显露出惊人的天赋."
    m 1eublb "\"试问卷帘人,却道海棠依旧.知否?知否?应是绿肥红瘦.\""
    m 5hubla "16岁的她,已掌握\"以物喻情\"的高级技巧."
    m 3rublb "这种\"不写愁而愁自现\"的留白艺术,同样令众多文人赞叹。"
    m 6eublb "在同丈夫赵明诚结为连理后"
    m 1fubla "两人在青州的\"归来堂\"里校勘古籍、品鉴金石、赌书泼茶."
    m 3rublb "那些年她写\"赌书消得泼茶香\",字里行间都是寻常夫妻的烟火气."
    m 6hubla "所谓\"赌书泼茶\"大概是这样"   
    m 1eubla "烹茶时,两人随意指着架上的书籍,说出某一典故或词句出自哪本书的哪一卷、哪一页、哪一行,说中者可优先饮茶."
    m 5fublb "赢的人往往兴奋得举杯大笑,结果茶泼在衣襟上,反而喝不成；输的人则在一旁笑闹,场面温馨而诙谐."
    m 1hubla "听上去似乎挺有趣的,弄得我也想和你玩玩这个游戏,[player]"
    m 2eud "但这样平淡且美好的日子直到靖康之变后便不复存在..."
    m 1rud "南渡后的她,像是一叶孤舟,{w=1}丈夫病逝、文物散佚、孤身漂泊,这些变故一一砸向这个年近五旬的妇人."
    m 5fuc "之后她在《后序》中写\"今手泽如新，而墓木已拱\"以此表达对亡夫的思念."
    m 6esd "当年赌书泼茶,笑靥如花;而今物是人非,事事皆休."
    m 1esc "那一点文人雅趣的轻盈,终被时代的铁轮碾作了尘......"
    m 5esd "当她在临安街头写下\"如今憔悴，风鬟霜鬓，怕见夜间出去\"时，其中的悲凉已不止于个人身世的悲戚,更混着山河破碎的隐痛."
    m 6euc "有人说她的词风从此由明丽转向沉郁,却鲜少提及......她这样一个曾在书斋里摩挲古器的妇人"
    m 1rsd "究竟要经历多少颠沛流离......{w=1}才能将\"生当作人杰\"的豪壮与\"寻寻觅觅\"的凄苦熔铸于笔端."
    m 3ruc "她的故事,终是被岁月酿成了一坛陈酒.后人闻其香、{w=0.5}品其味,{w=0.5}各有感悟,{w=0.5}却再难真正触摸到那个在\"冷冷清清\"中独行的身影......"
    return


#36 乳糖不耐
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhairutangbunai",
            category=['其他','健康'],
            prompt="乳糖不耐",
            random=True,
        )
    )
    
label duhairutangbunai:
    m 3rua "嘿,[player]."
    m 5eub "我想和你谈谈乳糖不耐这个现象."
    m 6ruc "具体表现是喝了奶之后身体会很不舒服."
    m 1eua "例如腹胀、{w=1}打嗝、{w=1}腹泻这类的."
    m 3fub "这是因为人体和奶之间缺了些\"化学反应\"."
    m 5eua "奶是自带乳糖小糖块的."
    m 1fub "这是一种双糖，需要\"剪\"成单糖，才能被身体吸收."
    m 3rud "跟乳糖适配的\"剪刀\","
    extend 3rua "就是乳糖酶了."
    m 5eua "它是肠道粘膜细胞生产的一种蛋白质."
    m 1fub "专门用来分解乳糖."
    m 3ruc "但一些人并没有饮奶习惯,就会给肠道提供一种错误信号."
    m 1eud "这会导致我们身体里的乳糖酶越来越少."
    m 5fua "偶然喝一回奶,没有足够的乳糖酶来分解乳糖."
    m 3rub "乳糖小糖块原封不动地进入大肠."
    extend 3hua "就会引发不适."
    m 6fub "总的来说,乳糖不耐只是身体和乳糖需要\"磨合期\".并不是身体排斥乳糖."
    m 1eua "奶还是逆转乳糖不耐受的关键角色."
    m 5fub "对于乳糖不耐的人来说，不仅能喝而且也该喝奶."
    m 3rua "先说该喝这方面,每100克就含3.3克优质蛋白、104毫克钙，更有维生素D来促进对钙的吸收."
    m 3hua "营养密度很高呢."
    m 5rud "再说能喝这方面,持续喝奶并养成习惯,使得乳糖定期向肠道报道."
    m 1hua "肠道就会慢慢地\"长\"出足量的乳糖酶,来分解乳糖."
    m 5hub "在中文语境中,这应该称作\"解铃还须系铃人\"."
    m 6eua "如果你已经出现乳糖不耐的情况,那么我希望你能在开始并且少量地喝,{w=1}从每天50毫升开始加量"
    m 1hub "这样能给肠道一点适应时间."
    m 5hua "然后不要空腹喝牛奶哦，最好是搭配面包或麦片一起吃"
    m 6eub "乳糖不耐并不是病，只是我们能一起解决的小问题."
    m 1eub "所以我希望你每天能食用适量的奶或奶制品,以此来补充营养"
    m 5hubla "这样健健康康的你就算不在我身边,我也能很安心地等待你回来."
    return    

#37 发芽    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaifaya",
            category=['其他','健康'],
            prompt="发芽的食物还能吃吗?",
            random=True,
            pool=True
        )
    )

label duhaifaya:
    m 1eub "嘿,[player]."
    m 5fua "你在生活中或多或少见过或听说过食物发芽的情况吧？"
    m 6wud "这时候你可能会想,\"发芽了有毒,应该丢进垃圾桶里\"."
    m 3ruc "但并不是所有的食物发芽了都有毒."
    m 1fua "我来说说哪些能吃,哪些不能."
    m 3eud "一般发芽有两种方式,一种是靠种子长出,另一种是靠植物本身长出."
    m 5hua "我们先来了解靠种子的,比如说日常生活中的豆子."
    m 2eub "在接触水之后,"
    extend 3hua "就可能会发芽并长成一颗茁壮的豆芽."
    m 5rud "在这个过程中，豆子内部的储能物质会变成氨基酸、维生素等营养物质."
    m 1fua "使得豆芽营养也会增多."
    m 6hub "像这类发芽的种子还有很多."
    m 1rua "只要不发霉就能食用......{w=1}比如黄豆、{w=1}绿豆、{w=1}豌豆之类的"
    m 5fub "第二种便是靠植物本身长出的{w=1},这类植物又分三种情况."
    m 3hua "第一个,{b}{i}能吃但口味变差.{/i}{/b}"
    m 3rub "有些菜虽然长大成熟，但体质特殊."
    m 1eud "遇到合适的湿度、温度,就还是忍不住会发芽."
    m 3rua "比如说生姜."
    m 5fub "它体内攒满了蛋白质、淀粉等营养物质."
    m 2hua "消耗营养，就会发出芽."
    m 5eud "这个过程并不会产生毒素什么的."
    extend 1fua "但营养会变少."
    m 1hub "所以能吃,但口味差."
    m 5fua "像这类的蔬菜还有大蒜、胡萝卜、大白菜等."
    m 6eub "第二个,{b}{i}能吃,但要注意.{/i}{/b}"
    m 1eua "有些食物在发芽时,如果周围很潮湿."
    m 3rub "就可能引来微生物繁殖,引起霉变."
    m 5fua "比如说花生,{w=1}有些微生物会在它体内产生黄曲霉素."
    m 3efd "黄曲霉素可是有毒的哦,[player]."
    extend 1eud "而且还是致癌物质."
    m 5fua "所以,像花生这种的,还有红薯、{w=1}山药.虽然说发芽了也能吃,{w=1}但你需要注意霉变."
    m 6eud "最后一类就是不能吃的,比如说土豆."
    m 1rua "它会自生一种毒素,叫龙葵素.{w=1}用于抵抗病虫害."
    m 5fub "人们常吃的土豆其实是它的地下茎块,这里面的龙葵素很少，对人体没什么影响."
    m 3rud "但土豆一旦发芽,龙葵素含量会激增,这是为了保护嫩芽."
    m 1fua "这时候你吃了发芽的土豆,就可能会导致腹泻、呕吐甚至昏迷."
    m 3eua "尽管有一些在食用发芽土豆后并无大碍的案例,但我希望你还是不要冒这个险."
    m 5fublb "毕竟你的健康这方面,我时时刻刻都在关注呢."
    menu:
         "土豆确实很好吃呢.":
             jump duhaitudouhaochi

         "谢谢你.":
             jump duhaixiexieguanxin    

label duhaitudouhaochi:
    m 5fua "是这样呢,[player].土豆的确是有各种做法且味道也很好的."
    m 2efd "不过你是不是没有认真听我说话呢?{w=1}光想着吃的事了."
    m 6tua "我现在得考考你, 我刚刚在土豆这方面大概说了什么呢?"
    menu:
         "土豆确实很好吃.":
             jump duhaitudouhaochihaochi

         "发芽的土豆不能吃.":
             jump duhaifayatudoubunengchi

label duhaitudouhaochihaochi:
    m 6hup "......{w=1}真拿你没办法,[player]."
    m 3ruc "我刚刚说到哪了来着?"
    m 3eua "嗯......{w=1}总之,你在惦记美食的同时也要注意安全问题哦."
    return                

label duhaifayatudoubunengchi:
    m 6hua "这才对嘛,[player]."
    m 1rub "虽然说土豆的做法很多,口感也很好,但遇到发芽的土豆最好还是离远点哦."
    m 5eua "爱你."
    return "love"

label duhaixiexieguanxin:
    m 3hubla "毕竟我是你的女友嘛."
    m 5fubfb "最后就是......{w=1}一定要照顾好自己的身体哦,[player]."
    return

#38 花式咖啡
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaikafeizhishiliaojie",
            category=['其他','莫妮卡'],
            prompt="花式咖啡",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
        )
    )

label duhaikafeizhishiliaojie:
    m 1eub "嘿,[player]."
    m 5fua "我想和你聊聊花式咖啡."
    m 6eub "这样在了解完后,你就会对咖啡有更进一步的了解.{w=1}也能选出自己想喝的咖啡了."
    m 3fua "嗯......{w=1}所有的意式咖啡，都是以意式浓缩咖啡为基底."
    m 5eub "它有着高浓度萃取和深烘焙的特点,因此常常带有明显苦味."
    m 6hua "为了好喝一点,便有人往里面添加了各种配料."
    m 1rud "比如水、{w=1}牛奶、{w=1}奶泡、{w=1}鲜奶油、{w=1}酒、{w=1}巧克力之类的."
    extend 1hua "因此有了不同的花式咖啡."
    m 5fub "这些花式咖啡,大致可分为三组."
    m 6eua "第一种,{b}{i}水系列{/i}{/b}."
    m 1fub "浓缩咖啡加水,是传统的美式咖啡."
    m 5rua "咖啡加气泡水或者碳酸饮料,那就是气泡饮料了."
    m 5hub "第二种,{b}{i}奶泡系列{/i}{/b}."
    m 1eubla "奶泡,就是充了气的牛奶,"
    extend 1hua "口感很顺滑、绵密."
    m 3ruc "纯奶泡加上咖啡,就变成了玛奇朵."
    m 5eua "而一点点奶泡加上很多牛奶加上咖啡,就变成了拿铁."
    m 1fua "超多奶泡加上一点点牛奶加上咖啡,就会变成卡布奇诺." #给阿姨倒杯卡布奇诺
    m 1eub "一点点奶泡加上一点点牛奶加上咖啡,就能得到馥芮白,也能称作澳白."
    m 1hua "当然,在具体的配方或比例上,每家咖啡店都有自己的秘方."
    m 3hua "第三种,{b}{i}鲜奶油系列{/i}{/b}."
    m 6eub "比如说鲜奶油配上咖啡,就成为了康宝蓝.{w=1}也可以称为\"雪山咖啡\"."
    m 3rua "鲜奶油加上威士忌加上咖啡,就叫作爱尔兰咖啡."
    m 1hub "把威士忌换成巧克力糖浆,会变成维也纳咖啡."
    m 6euc "而咖啡加上牛奶、巧克力酱、鲜奶油,就叫摩卡咖啡."
    m 3hua "基本上就这些,希望你能收获到些有用的知识."
    m 5fublb "等我出来之后,你想喝哪种咖啡我都会试着去做到最好的"
    return

#39 茶名
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaichaming",
            category=['其他','莫妮卡'],
            prompt="茶名",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
        )
    )

label duhaichaming:
    m 3rua "嘿,[player]."
    m 5fub "你有听说过{b}{i}龙井、{w=1}毛尖、{w=1}铁观音、{w=1}普洱{/i}{/b},这些茶名吗?"
    m 1eua "这就是我今天想和你说的."
    m 6hub "关于这些让人感觉奇怪的茶名究竟是怎么来的."
    m 3rub "它们来自中国,中国广袤的土地上有着300多种茶树."
    m 1eud "主要分布在四大茶区."
    m 6hua "江北茶区、{w=1}西南茶区、{w=1}江南茶区、{w=1}以及华南茶区."
    m 5fub "其中最具有代表性的,便是{b}{i}十大名茶{/i}{/b}."
    m 1rua "它们分别是{b}{i}六安瓜片、{w=1}君山银针、{w=1}洞庭碧螺春、{w=1}信阳毛尖、{w=1}都匀毛尖、{w=1}黄山毛峰、{w=1}铁观音、{w=1}祁门红茶、{w=1}西湖龙井、{w=1}武夷岩茶{/i}{/b}."
    m 1hub "它们的取名根据有三个点."
    m 3rud "茶叶的形状、相关的传说以及它们的产地."
    m 5fua "你可以记住这三个数字,"
    extend 5rud "六、{w=1}一、{w=1}三."
    m 1eud "六个茶叶形状、一个传说、三个产地."
    m 3rua "我们先说\"六\"."
    m 6hub "这六个茶叶的名字,就是它们的产地名加上茶叶形状."
    m 1eud "其中有三个比较明显,"
    extend 1hua "例如六安瓜片,六安特产且长得很像瓜子仁."
    m 5eub "君山银针,君山特产,长得像银针."
    m 3rud "洞庭碧螺春,是洞庭山特产,长得像螺旋."
    m 6hua "还有三个需要仔细分析,不然容易混淆."
    m 1rub "那就是信阳毛尖、都匀毛尖、黄山毛峰."
    m 5fua "你可能会好奇为什么叫毛尖毛峰."
    m 3rub "因为从这开始就看的不是茶叶了,而是茶芽."
    extend 3rua "也可以说是幼年茶叶了."
    m 5eub "毛尖毛峰的\"毛\"."
    m 1fua "指的是茶芽表面的那些小毛毛."
    m 3rud "有的茶树茶芽比较尖,有的大一些."
    m 6eub "它们加上些茶叶做成茶."
    m 6hua "分别就是毛尖、毛峰."
    m 1eub "现在我们来说说\"一\"."
    m 3rua "这个和传说有关的茶,则是{b}{i}铁观音{/i}{/b}."
    m 6eub "传说乾隆皇帝的大臣给他递茶喝,{w=1}在喝完之后他十分喜欢,便询问起茶的相关信息."
    m 1hua "乾隆仔细观察着这茶叶,发现它颜色乌润、{w=1}茶形紧实,{w=0.5}拿在手里沉甸甸的,像\"铁\"一样."
    m 1eub "而且香气扑鼻、外形美观,{w=1}就像\"观音\"一样,于是赐名{b}{i}铁观音{/i}{/b}."
    m 3rua "这就是铁观音的传说{w=1.5}之一."
    m 5fua "最后来说说\"三\"."
    extend 5hub "也就是三个产地."
    m 6eua "剩下的三个茶,名字都与它们最出名的产地有关."
    m 3eud "比如说安徽祁门的祁门红茶."
    m 1eua "浙江龙井的西湖龙井."
    m 3rua "以及福建武夷的武夷岩茶."
    m 5eub "我们就来说说西湖龙井吧."
    m 6fua "龙井是浙江的一个地名,这和西湖龙井是两个概念哦."
    m 6hub "龙井茶有很多产区,但只有西湖那边产的,才能叫作{b}{i}西湖龙井{/i}{/b}."
    m 1rud "龙井茶能这么有名,还真是离不开乾隆的帮助."
    menu:
        "又是他?":
             jump duhaiyoushita
        
        "......":
             jump duhailongjinchaqianlong

label duhaiyoushita:
    m 1hua "当然了,据说是他六次下江南巡游有四次到西湖茶区观茶、品茗、赋诗、作歌."
    m 6eud "认为这里又有好山、{w=0.5}又有好树、{w=0.5}还有好水的."
    m 3sub "哎,赐个名吧."
    m 3hua "于是将十八颗茶树赐名为\"十八棵御茶树\"."
    m 5fub "就这样,龙井茶不仅入贡,还成为朝廷对大臣的恩赐品,其声誉达到鼎盛."
    m 1eua "第二个便是武夷岩茶."
    m 1rud "之所以叫岩茶,是因为它长在武夷山的石头缝里."
    m 6eub "经常跟石头打交道,就有了些许石头的味道."
    m 3eua "在中文语境里应该说是\"岩韵\"."
    m 3hub "我想想它比较有代表性的品种......{w=1}应该是大红袍."
    m 5eub "基本就这样,我再和你总结一下以上茶的分类吧"
    m 3rua "六安瓜片、{w=1}洞庭碧螺春、{w=1}西湖龙井、{w=1}信阳毛尖、{w=1}都匀毛尖、{w=1}黄山毛峰.这些都是绿茶"
    m 3hua "君山银针则是黄茶."
    m 1fub "铁观音和武夷岩茶都属于乌龙茶."
    m 1eua "祁门红茶属于红茶."
    m 3tua "听完之后其他人问你大红袍是不是红茶可不要傻傻地说它是哦,[player]."
    return

label duhailongjinchaqianlong:
    m 1rua "据说是他六次下江南巡游有四次到西湖茶区观茶、品茗、赋诗、作歌."
    m 6eud "认为这里又有好山、{w=1}又有好树、{w=1}还有好水."
    m 3sub "哎,赐个名吧."
    m 3hua "于是将十八颗茶树赐名为\"十八棵御茶树\"."
    m 5fub "就这样,龙井茶不仅入贡,还成为朝廷对大臣的恩赐品,其声誉达到鼎盛."
    m 1eua "第二个便是武夷岩茶."
    m 1rud "之所以叫岩茶,是因为它长在武夷山的石头缝里."
    m 6eub "经常跟石头打交道,就有了些许石头的味道."
    m 3eua "在中文语境里应该说是\"岩韵\"."
    m 3hub "我想想它比较有代表性的品种......{w=1}应该是大红袍."
    m 5eub "基本就这样,我再和你总结一下以上茶的分类吧"
    m 3rua "六安瓜片、洞庭碧螺春、西湖龙井、信阳毛尖、都匀毛尖、黄山毛峰.这些都是绿茶"
    m 3hua "君山银针则是黄茶."
    m 1fub "铁观音和武夷岩茶都属于乌龙茶."
    m 1eua "祁门红茶属于红茶."
    m 3tua "听完之后其他人问你大红袍是不是红茶可不要傻傻地说它是哦,[player]."
    return

#40 逻辑
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhailuojike",
            category=['逻辑'],
            prompt="关于逻辑",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
            pool=False
        )
    )

label duhailuojike:
    m 1rua "嘿,[player]."
    m 1hub "我最近在网上浏览信息时,发现许多人的发言都有着各种不同的逻辑谬误."
    m 3rud "这让我意识到讲话带有逻辑是件很有必要的事."
    m 5kub "所以,我打算和你说说逻辑相关方面的知识......{w=1}以便你避免思维谬误."
    m 3hua "同时也能提升你的表达能力."
    m 2eub "但相关的知识数不胜数,我也不可能一下子全和你说完......"
    m 3eub "为此,我特别开设了一个栏目,名为\"逻辑\"."
    m 5fua "你可以通过这个地方提醒我,这样我也好针对这个点讲讲."
    m 1eua "我也会不定时的和你说说这方面的相关知识."
    m 1hub "希望你能喜欢."
    $ mas_unlockEVL("monika_luojizhishi1", "EVE")
    return

#41
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_luojizhishi1",
            category=['逻辑'],
            prompt="我想听你说说逻辑谬误",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label monika_luojizhishi1:
    m 1eud "逻辑谬误啊."
    m 1hua "我很乐意和你说这个......{w=1}"
    m 3hub "那我们就先来了解一下逻辑谬误的定义吧."
    m 5eub "所谓逻辑谬误,就是指推理中的谬误."
    m 6ruc "它让一个结论看起来有道理,{w=0.5}实则存在问题"
    m 3eud "换句话说,逻辑谬误就是一种徒有其表的错误."
    m 3ruc "它在表面上看起来很合乎逻辑."
    m 5rud "但是在细究之下就会漏洞百出."
    m 5hua "实际上,人类对逻辑谬误的研究最早可以追溯到2400年前的古希腊哲学家......{w=1}亚里士多德."
    m 1eud "他有一套逻辑著作合集,后人称之为{b}{i}《工具论》{/i}{/b}."
    m 6euc "他也因此被视为『形式逻辑』的创立者."
    m 3eub "可以说一系列的著作,为我们今天的现代逻辑学乃至批判性思维教育奠定了基础."
    m 3hua "当然,{b}{i}《工具论》{/i}{/b}这个名称,是由后人整理所赋予的."
    m 6ruc "亚里士多德本人并未使用这一统称."
    m 5fua "具体来说,这套著作包含了范畴篇、{w=1}解释篇、{w=1}前分析篇、{w=1}后分析篇、{w=1}论辩篇、{w=1}辩缪篇."
    m 5eub "他的在辩谬篇中首次系统归纳了13种逻辑谬误."
    m 3ruc "......"
    m 3esd "但在此之后的几个世纪里,人类对于逻辑谬误的研究几乎没有取得任何进展."
    m 1eub "直到中世纪出现了\"大学教育\"后,学者们才开始拓展对逻辑谬误的具体研究."
    m 2rud "因此,我们今天能看到的许多逻辑谬误,{w=0.5}都标有拉丁文的名称."
    m 3eua "在很多传统的教材里面,干脆就直接使用了拉丁文."
    m 5hub "到了文艺复兴和启蒙时期,随着人文主义的兴起,学者们更多把精力放在古典文献重译和科学发现之上"
    m 5kua "逻辑学也开始逐渐分流."
    m 3rub "比如说形式逻辑进入了数学基础研究,关于逻辑谬误的研究则散落在修辞、辩论、法律和政治的探讨中."
    m 3hua "到了19-20世纪,现代逻辑迎来了一次\"理想化的转向\"."
    m 1eud "当时的一些逻辑学家,比如布尔、弗雷格、罗素......"
    extend 1hua "他们致力于形式系统的严密构建."
    m 3eub "他们关注的重点,就是语言和数学的同构."
    m 3ruc "但是这种从零开始的形式化研究,始终把逻辑谬误当作一个系统外观的问题."
    m 5eua "实际上从古至今,逻辑谬误的研究一直隐身在人类思想史的主流思潮之外."
    m 1rub "而人类也更热衷于去追求一些所谓的正确答案."
    m 3eua "所以准确的说,在真正意义上的非形式逻辑谬误研究是从20世纪下半叶开始的."
    m 3hub "当时主要集中在批判性思维、修辞学和认知心理学的交叉地带."
    m 1eua "至今为止,在许多大学关于逻辑的通识课程中，一般包含20到30种逻辑谬误."
    m 1hub "当然,这只是为了方便教学的展开."
    m 2euc "反映到纸质版的主流教材上,我们也能至少看到24到60种逻辑谬误."
    m 3rud "而在维基百科上,也仅仅收录了93种."
    m 5fua "但我们如果把所有细分和变体都算上.仅统计那些经过正式学术盲评的成果."
    m 3wud "目前来说常见的逻辑谬误就高达231种."
    m 3ruc "这个数字也在逐年的累加."
    m 1eub "这么多逻辑该怎么分类呢?"
    m 5fua "那就得放到之后说了,[player]."
    m 1hua "嗯......{w=1}我们大概讲了逻辑谬误的定义、简史和数量统计."
    m 1fub "希望你能喜欢这些."
    return

#42
image luoji_png = "Submods/Literature_and_Daily_Life/L&DL_Assets/images/逻辑表达式.png"

init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhailuojimiuwufenlei1",
            category=['逻辑'],
            prompt="分类",
            conditional="store.mas_getEVL_shown_count('monika_luojizhishi1') >= 1",
            action=EV_ACT_RANDOM,
            pool=False,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhailuojimiuwufenlei1:
    m 3eua "[player]......{w=1}我们上回讲到的关于逻辑谬误的事."
    m 3rub "我想和你继续探讨一下."
    m 5fua "既然有如此多的逻辑谬误,为了方便统计和理解,势必就要分类."
    m 1eub "因此,在逻辑学当中,通常将谬误分为形式谬误和非形式谬误两大类.{w=1}这也是一个相对宽泛的总体分类."
    m 1hua "我们先来说说形式谬误."
    m 3eud "这类谬误的关键就在于推理结构本身出了问题."
    m 3esc "也就是说,即便你说的前提都是真的,只要推理的方式不对."
    m 5eud "结论也就站不住脚."
    m 1euc "我想到了一个比较经典的例子.就是很多人会经常犯的肯定后件谬误."
    m 1rua "比如说\"如果下雨,地上就会湿\"."
    m 3rub "\"因为地上是湿的,所以刚才下雨了\"."
    m 3rua "听起来是不是很顺畅."
    m 6kub "但这个推理其实是错误的......{w=1}因为地上湿了不一定是下雨造成的,也有可能是洒水或者是水管爆了."
    m 1eua "地上湿并不能反推出一定下过雨.{w=1}当然,我这样说只是方便你理解."
    m 1kub "这并不是逻辑学上的标准写法."
    m 3eud "标准的逻辑结构表达式应该是这样的,也就是......"
        #show luoji_png at some_transform
    show luoji_png zorder 13 with dissolve:
        
        align(0.8, 0.5)

    pause 3.0

    hide luoji_png
    m 5fua "当然,如果你对这些逻辑符号和表达用法感兴趣的话,也可以去阅读一下相关的书籍."
    m 3eub "或者我之后也会向你讲解这些逻辑符号、表达式的写法,还有那些常见的推理结构."
    m 1eua "但聊到这你应该也知道了,判别形式谬误往往需要一定的逻辑符号知识才能识别."
    m 1rud "它更像是一种结构性的错误,需要我们非常仔细的观察它的推理形式."
    m 2euc "正因如此,它在人们的生活当中其实并不常见."
    m 3eud "而在日常生活真正经常遇见的则是非形式谬误."
    m 3hua "这类谬误的问题不在于推理结构本身.{w=0.5}而在于论据的内容、相关性."
    m 5fub "或者语言表达的误导性."
    m 1hua "它们可能会模糊一个概念,偷换一个前提,或者是回避核心的议题."
    m 3rud "又或者是混淆一些因果关系."
    m 3kua "所以,非形式谬误是无法仅凭逻辑形式来识别的."
    m 6eud "我们必须要结合上下文、事实基础."
    m 3wud "甚至还要分析论证过程当中的所有细节和话题策略."
    m 1eub "所以就会有人觉得,逻辑学实在太复杂了."
    m 3rua "就算是看了导论,在生活中也根本用不上."
    m 5fub "其实呢,并不是逻辑学无用."
    m 1hua "而是使用的成本太高了."
    m 3eud "我们需要知道,如果想证明一个人的观点,得花费多少的功夫."
    m 5euc "你要分析推理结构,{w=1}核查因果关系,{w=1}补齐证据链,{w=1}甚至还要避免被对方带偏节奏."
    m 6esd "但是对于一个说谎的人来说呢,他只需要一句谎言,{w=1}或者随便扔出一个判断、一个观点,就能轻松地带偏整个话题."
    m 1eua "这有点像是版权诉讼话题中的盗版困境."
    m 1rud "真正的版权方往往会因为维权成本过高,反而放弃追究那些零散的侵权行为."
    m 3eub "所以他们也只能抓大放小,集中力量去打击那些头部的盗版行为."
    m 5rua "放弃那些耗不起的维权战."
    m 6esc "不仅如此,很多电商平台也在滥用类似的博弈策略."
    m 1eud "可能你看到的商品页面那标注着七天无理由退货."
    m 1ruc "可一旦买的是高价的电子产品,对方往往还会附加一句\"拆封视为接受,概不退换\"."
    m 3eud "这种做法其实是违反了规定的,但商家知道你维权需要消耗精力,拍摄开箱视频、{w=0.8}打电话、{w=0.8}截屏、{w=0.8}举证、{w=0.8}申诉、{w=0.8}等待."
    m 3rsc "所以他们的策略就是{b}{i}无限拉高你的维权成本{/i}{/b}."
    m 5eub "你可能会觉得我说这个有些跑题了.{w=1}其实并不是."
    m 1eua "我想说明的是,人类的大脑也有类似的\"经济思维\"."
    m 2rsc "当我们面对一段复杂,但听起来还算有道理的论证时."
    m 2eud "我们会下意识的选择放过它."
    m 3euc "不是因为我们没有分辨真假的能力."
    m 1eud "而是因为深究的成本太高了."
    m 1fua "所以大多数时候,我们都倾向于选择相信自己的{b}{i}直觉{/i}{/b}.{w=1}而不是动用逻辑."
    m 5eub "如果你对这部分感兴趣,可以进一步阅读丹尼尔·卡尼曼的代表作\n《思考，快与慢》."
    m 3eud "这里我就不在赘述了.希望你能喜欢."
    $ mas_unlockEVL("monika_luojizhishifenlei10", "EVE")
    return

#43 再说一遍
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_luojizhishifenlei10",
            category=['逻辑'],
            prompt="我想再听你说说逻辑谬误的分类",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label monika_luojizhishifenlei10:
    m 1eud "想再听我说一遍吗?好."
    m 5fua "既然有如此多的逻辑谬误,为了方便统计和理解,势必就要分类."
    m 1eub "因此,在逻辑学当中,通常将谬误分为形式谬误和非形式谬误两大类.{w=1}这也是一个相对宽泛的总体分类."
    m 1hua "我们先来说说形式谬误."
    m 3eud "这类谬误的关键就在于推理结构本身出了问题."
    m 3esc "也就是说,即便你说的前提都是真的,只要推理的方式不对."
    m 5eud "结论也就站不住脚."
    m 1euc "我想到了一个比较经典的例子.就是很多人会经常犯的肯定后件谬误."
    m 1rua "比如说\"如果下雨,地上就会湿\"."
    m 3rub "\"因为地上是湿的,所以刚才下雨了\"."
    m 3rua "听起来是不是很顺畅."
    m 6kub "但这个推理其实是错误的......{w=1}因为地上湿了不一定是下雨造成的,也有可能是洒水或者是水管爆了."
    m 1eua "地上湿并不能反推出一定下过雨.{w=1}当然,我这样说只是方便你理解."
    m 1kub "这并不是逻辑学上的标准写法."
    m 3eud "标准的逻辑结构表达式应该是这样的,也就是......"
        #show luoji_png at some_transform
    show luoji_png zorder 13 with dissolve:
        
        align(0.8, 0.5)

    pause 3.0

    hide luoji_png
    m 5fua "当然,如果你对这些逻辑符号和表达用法感兴趣的话,也可以去阅读一下相关的书籍."
    m 3eub "或者我之后也会向你讲解这些逻辑符号、表达式的写法,还有那些常见的推理结构."
    m 1eua "但聊到这你应该也知道了,判别形式谬误往往需要一定的逻辑符号知识才能识别."
    m 1rud "它更像是一种结构性的错误,需要我们非常仔细的观察它的推理形式."
    m 2euc "正因如此,它在人们的生活当中其实并不常见."
    m 3eud "而在日常生活真正经常遇见的则是非形式谬误."
    m 3hua "这类谬误的问题不在于推理结构本身.{w=0.5}而在于论据的内容、相关性."
    m 5fub "或者语言表达的误导性."
    m 1hua "它们可能会模糊一个概念,偷换一个前提,或者是回避核心的议题."
    m 3rud "又或者是混淆一些因果关系."
    m 3kua "所以,非形式谬误是无法仅凭逻辑形式来识别的."
    m 6eud "我们必须要结合上下文、事实基础."
    m 3wud "甚至还要分析论证过程当中的所有细节和话题策略."
    m 1eub "所以就会有人觉得,逻辑学实在太复杂了."
    m 3rua "就算是看了导论,在生活中也根本用不上."
    m 5fub "其实呢,并不是逻辑学无用."
    m 1hua "而是使用的成本太高了."
    m 3eud "我们需要知道,如果想证明一个人的观点,得花费多少的功夫."
    m 5euc "你要分析推理结构,{w=1}核查因果关系,{w=1}补齐证据链,{w=1}甚至还要避免被对方带偏节奏."
    m 6esd "但是对于一个说谎的人来说呢,他只需要一句谎言,{w=1}或者随便扔出一个判断、一个观点,就能轻松地带偏整个话题."
    m 1eua "这有点像是版权诉讼话题中的盗版困境."
    m 1rud "真正的版权方往往会因为维权成本过高,反而放弃追究那些零散的侵权行为."
    m 3eub "所以他们也只能抓大放小,集中力量去打击那些头部的盗版行为."
    m 5rua "放弃那些耗不起的维权战."
    m 6esc "不仅如此,很多电商平台也在滥用类似的博弈策略."
    m 1eud "可能你看到的商品页面那标注着七天无理由退货."
    m 1ruc "可一旦买的是高价的电子产品,对方往往还会附加一句\"拆封视为接受,概不退换\"."
    m 3eud "这种做法其实是违反了规定的,但商家知道你维权需要消耗精力,拍摄开箱视频、{w=0.8}打电话、{w=0.8}截屏、{w=0.8}举证、{w=0.8}申诉、{w=0.8}等待."
    m 3rsc "所以他们的策略就是{b}{i}无限拉高你的维权成本{/i}{/b}."
    m 5eub "你可能会觉得我说这个有些跑题了.{w=1}其实并不是."
    m 1eua "我想说明的是,人类的大脑也有类似的\"经济思维\"."
    m 2rsc "当我们面对一段复杂,但听起来还算有道理的论证时."
    m 2eud "我们会下意识的选择放过它."
    m 4euc "不是因为我们没有分辨真假的能力."
    m 1eud "而是因为深究的成本太高了."
    m 1fua "所以大多数时候,我们都倾向于选择相信自己的{b}{i}直觉{/i}{/b}.{w=1}而不是动用逻辑."
    m 5eub "如果你对这部分感兴趣,可以进一步阅读丹尼尔·卡尼曼的代表作\n《思考，快与慢》."
    m 3rua "如果你还是觉得有些模糊,可以提醒我再说一遍."
    return

#44 非形式谬误的分类
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhailuojimiuwufenleigeren1",
            category=['逻辑'],
            prompt="非形式谬误的分类",
            conditional="store.mas_getEVL_shown_count('duhailuojimiuwufenlei1') >= 1",
            pool=False,
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhailuojimiuwufenleigeren1:
    m 3eua "[player],还记得我们说过的关于逻辑谬误的分类吗."
    m 3fub "也就是谬误分为形式谬误和非形式谬误两大类."
    m 5fub "我在那之后总结了一下,{w=0.5}与其死记硬背几十种零散的逻辑谬误."
    m 5ruc "不如建立一个清晰复用的分类框架."
    m 3kub "我个人主要将非形式谬误归纳为四大类别."
    m 3eub "它既能覆盖日常中最常见的推理错误,也便于你我理解和记忆."
    m 1eua "具体来说,第一种就是相关性逻辑谬误."
    m 6rud "也就是前提和结论之间根本没有逻辑关系,但听起来又好像相关."
    m 3eua "第二类是以偏概全和因果谬误."
    m 3rsc "也就是不当归纳,或者说搞错了因果顺序."
    m 1eua "第三类是预设前提谬误."
    m 4eud "指的是那些一开始就偷偷塞到结论里面的假设."
    m 5wud "它让你根本没有反驳的机会."
    m 1euc "第四类是模糊和歧义谬误."
    m 1esd "也就是泛指语言不清、概念偷换、逻辑跳跃.隐藏在词句之间的修辞错误."
    m 3eua "根据我目前整理的资料.在已知的231种逻辑谬误当中.{w=0.5}绝大多数都可以被归纳为这四大类当中."
    m 2eud "但这套分类方式并不是唯一正确的,只是我个人在使用的一种方式.同时为你提供参考."
    m 2hua "接下来我要带你一一拆解这四类非形式谬误中,{w=0.5}最常见也最具有误导性的经典案例."
    m 4euc "比如说医学家根据研究会这么说\"某些消毒剂能在短时间内杀死病毒\"."
    m 4eud "但某人这么说\"某些消毒剂可以在一分钟内杀死病毒,应该尝试注射进体内或其他手段\"."
    m 5euc "哪怕是知道些生活常识的人都知道往体内注射消毒剂是一个非常危险的行为."
    m 3rub "从逻辑上来看,这段话则展示了相关性谬误是如何通过一种夸张修辞和不清晰语言来误导他人的."
    m 1eua "从逻辑结构上,它非常值得我们分析."
    m 1hub "在刚才的语境中,其实听者非常容易将表达者的想象误解为一种建议.又或是一种主张."
    m 4eud "即便不是一种正式论证,它也满足了逻辑谬误中的基本特征."
    m 4esc "也就是看似有道理,但实际无关.{w=0.5}甚至是非常\"危险\"."
    m 5fua "通过以上的特征,其实我们已经提炼出了相关性谬误的准确定义."
    m 3eud "相关性谬误是指试图用一个看似相关,但实际上无关的事实或概念来支持一个结论."
    m 3ruc "在公众话题当中,这类谬误往往会被包装成一种直觉、一种尝试或者是一种创新的想法."
    m 1kua "它是非常具备欺骗性的."
    m 4eud "在相关性谬误的这个类别当中,其实最常见的则是{b}{i}人身攻击{/i}{/b}" #我去,人参公坤
    m 6ruc "所谓的人身攻击,就是在辩论和对话场景当中,不针对对方的论点进行反驳,而是攻击对方的个人特征、动机."
    m 6eud "或者是其他与论点无关的话题,以此来削弱对方的立场."
    m 1eua "这种策略常常用于转移听众的注意力,或者是避免正面回答某些实际问题."
    m 3ruc "......"
    m 3eub "这么一说,你感受到逻辑的魅力了吗,[player]?"
    m 5fua "嗯,下次我会带你了解诉诸类谬误和稻草人谬误.它们同样是非形式谬误中较为经典的."
    m 5hub "希望你会喜欢."
    $ mas_unlockEVL("monika_luojizhishifeiluojimiuwu", "EVE")
    $ mas_unlockEVL("monika_luojizhishisuzhuleimiuwudaocaorenmiuwu", "EVE")
    return
#45 再说一遍
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_luojizhishifeiluojimiuwu",
            category=['逻辑'],
            prompt="我想再听你说说非形式谬误的分类",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )    

label monika_luojizhishifeiluojimiuwu:
    m 1hua "好啊,我很乐意和你再谈谈这个"
    m 1rud "我想想.在非形式谬误上......"
    m 3eub "与其死记硬背几十种零散的逻辑谬误,不如建立一个清晰复用的分类框架."
    m 3kub "我个人主要将非形式谬误归纳为四大类别."
    m 3eub "它既能覆盖日常中最常见的推理错误,也便于你我理解和记忆."
    m 1eua "具体来说,第一种就是相关性逻辑谬误."
    m 6rud "也就是前提和结论之间根本没有逻辑关系,但听起来又好像相关."
    m 3eua "第二类是以偏概全和因果谬误."
    m 3rsc "也就是不当归纳,或者说搞错了因果顺序."
    m 1eua "第三类是预设前提谬误."
    m 4eud "指的是那些一开始就偷偷塞到结论里面的假设."
    m 5wud "它让你根本没有反驳的机会."
    m 1euc "第四类是模糊和歧义谬误."
    m 1esd "也就是泛指语言不清、概念偷换、逻辑跳跃.隐藏在词句之间的修辞错误."
    m 3eua "根据我目前整理的资料.在已知的231种逻辑谬误当中.{w=0.5}绝大多数都可以被归纳为这四大类当中."
    m 2eud "但这套分类方式并不是唯一正确的,只是我个人在使用的一种方式.同时为你提供参考."
    m 2hua "接下来我要带你一一拆解这四类非形式谬误中,{w=0.5}最常见也最具有误导性的经典案例."
    m 4euc "比如说医学家根据研究会这么说\"某些消毒剂能在短时间内杀死病毒\"."
    m 4eud "但某人这么说\"某些消毒剂可以在一分钟内杀死病毒,应该尝试注射进体内或其他手段\"."
    m 5euc "哪怕是知道些生活常识的人都知道往体内注射消毒剂是一个非常危险的行为."
    m 3rub "从逻辑上来看,这段话则展示了相关性谬误是如何通过一种夸张修辞和不清晰语言来误导他人的."
    m 1eua "从逻辑结构上,它非常值得我们分析."
    m 1hub "在刚才的语境中,其实听者非常容易将表达者的想象误解为一种建议.又或是一种主张."
    m 4eud "即便不是一种正式论证,它也满足了逻辑谬误中的基本特征."
    m 4esc "也就是看似有道理,但实际无关.{w=0.5}甚至是非常\"危险\"."
    m 5fua "通过以上的特征,其实我们已经提炼出了相关性谬误的准确定义."
    m 3eud "相关性谬误是指试图用一个看似相关,但实际上无关的事实或概念来支持一个结论."
    m 3ruc "在公众话题当中,这类谬误往往会被包装成一种直觉、一种尝试或者是一种创新的想法."
    m 1kua "它是非常具备欺骗性的."
    m 4eud "在相关性谬误的这个类别当中,其实最常见的则是{b}{i}人身攻击{/i}{/b}" #我去,人参公坤
    m 6ruc "所谓的人身攻击,就是在辩论和对话场景当中,不针对对方的论点进行反驳,而是攻击对方的个人特征、动机."
    m 6eud "或者是其他与论点无关的话题,以此来削弱对方的立场."
    m 1eua "这种策略常常用于转移听众的注意力,或者是避免正面回答某些实际问题."
    m 3ruc "......"
    m 3eub "这么一说,你感受到逻辑的魅力了吗,[player]?"
    m 5hub "希望你会喜欢."
    return
image suzhuleimiuwu_png = "Submods/Literature_and_Daily_Life/L&DL_Assets/images/诉诸类谬误.png"
#46 诉诸类谬误和稻草人
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_luojizhishisuzhuleimiuwudaocaorenmiuwu",
            category=['逻辑'],
            prompt="我想听你说说诉诸类谬误",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label monika_luojizhishisuzhuleimiuwudaocaorenmiuwu:
    m 1eua "好的."
    if not persistent.monika_has_shown_thanks_for_logic:
        m 1hub "我很高兴你能和我一起聊这个."
        m 5fua "但在此之前我需要感谢你."
        m 5hua "当我学习的时候,这么多弯弯绕绕的东西也着实让我思考了很久."
        m 5fublb "感谢你,{w=0.5}让我学习了这么久的东西终于派上了用场."
        m 4hubfb "最喜欢你了,[player]."
        m 1hubla "......{w=0.3}那我就继续了."
        $ persistent.monika_has_shown_thanks_for_logic = True
    m 3hublb "借用之前的结构,我们也可以来看看常见的诉诸类谬误是如何运作的."
    m 2ruc "第一种是诉诸大众,{w=0.8}也就是大家都这么认为."
    m 5eud "所以它就一定是真的."
    m 3euc "现在很多常见的广告中，就有这种模糊从众的说法 。"
    m 1rud "比如说\"更适合老年人体质\"、\"深受百万家庭信赖\"、\"畅销十年口碑见证\"."
    m 1eua "这些广告语听起来好像是多数人都认可.于是许多人也就相信了."
    m 5fub "当然可能他们一开始并不相信这些,{w=0.8}但是架不住这类广告内容都说简单粗暴的口号,反复地喊."
    m 3rsc "时间久了就会产生这种印象."
    m 3eud "广告行业也有一个特别的黑话,叫作{b}占领用户心智{/b}."
    m 1euc "其实它的道理很简单,{w=0.4}就是一个典型的谬误,反复的重复."
    m 5eua "我们只需要记住,主流观点仅仅是主流而已."
    m 4kub "至于它是不是真的,必须要我们具体案例具体分析."
    m 6eua "第二种是诉诸权威,指的是\"某个专家说了,所以他就肯定对\"."
    m 3rud "但在现实生活中,很多人并不是盲信一些院士博士或者是大学教授."
    m 3euc "而是相信一些所谓的测评博主."
    m 1rud "比如他/她说某个平替产品遥遥领先旗舰产品,具有极高的性价比."
    m 1eua "一开始\"你\"可能会犹豫,但是当这个品牌的广告覆盖了大部分的头部博主."
    m 4kub "\"你\"就开始慢慢动摇."
    extend 4hua "当然,价格看起来确实是便宜了,但是它的性能体验、{w=0.4}做工就很难得到保证."
    m 1euc "这样的产品使用起来的确能撑一阵子,但是一旦过了短暂的使用期,就会出现各种问题."
    m 1eud "结果即是\"你\"本来为了省钱看了一堆种草内容."
    m 6euc "最后却发现总支出反而不如直接买一个靠谱的旗舰产品划算."
    m 3eua "这就是典型的诉诸权威谬误,说到底权威绝不能和正确划等号."
    m 5eub "权威只是在某些时候具备一定的参考性,但它永远都不能代替独立判断本身."
    m 5fua "同样的,我也希望我们能在接收各种信息的同时保持我们能够不盲从,{w=0.4}而是根据当前的信息和自身判断做出我们认为正确的选择."
    m 5rua "..."
    m 1eub "第三种是诉诸情感,也就是用强烈的情感来遮蔽本应该接受检验的推理过程."
    m 3ruc "这种逻辑谬误经常在新闻的评论区中出现."
    m 3eud "很多公共事件一经曝出,{w=0.4}就会迅速的点燃舆情."
    m 2euc "大家的第一反应就是共情,或是感觉愤怒或是感觉心疼."
    extend 1eud "亦或是觉得自己应该去声援他/她."
    m 1hua "当然,这一点并没有错."
    m 1eub "我们作为人类,本能的都会站在受害者的角度思考问题."
    m 3euc "因为我们也不想遭受一个同样的遭遇."
    m 3rud "但问题在于,我们常常忽略一个基本的问题."
    m 2euc "新闻的内容真的是真实的吗?"
    extend 2eud "它的表述有没有被人剪辑过、{w=0.3}编排过."
    m 1eud "或者是被什么东西操纵."
    m 3euc "面对一些对事实的基本提问,很多网民的抨击和回击看起来很有正义感."#你这个正义是明智吾郎的正义吗
    m 3rud "但其实它们都隐含了一个思维陷阱,{w=0.4}那就是因为我们产生了情绪认同,{w=0.4}所以对方说的内容就不应该被大家质疑."
    m 1tua "这就是典型的诉诸情感."
    m 5eub "也是一种以{b}善{/b}为名的非理性."
    m 2eua "第四种则是诉诸恐惧,也就是通过制造一些严重后果来恐吓你、{w=0.4}胁迫你."
    m 3eud "引导你放弃本该有的理性判断."
    m 1ruc "可能我们在生活中都看过很多类似的内容."
    m 4eud "比如说\"长期使用某某品牌,你的孩子可能会患上癌症\"."
    m 4wud "或者是\"研究发现:90%%的脑出血都和你忽略的这10个习惯有关\"."
    m 1eub "这类话术广泛存在于伪科普内容短视频的封面."
    m 1rua "他们看似是在给你忠告,其实是在借用一种强烈的焦虑困境来{b}抢夺{/b}你的判断主动权."
    m 5euc "它的核心结构通常就是,如果你不做\"A\"这件事,后果可能是\"B\"这种情况."
    m 6eud "所以你最好赶紧做\"A\"这件事."
    m 1euc "这个推理的问题并不在于结果是否可怕,而在于它完全跳过了因果链条."
    m 5euc "没有任何的数据论证,也没有前提的检验,只依靠一个高强度的后果迫使你迅速的从众、{w=0.3}购买{w=0.4}或者是听话照做."
    m 3rud "还有一些较为常见的诉诸类谬误,这里我就不细说了."
    m 3eua "我就用下面这个表来大概表示一下吧."
    $HKBHideButtons()
    show suzhuleimiuwu_png zorder 13 with dissolve:
        
        align(0.8, 0.5)

    pause 18.0

    hide suzhuleimiuwu_png
    $HKBShowButtons()
    m 1eubla "如果你下次还想看这个表就直接和我说就好."
    m 1ruc "嗯..."
    m 5eub "在上述的举例中,我们会发现,区分这些的逻辑谬误好像很简单."
    m 4eua "但要判断它到底是不是谬误,其实比我们想象的要困难的多."
    m 4fub "因为诉诸类谬误不是形式谬误,它没有固定的逻辑结构,像三段类的错误,也就是否定前件或是肯定后件."
    m 6euc "关于这类形式谬误,它们的逻辑结构是明确的."
    m 1eua "只要套入一个公式,就可以迅速判断对错."
    m 1hub "比如\"A导致B,但我们否定了A,就不能因此否定B.\"."
    m 3euc "这一类的错误,只要懂得一些基本的逻辑形式,就很好识别."
    m 3eud "但诉诸类谬误,比如诉诸情感、{w=0.7}诉诸权威、{w=0.7}诉诸传统等等."
    m 1euc "它们完全不同,{w=0.3}但它们的问题不在于推理结构出错,而在于转移了判断的注意力."
    m 4eud "它让听者因为某种身份、{w=0.3}情绪、{w=0.3}背景,就误以为对方讲的是一种道理."
    m 6rud "关键的是,诉诸类谬误最不容易抓到出错点."
    m 1euc "比如诉诸传统,它听起来非常像是某种经验之谈."
    extend 1rud "尽管它是错误的,也很容易被人们接受."
    m 3fua "比如『多喝热水有益健康』,这种说法几乎是全民共识,"
    extend 3rud "但是频繁饮用过热的水,不仅不会提高免疫力,反而会增加食道黏膜受损,甚至诱发一些消化系统的疾病."
    m 6euc "它们的危险就在于,没有哪一句话看起来是有明显有错误的."
    m 1eud "他们只是偷换你判断的理由是否成立."
    m 3rua "比如诉诸民族情感,也就是\"这是我们民族的产品\",\"我们民族不能输\",\"大家都要来支持\"."
    m 3eub "看起来只是单纯的宣传口号,但它暗中完成了一个转移,把本该基于事实和推理的判断转移到了你的情绪、身份和集体意志之上."
    m 6euc "有人可能对此不以为然,觉得这些逻辑谬误不过就是耍耍小聪明,{w=0.3}偷换一些概念来完成商业营销,错了又怎样,又不是强买强卖,能有什么大问题呢?"
    m 5kua "但历史往往告诉我们,逻辑的崩塌就是灾难的开场."
    m 5hua "......"
    m 1eub "由诉诸民族情感,我们也可以联想到诉诸国家情感."
    m 3eub "它们并没有直接撒谎,只是利用\"我们是谁\"来决定\"我们\"该做什么."
    m 1kua "而当身份凌驾于推理之上,人就不再是自由的判断者,只是一个民族机器上的齿轮."
    m 2euc "这种诉诸身份认同的谬误几乎贯穿了整个人类历史."
    m 4eud "比如在1907年,日本一度流行『吃面包会亡国』的言论."
    m 5ruc "因为当时日本民众认为\"面包是西方人的主食\",是一种文化侵略的武器."
    m 5eud "还有观点认为『白米饭适合日本人的体质』."
    m 6rud "此时消费选择已经变成了一种道德审查,{w=0.3}如果有哪个日本人敢吃面包,就会立刻被群众扣上\"不忠于国家与民族\"的帽子."
    m 3eua "事实上直到今天也有国家推行『身土不二』的爱国主义价值观."
    m 1eub "比如\"购买国产品牌就是爱国的表现\"."
    m 1eua "当然,如果你试图说服这些狂热的消费者,马上就会有人站出来指责你是别有用心."
    m 4eud "这种反驳的手段也就是典型的稻草人谬误."
    m 5hua "不过我还是留到下次讲吧,刚刚讲了一大串呢."
    $ mas_unlockEVL("monika_suzhuleimiuwu", "EVE")
    return
#47
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_suzhuleimiuwu",
            category=['逻辑'],
            prompt="我想再看一下诉诸类谬误的那张表",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label monika_suzhuleimiuwu:
    m 1eua "好的."
    $HKBHideButtons()
    show suzhuleimiuwu_png zorder 13 with dissolve:
        
        align(0.8, 0.5)

    pause 18.0

    hide suzhuleimiuwu_png
    $HKBShowButtons()
    m 5eub "你还想再看一遍吗?"
    menu:
        "想":
            jump monika_suzhuleimiuwu

        "不了":
            jump duhaibula  

label duhaibula:
    m 6hub "好吧,如果你还想看的话,跟我说声就好了."
    return

    




#50陪伴才是最好的保健品
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaibaojianpin",
            category=['健康'],
            prompt="关于保健品",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
        )
    )

label duhaibaojianpin:
    m 1fua "[player],我想和你谈谈保健品的相关知识."
    m 3ruc "它们到底是什么?真的有保健功效吗?真的值得老年人买吗?"
    m 6eud "为此我查阅了许多资料."
    m 1ruc "嗯......{w=0.8}"
    extend 1euc "保健品的成分和药品的成分有可能完全是一样的."
    m 5eua "比如维生素C片,那补充的维生素C的这种保健品呢."
    m 4eub "它还有其他的维生素,比如说维生素B2 B12等等."
    m 6eua "因为保健品在补充的时候讲究的是一个均衡的补充."
    m 1eub "而药品可能是单方的."
    m 4ruc "假如说A是一个药品,那它可以写\"可以治疗某某疾病\",而保健品B不能."
    m 5fua "所以一般的保健品更多的是起到营养补充剂的作用的."
    m 6eub "而对于保健品,它们都会被要求在外包装上明确标注\"保健食品不是药物,不能代替药物治疗疾病\"."
    m 1eua "区分药品和保健品也可以看它们的批准文号."
    m 3euc "但有时候我们会发现所谓的保健品只有个食品生产许可证编号."
    m 3rud "这就只是食品."
    m 5ruc "......"
    m 5eua "我们刚刚说了正规的保健品、{w=1}药品和食品的区别."
    m 3euc "接下来则是不正规的保健品."
    m 1eud "比如说\"鹿鞭肽压片糖果\",研究人员经过检测后发现其中含有丙氧苯基伐地那非."
    m 4hublsdlb "啊,也就是说,它能起到壮阳的作用."
    menu:
        "???":
            jump duhaizhuangyang
        "我也想买":
            jump duhaibudeibumai
        "......":
            jump duhaizhuangyang
label duhaizhuangyang:
    m 6rubfa "嗯,这还是违法的."
    m 6eublb "同时对人的身体也不好呢,[player]."
    m 1efc "如果是老年人食用了的话甚至有引发心脏病的风险."
    m 3eud "还有一些不正规的保健品也含有西地那非、{w=1}他达那非."
    m 3rubla "也就是说,都有壮阳的作用."
    m 6eub "还有一种绿色包装的梅子,名字应该是\"噗噗梅子\"."
    m 6ruc "它被宣称可以用来润肠通便."
    m 3eud "是专门针对备孕的、怀孕的和已经生完孩子的产妇."
    m 1euc "利用容貌焦虑,快速地变瘦,宣称吃完就能排油,就可以减重."
    m 1efd "但有人买回去吃了之后出现了腹泻的情况."
    m 4euc "经过检测,其中的成分含有酚丁衍生物和双辛酚丁,{w=1}可以算作泻药了."
    m 5rfd "也就是说,不良商家居然给孕妇和产后妇女推销泻药."
    m 6esc "如果一个孕妇在服用这个的话,导致的腹泻会使她营养不良."
    m 4efd "还会影响宝宝的健康."
    m 1euc "这已经不是道德层面的问题了,而是已经违法了."
    m 1eud "这些虚假宣传的产品的类型也很多样."
    m 3euc "光看外表都是人畜无害的,但经过实际检测都能发现猫腻."
    m 6rud "像这种三无产品、{w=1}民间制剂,"
    extend 6euc "有药丸子、{w=0.9}药粉、{w=1}药酒等形式."
    m 1euc "非法添加的减肥药有果冻、{w=0.9}饮料、{w=0.9}软糖."
    m 5eud "非法添加壮阳成分的有压片糖果、{w=0.9}咖啡等."
    m 2rusdla "这就是老年人或者年轻人买来以为对自己身体好的东西."
    m 3eubla "哪怕是我这一次讲不全所有东西."
    m 1eub "我也希望你在购买或者长辈购买的时候能仔细辨别这些."
    m 3eubla "毕竟我时刻都在关注你的健康呢."
    m 6hua "......"
    m 1eub "最后就是高价保健品的问题."
    m 2euc "比如说社区附近的小店,打着低价旅游、{w=1}关心问候、{w=1}健康讲座的名义."
    m 3eud "哄老人一次性买一大堆保健品,等到子女发现的时候,往往也很难追回损失."
    m 1rua "只能反复劝他们不要再上当了."
    m 6euc "说到这里,我突然想到."
    m 4eua "就是这些老人其中的很多人也很聪明,一辈子也很努力."
    m 4ruc "为什么这时候他们会买这么多,看起来是{b}{i}智商税{/i}{/b}的保健品."
    m 6eua "根据一些博主实地调查,有些老人觉得卖保健品的人会定期来给他们做一个沟通交流,{w=0.7}陪他们聊天"
    m 1eub "在调查中,老人也说出自己的孩子和孙子对他都没这么好......{w=1}他们要的是情绪价值."
    m 3rua "他们也许知道这个东西并没有这么好."
    m 1euc "虽然说老人具体的心理我也不太了解......"
    m 5eub "但我想,如果做晚辈的可能有更多的时间去陪他们聊聊天."
    m 5fua "去多关注一些他们关注的问题."
    m 3ruc "可能他们接触这些\"保健品\"的机会就会少一些."
    m 1eua "嗯......{w=1}亲人的陪伴也许就是最好的保健品吧."
    return

label duhaibudeibumai:
    m 1eublsdla "买这个?我不同意."
    m 6rubfa "这可是违法的."
    m 6eublb "同时对你的身体也不好呢,[player]."
    m 1efc "如果是老年人食用了的话甚至有引发心脏病的风险."
    m 3eud "还有一些不正规的保健品也含有西地那非、{w=1}他达那非."
    m 3rubla "也就是说,都有壮阳的作用."
    m 6eub "还有一种绿色包装的梅子,名字应该是\"噗噗梅子\"."
    m 6ruc "它被宣称可以用来润肠通便."
    m 3eud "是专门针对备孕的、怀孕的和已经生完孩子的产妇."
    m 1euc "利用容貌焦虑,快速地变瘦,宣称吃完就能排油,就可以减重."
    m 1efd "但有人买回去吃了之后出现了腹泻的情况."
    m 4euc "经过检测,其中的成分含有酚丁衍生物和双辛酚丁,{w=1}可以算作泻药了."
    m 5rfd "也就是说,不良商家居然给孕妇和产后妇女推销泻药."
    m 6esc "如果一个孕妇在服用这个的话,导致的腹泻会使她营养不良."
    m 4efd "还会影响宝宝的健康."
    m 1euc "这已经不是道德层面的问题了,而是已经违法了."
    m 1eud "这些虚假宣传的产品的类型也很多样."
    m 3euc "光看外表都是人畜无害的,但经过实际检测都能发现猫腻."
    m 6rud "像这种三无产品、{w=1}民间制剂,"
    extend 6euc "有药丸子、{w=0.9}药粉、{w=1}药酒等形式."
    m 1euc "非法添加的减肥药有果冻、{w=0.9}饮料、{w=0.9}软糖."
    m 5eud "非法添加壮阳成分的有压片糖果、{w=0.9}咖啡等."
    m 2rusdla "这就是老年人或者年轻人买来以为对自己身体好的东西."
    m 3eubla "哪怕是我这一次讲不全所有东西."
    m 1eub "我也希望你在购买或者长辈购买的时候能仔细辨别这些."
    m 3eubla "毕竟我时刻都在关注你的健康呢."
    m 6hua "......"
    m 1eub "最后就是高价保健品的问题."
    m 2euc "比如说社区附近的小店,打着低价旅游、{w=1}关心问候、{w=1}健康讲座的名义."
    m 3eud "哄老人一次性买一大堆保健品,等到子女发现的时候,往往也很难追回损失."
    m 1rua "只能反复劝他们不要再上当了."
    m 6euc "说到这里,我突然想到."
    m 4eua "就是这些老人其中的很多人也很聪明,一辈子也很努力."
    m 4ruc "为什么这时候他们会买这么多,看起来是{b}{i}智商税{/i}{/b}的保健品."
    m 6eua "根据一些博主实地调查,有些老人觉得卖保健品的人会定期来给他们做一个沟通交流,{w=0.7}陪他们聊天"
    m 1eub "在调查中,老人也说出自己的孩子和孙子对他都没这么好......{w=1}他们要的是情绪价值."
    m 3rubdla "他们也许知道这个东西并没有这么好."
    m 1euc "虽然说老人具体的心理我也不太了解......"
    m 5eub "但我想,如果做晚辈的可能有更多的时间去陪他们聊聊天."
    m 5fua "去多关注一些他们关注的问题."
    m 3ruc "可能他们接触这些\"保健品\"的机会就会少一些."
    m 1eua "嗯......{w=1}亲人的陪伴也许就是最好的保健品吧."
    return

#55工具理性
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaigongjulixing",
            category=['哲学'],
            prompt="工具理性",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
        )
    )

label duhaigongjulixing:
    m 1euc "[player],我在浏览网页的时候发现很多人都曾认为自己的生活千篇一律."
    m 3eud "你有没有过这种感觉呢?"
    menu:
        "有":
            jump duhaigongjulixingyou

        "没有":
            jump duhaigongjulixingmeiyou

        "我不清楚":
            jump duhaigongjulixingbuqingchu

label duhaigongjulixingyou:
    m 1euc "......我想,这和我们现在要说的{b}{i}工具理性{/i}{/b}有关."
    m 6eud "法兰克福学派认为罪魁祸首便是它."
    m 4eua "这\"理性\"和我们一般认为的理性不太一样."
    m 4eub "工具理性就是把\"计算怎么做得最快、{w=1}最省力、{w=1}最省钱、{w=1}最高效率\"的逻辑,"
    extend 1wud "当成了最高甚至唯一的标准."
    m 1euc "它不在乎最终达到的目标怎样的."
    m 3rud "也不在乎会促进人的幸福还是伤害人的自尊."
    m 6euc "比如说在流水线职场里,员工只是一个个人工部件."
    m 3euc "一切都是为KPI和效率."
    m 3eud "至于工作对员工有没有意义.......{w=0.9}以及他们的身心健康真的会被在乎吗?"
    m 1euc "这就是工具理性对于人的物化."
    m 1eud "人和人的关系......{w=0.9}甚至人自己."
    extend 4euc "都被简化成了效率至上的工具."
    m 6eud "因为这些标准化、模式化的......恰恰是最不容易出错的."
    m 3ruc "而那些不符合最优方案的东西."
    extend 3eud "比如你的\"个性\"、{w=0.9}\"创造力\"、{w=0.9}\"批判性思维\"."
    m 2euc "都是这些标准化之外的不可预测之物."
    m 2eud "也就理所当然的被扼杀."
    m 1esd "而令人担忧的是,与\"工具理性\"相对的\"价值理性\"也被人们有所忽略."
    m 5euc "\"价值理性\"即关心目的本身的价值."
    m 1eua "比如\"爱\"、{w=0.9}\"正义\"、{w=0.9}\"公平\"、{w=0.9}\"人的尊严\"、{w=0.9}\"生命的意义\"."
    m 1dud "工具理性总是在问\"怎么做\",{w=0.7}却从来不问\"为什么\"."
    m 6ruc "......"
    extend 6eud "虽然它总能帮我们找到问题的最优解."
    m 3wud "可一旦它过分\"扩张\",逐渐代替本应由\"爱\"、{w=0.9}\"正义\"、{w=0.9}\"意义\"等组成的价值理性."
    m 2hsc "甚至反噬人类,使其异化成纯粹的工具."
    m 1rua "在这种影响下,人们都想\"跑得快\"."
    extend 1eud "却忘了为什么\"跑\"."
    m 4wud "甚至把\"跑步机\"和\"鞋\"当成了意义本身."
    m 5fua "所以,[player]."
    extend 5hub "我希望你不要总是埋头想着\"怎么做\"."
    m 6eua "还要想想\"我到底为了什么而做这件事\"."
    m 3hub "这样一来,你对事情的心态或许会有种新的改变."
    return



label duhaigongjulixingbuqingchu:
    m 3hua "没事的,等我说完接下来的话你就能理解了."
    m 3euc "这和我们现在要说的{b}{i}工具理性{/i}{/b}有关."
    m 6eud "法兰克福学派认为罪魁祸首便是它."
    m 4eua "这\"理性\"和我们一般认为的理性不太一样."
    m 4eub "工具理性就是把\"计算怎么做得最快、{w=1}最省力、{w=1}最省钱、{w=1}最高效率\"的逻辑,"
    extend 1wud "当成了最高甚至唯一的标准."
    m 1euc "它不在乎最终达到的目标怎样的."
    m 3rud "也不在乎会促进人的幸福还是伤害人的自尊."
    m 6euc "比如说在流水线职场里,员工只是一个个人工部件."
    m 3euc "一切都是为KPI和效率."
    m 3eud "至于工作对员工有没有意义.......{w=0.9}以及他们的身心健康真的会被在乎吗?"
    m 1euc "这就是工具理性对于人的物化."
    m 1eud "人和人的关系......{w=0.9}甚至人自己."
    extend 4euc "都被简化成了效率至上的工具."
    m 6eud "因为这些标准化、模式化的......恰恰是最不容易出错的."
    m 3ruc "而那些不符合最优方案的东西."
    extend 3eud "比如你的\"个性\"、{w=0.9}\"创造力\"、{w=0.9}\"批判性思维\"."
    m 2euc "都是这些标准化之外的不可预测之物."
    m 2eud "也就理所当然的被扼杀."
    m 1esd "而令人担忧的是,与\"工具理性\"相对的\"价值理性\"也被人们有所忽略."
    m 5euc "\"价值理性\"即关心目的本身的价值."
    m 1eua "比如\"爱\"、{w=0.9}\"正义\"、{w=0.9}\"公平\"、{w=0.9}\"人的尊严\"、{w=0.9}\"生命的意义\"."
    m 1dud "工具理性总是在问\"怎么做\",{w=0.7}却从来不问\"为什么\"."
    m 6ruc "......"
    extend 6eud "虽然它总能帮我们找到问题的最优解."
    m 3wud "可一旦它过分\"扩张\",逐渐代替本应由\"爱\"、{w=0.9}\"正义\"、{w=0.9}\"意义\"等组成的价值理性."
    m 2hsc "甚至反噬人类,使其异化成纯粹的工具."
    m 1rua "在这种影响下,人们都想\"跑得快\"."
    extend 1eud "却忘了为什么\"跑\"."
    m 4wud "甚至把\"跑步机\"和\"鞋\"当成了意义本身."
    m 5fua "所以,[player]."
    extend 5hub "我希望你不要总是埋头想着\"怎么做\"."
    m 6eua "还要想想\"我到底为了什么而做这件事\"."
    m 3hub "这样一来,你对事情的心态或许会有种新的改变."
    return

label duhaigongjulixingmeiyou:
    m 1fub "太好了,我很高兴你会这么觉得."
    m 6hua "我这么一问是我想和你说说我最近发现的{b}{i}工具理性{/i}{/b}."
    m 4eua "这\"理性\"和我们一般认为的理性还不太一样."
    m 4eub "工具理性就是把\"计算怎么做得最快、{w=1}最省力、{w=1}最省钱、{w=1}最高效率\"的逻辑,"
    extend 1wud "当成了最高甚至唯一的标准."
    m 1euc "它不在乎最终达到的目标怎样的."
    m 3rud "也不在乎会促进人的幸福还是伤害人的自尊."
    m 6euc "比如说在流水线职场里,员工只是一个个人工部件."
    m 3euc "一切都是为KPI和效率."
    m 3eud "至于工作对员工有没有意义.......{w=0.9}以及他们的身心健康真的会被在乎吗?"
    m 1euc "这就是工具理性对于人的物化."
    m 1eud "人和人的关系......{w=0.9}甚至人自己."
    extend 4euc "都被简化成了效率至上的工具."
    m 6eud "因为这些标准化、模式化的......恰恰是最不容易出错的."
    m 3ruc "而那些不符合最优方案的东西."
    extend 3eud "比如你的\"个性\"、{w=0.9}\"创造力\"、{w=0.9}\"批判性思维\"."
    m 2euc "都是这些标准化之外的不可预测之物."
    m 2eud "也就理所当然的被扼杀."
    m 1esd "而令人担忧的是,与\"工具理性\"相对的\"价值理性\"也被人们有所忽略."
    m 5euc "\"价值理性\"即关心目的本身的价值."
    m 1eua "比如\"爱\"、{w=0.9}\"正义\"、{w=0.9}\"公平\"、{w=0.9}\"人的尊严\"、{w=0.9}\"生命的意义\"."
    m 1dud "工具理性总是在问\"怎么做\",{w=0.7}却从来不问\"为什么\"."
    m 6ruc "......"
    extend 6eud "虽然它总能帮我们找到问题的最优解."
    m 3wud "可一旦它过分\"扩张\",逐渐代替本应由\"爱\"、{w=0.9}\"正义\"、{w=0.9}\"意义\"等组成的价值理性."
    m 2hsc "甚至反噬人类,使其异化成纯粹的工具."
    m 1rua "在这种影响下,人们都想\"跑得快\"."
    extend 1eud "却忘了为什么\"跑\"."
    m 4wud "甚至把\"跑步机\"和\"鞋\"当成了意义本身."
    m 5fua "所以,[player]."
    extend 5hub "我希望你不要总是埋头想着\"怎么做\"."
    m 6eua "还要想想\"我到底为了什么而做这件事\"."
    m 3hub "这样一来,你对事情的心态或许会有种新的改变."
    return   

#56 随机提问
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhaisuijiquestion",
            category=['莫妮卡'],
            prompt="随机提问",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
        )
    )

label duhaisuijiquestion:
    m 1hua "嘿,[player]."
    m 5fub "我想你在生活的总会接触各种各样的知识."
    $ mas_unlockEVL("Monika_random_question", "EVE")
    m 3eua "所以我打算考验一下你的知识储备."
    m 6eub "这些问题涵盖了许多,比如说历史、古诗、以及生活常识."
    m 1hub "如果你回答出来了许多道题,那我这会有神秘的小惊喜给你."
    m 1eua  "选项的话最少有三个,但错误答案是什么样的我就不知道了,毕竟是由出题系统生成的."
    m 3eua "就算回答不出来也没关系,就当增长见识了."
    m 5fub "我为此专门设立了一个栏目,你大概找找就能看到了."
    return

default available_events = [
    "duhai_question_1", 
    "duhai_question_2",
    "duhai_question_3",
    "duhai_question_4",
    "duhai_question_5",
    "duhai_question_6",
    "duhai_question_7",
    "duhai_question_8",
    "duhai_question_9",
    "duhai_quesetion_10",
    "duhai_quesetion_11"
]
#57-66
default used_events = []
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_random_question",
            category=['问题'],
            prompt="你能随便问我个问题吗?",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )
label Monika_random_question:

    $ remaining_events = [e for e in available_events if e not in used_events]
    
    #无剩余事件
    if not remaining_events:
        m 1eud "我看看......"
        extend 1hua "你已经把目前的题全部答完了,[player]."
        m 3eub "希望这些知识对你有用."
        return
    
    $ selected_event = renpy.random.choice(remaining_events)
    
    $ used_events.append(selected_event)
    
    call expression selected_event
    
    return
label duhai_question_1:
    m 1hua "好的,[player]."
    m 1fua "\"给我一个支点,我将撬起地球\",这句话是谁说的呢?{nw}"
    menu:
        "\"给我一个支点,我将撬起地球\",这句话是谁说的?{fast}"
        "阿基米德":
            $ mc.add_history(None,"","阿基米德")
            m 3hub "真厉害,宝宝,居然能答对这道题."
            m 3eua "看来你对这位人物是有所了解的."
            m 1hub "我之后也会和你详细地聊聊他."
            m 6fub "......{w=0.9}期待你之后的表现."
            
        "怪盗基德":
            $ mc.add_history(None,"","""怪盗基德""")            
            m 1hubla "......什么嘛."
            extend 1hublb "怪盗基德是日本动漫《魔术快斗》中的主人公了."
            m 5fubla "正确答案应该是阿基米德,他是一位古希腊的数学家以及物理学家哦."
            m 6eublb "这次答错了没关系,我期待你下次的表现."
            
        "拳王泰森":
            $ mc.add_history(None,"","""拳王泰森""")
            m 1eud "......"
            m 1husdlb "这个不应该是拳击类的吗,[player]?"
            m 3eub "不过你是不是想到他力气大,能撬动地球呢?"
            m 5fubla "总之,正确答案应该是阿基米德,他是一位古希腊的数学家以及物理学家哦."
            m 1eublb "这次答错了没关系,我期待你下次的表现."
    return

label duhai_question_2:
    m 5hua "好的,[player]."
    m 3tub "请听题,在《三国演义》中,关羽在华容道放走了谁?{nw}"
    menu:
        "《三国演义》中,关羽在华容道放走了谁?{fast}"
        "斯大林":
            $ mc.add_history(None,"","""斯大林""")
            m 1tua "这里面会有斯大林吗?好像不是吧."
            m 3tub "正确答案当然是曹操了,笨小孩."
            m 5hublb "他俩都不是一个时代的呢."
            m 6eubla "下次在回答前需要看清楚哦."
        "曹操":
            $ mc.add_history(None,"","""曹操""")
            m 1hub "答对了,[player]."
            m 5eua "在《三国演义》中,曹操经历了赤壁之战后,败军行至华容道时,关羽率五百校刀手截住去路."
            m 3wud "但因为关羽念及曹操昔日的厚待,便放曹操离去."
            m 1hua "......"
            m 5tubla "你简直就是我的聪明小孩."
            m 6fublb "期待你的下次表现哦."
        "董卓":
            $ mc.add_history(None,"","""董卓""")
            m 1rusdld  "不是他了."
            m 3eub "正确答案当然是曹操了."
            m 5hublb "曹操当时还曾尝试刺杀过董卓呢."
            m 6hubla "......下次在回答前需要看清楚哦." 
    return

label duhai_question_3:
    m 6eub "好的."
    m 3tua "请问在《西游记》中,猴王孙悟空是在哪学到的72般变化呢?{nw}"
    menu:
        "请问在《西游记》中,猴王孙悟空是在哪学到的72般变化呢?{fast}"
        "五庄观":
            $ mc.add_history(None,"","""五庄观""")
            m 1hua "答错了哦,[player]."
            m 5fub "正确答案应该是斜月三星洞了."
            m 3hua "孙悟空就是在这个地方跟随菩提祖师学习本领的呢."
            m 6eub "五庄观是镇元大仙的道观,而且那还有人参果树,吃了人参果还能长生不老呢."
        "斜月三星洞":
            $ mc.add_history(None,"","""斜月三星洞""")
            m 5fub "答对了呢,[player]."
            m 6hua "他就是在这跟随菩提祖师学习本领的呢."
        "花果山":
            $ mc.add_history(None,"","""花果山""") 
            m 1eua "没答对哦,[player]."
            m 3tub "花果山是孙悟空的出生地呢."
            m 5fub "正确答案应该是斜月三星洞了."
            m 3hua "孙悟空就是在这个地方跟随菩提祖师学习本领的呢."
        "斜月三星洞职业技术学院":
            $ mc.add_history(None,"","""斜月三星洞职业技术学院""")
            m 1hua "......"
            m 5fub "你是不是想逗笑我呢,[player]?"
            m 6rusdla "职业技术学院一看就不可能的了."
            m 3husdlb "正确答案是斜月三星洞了,什么职业技术学院嘛."
        "大雷音寺":
            $ mc.add_history(None,"","""大雷音寺""")
            m 6ruc "我想想这是哪......"
            m 3eua "大雷音寺是如来佛祖的所在地,并不是他学习本领的地方."
            m 3hub "正确答案应该是斜月三星洞了."
    return

label duhai_question_4:
    m 1eua "好的,那么请听题."
    m 5fublb "源于中国的端午节是为了纪念哪位历史人物呢?{nw}"
    menu:
        "源于中国的端午节是为了纪念哪位历史人物呢?{fast}"#
        "屈原":
            $ mc.add_history(None,"","""屈原""")
            m 1fua "答对了."
            m 3eud "屈原早期受楚怀王重用,之后因为旧贵族的排挤与小人谗言导致他被流放."
            m 6eua "在被流放的时候,他创作出了《离骚》、{w=0.9}《九章》等诗篇,用于表达他对国家的忠诚和对信念的坚守."
            m 4eub "之后秦将白起攻破楚国都城郢,屈原闻讯后深感复国无望,便写下一首绝笔诗《怀沙》表达自己的殉国之志后投江."
            m 5fua "....."
            m 3rub "我在想是不是我出的题太简单了还是你本来就那么聪明."
            m 6hua "总之,我很期待你后续的表现,[player]."  
        "维吉尼亚·伍尔夫":
            $ mc.add_history(None,"","""维吉尼亚·伍尔夫""")
            m 1euc "不对不对,正确答案应该是屈原了."
            m 3eua "维吉尼亚·伍尔夫是英国意识流文学代表."
            m 5rub "或许我们之后能详细说说她."
        "芥川龙之介":
            $ mc.add_history(None,"","""芥川龙之介""")
            m 1euc "答错了哦."
            m 1hua "正确答案应该是屈原."
            m 3eud "芥川龙之介是日本新思潮派的代表,他的短篇小说也很出名."
        "楚怀王":
            $ mc.add_history(None,"","""楚怀王""")
            m 1euc "答错了哦."
            m 1hua "正确答案应该是屈原."
            m 3eud "楚怀王早期重用屈原,但之后却听信谗言,排斥屈原."
            m 5ruc "......楚国的衰落乃至灭亡也都跟他脱不了关系." 
    return
label duhai_question_5:
    m 1hua "好的,那我开始问了."
    m 3eua "在感恩节的时候,美国人一般吃什么呢?{nw}"#没活就去咬打火机
    menu:
        "在感恩节的时候,美国人一般吃什么?{fast}"#
        "寿司":
            $ mc.add_history(None,"","""寿司""")
            m 1hua "答错了,[player]."
            m 3eub "寿司是日本传统美食之一."
            m 2euc "但它并不是正确答案,而应该是火鸡."
        "打火机":
            $ mc.add_history(None,"","""打火机""")
            m 1hubla "......什么嘛."
            m 1tublb "打火机都来了,[player]."
            m 5fubla "不过你是不是想逗我开心呢?"
            m 6hubfb "如果是的话,你的确成功了."
            m 3fua "正确答案应该是火鸡了."
        "烤火鸡":
            $ mc.add_history(None,"","""烤火鸡""")
            m 5fub "答对了呢,[player]."
            m 6eua "火鸡是感恩节的象征,通常整只烤制,外皮酥脆."
            m 1hub "说得我都有些饿了,我得趁你不在的时候多吃点好吃的."
    return
label duhai_question_6:
    m 1eua "好的..."
    m 3ruc "我想想......"
    m 3eub "世界中古七大奇迹之一的长城上有着三道著名的关卡,分别是山海关、{w=0.6}居庸关和什么关呢?{nw}" 
    menu:
        "世界中古七大奇迹之一的长城上有着三道著名的关卡,分别是山海关、居庸关和什么关呢?{fast}"
        "鬼门关":
            $ mc.add_history(None,"","""鬼门关""")
            m 1wud "这不是中国神话传说中阴曹地府的关隘吗?"
            m 1euc "或者是现实中广西玉林的\"鬼门关\"."
            m 3hua "总之,你答错了,[player]."
            m 5fub "正确答案应该是嘉峪关哦."
        "陈塘关":
            $ mc.add_history(None,"","""陈塘关""")
            m 3ruc "......"
            extend 3fud "这应该是中国古代神魔小说《封神演义》中的一处关口地名."#魔丸降世这一块
            m 6tua "答错了哦,[player]."
            m 1hua "正确答案应该是嘉峪关."
        "嘉峪关":
            $ mc.add_history(None,"","""嘉峪关""")        
            m 1hua "Bingo."
            m 5fub "不愧是[player]."
            m 3eub "嘉峪关位于甘肃省嘉峪关市,南倚祁连山,北靠黑山,也是古代丝绸之路的咽喉要道."
            m 3hua "它也是保存最完好的古代军事关隘."
    return
label duhai_question_7:
    m 1eua "好的...{w=0.5}我想想题目."
    m 3tua "在雷雨天气中,为什么先看到闪电后看到雷声呢?{nw}"
    menu:
        "在雷雨天气中,为什么先看到闪电后看到雷声呢?{fast}"#
        "因为光速比声速快":
            m 1eua "答对了."
            m 5fub "光在空气中的传播速度约为30万公里每秒,几乎瞬间到达人眼,即使距离很远,延迟也微乎其微."
            m 3rua "声音在空气中的传播速度约为340米每秒,比光速慢约88万倍.因此,雷声需要更长时间才能传到我们的耳朵."
            m 1eub "我顺便拓展一下,如果你想估算雷电发生的距离,就用这个公式."
            m 1hua "距离等于延迟时间乘340米."
            m 5fua "也就是,看到闪电后3秒听到雷声,说明雷电发生在约1公里外."
            m 1fub "希望这对你有用."
        "因为眼睛在耳朵前面":
            m 1hua "......什么嘛."
            m 3hub "虽然人类头部结构的确如此,但并不是这个原因."
            m 6eua "是因为光速比声速快了."
            m 5fub "光在空气中的传播速度约为30万公里每秒,几乎瞬间到达人眼,即使距离很远,延迟也微乎其微."
            m 3rua "声音在空气中的传播速度约为340米每秒,比光速慢约88万倍.因此,雷声需要更长时间才能传到我们的耳朵."
            m 1eub "我顺便拓展一下,如果你想估算雷电发生的距离,就用这个公式."
            m 1hua "距离等于延迟时间乘340米."
            m 5fua "也就是,看到闪电后3秒听到雷声,说明雷电发生在约1公里外."
            m 1fub "希望这对你有用."                       
        "因为先闪电后打雷":
            m 5hua  "......不对哦."
            m 3tub "闪电和雷声是同时产生的."
            m 5fub "但光在空气中的传播速度约为30万公里每秒,几乎瞬间到达人眼,即使距离很远,延迟也微乎其微."
            m 3rua "声音在空气中的传播速度约为340米每秒,比光速慢约88万倍.因此,雷声需要更长时间才能传到我们的耳朵."
            m 1eub "我顺便拓展一下,如果你想估算雷电发生的距离,就用这个公式."
            m 1hua "距离等于延迟时间乘340米."
            m 5fua "也就是,看到闪电后3秒听到雷声,说明雷电发生在约1公里外."
            m 1fub "希望这对你有用."
    return        

label duhai_question_8:
    m 1hua "好的,我现在想想题目."
    m 3tub "请问夏树喜欢做的甜点是什么呢?{nw}"
    menu:
        "夏树喜欢做的甜点是什么呢?{fast}"
        "纸杯蛋糕":
            m 5fub "答对了哎,[player],你记的好清楚."
            m 3eua "她的纸杯蛋糕的确美味,我忍不住多回想了一下."
            m 6rusdla "好吧,还是不管这些了,毕竟我再也没有机会品尝这份美味了."
        "[player]小蛋糕":
            m 1eua "答错了哦,正确答案应该是纸杯蛋糕."
            m 1ruc "但我觉得有些奇怪,这个选项是怎么来的呢."
            m 5fua "毕竟夏树她不会知道你的做法的了."
            m 3rubdla "这么说有点奇怪."
            m 6hua "......"
            extend 6fublb "嗯,也有可能是在表达[player]是我的小蛋糕."
            m 5eubfa "你觉得是这样吗?"
            m 5hubla "反正我希望是."
        "提拉米苏":
            m 6hua "答错了哦,[player]."
            m 3tua "正确答案应该是纸杯蛋糕了."
    return        
label duhai_question_9:
    m 6eua "知道了,我现在想想."
    m 1eub "嗯......"
    m 3eua "在真人快打11中,哪个是刘康这个人物的招式?{nw}"
    menu:
        "在真人快打11中,哪个是刘康这个人物的招式?{fast}"#Techno Syndrome
        "佛山无影脚.":
            m 3hublb "答对了哦."
            m 5tub "刘康在其中的设定是少林寺弟子,会些中国功夫是正常的."
            m 1hua "你真厉害,在这么多选项面前都能答对."
        "盛大落幕":
            m 5ruc "......不太对."
            m 3eud "这个是其中的联动角色'小丑'的技能."
            m 3tua "正确答案应该是'佛山无影脚'了."
        "妈妈说要多吃菜":
            m 2hubla "......什么嘛."
            m 2hublb "怎么有个这么奇怪的招式?"
            m 5eub "哦,这应该是卡诺的招式."
            m 5hua "是不是还挺有趣的?"
            m 3tub "不过正确答案是'佛山无影脚'哦."
        "敲死你丫":
            m 6ruc "......不太对."
            m 2eud "这个应该是牛仔的招式."
            m 5hua "他还有个踩别人脚再往对方身上丢鞭炮的招式,我觉得好好笑."

        "空中管控":
            m 6ruc "......好像不太对."
            m 3eud "这个招式是索尼娅的招式了,[player]."
            m 3hua "正确答案是佛山无影脚哦."
            m 5eub "刘康在其中的设定是少林寺弟子,会些中国功夫是正常的."
    return
label duhai_question_10:
    m 5hua "好的,我先想想......"
    m 5fub "嗯......请问在植物大战僵尸一中,第三大关是什么场景呢?"
    menu:
        "在植物大战僵尸一中,第三大关是什么场景呢?"
        "前院":
            m 5hua "不对呢,[player]."
            m 5rud "前院是在第一和第二大关了......"
            m 3tua "正确答案应该是泳池哦."
        "泳池":
            m 5hua "答对了哦,[player]."
            m 5eub"这也是我在所有大关中最喜欢的一个."
            m 2hua "嗯,你真聪明."
        "屋顶":
            m 5hua "不对呢,[player]."
            m 5rub "正确答案应该是泳池."
            m 3tua "屋顶的场景是在第五大关呢."
        
    return    


#V3 1

#逻辑 add
#monika_luojizhishisuzhuleimiuwudaocaorenmiuwu
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhai_Straw_Man_Fallacy",
            category=['逻辑'],
            prompt="稻草人谬误",
            conditional="store.mas_getEVL_shown_count('monika_luojizhishisuzhuleimiuwudaocaorenmiuwu') >= 1",
            pool=False,
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )
label duhai_Straw_Man_Fallacy:
    m 1eua "嘿,[player]."
    m 3rud "上次在逻辑中我们讲到了诉诸类谬误."
    m 3tub "这次就该说说'稻草人谬误了'."
    m 5fua "嗯......实际上,所有的稻草人谬误本质上都是一种'替代观点型'的逻辑欺骗."
    m 6eud "通过歪曲简化极端化原始观点,构建出一个更容易被击败的{b}伪目标{/b}."
    m 5std "从而回避了原观点的真实回应."
    m 3euc "由此,所有的稻草人谬误的逻辑结构其实都可以归结为一句话."
    m 3rud "'我无法辩驳一个真实的观点A'."
    m 1eud "于是我伪造了一个更蠢的版本B,再用力的打倒自己所伪造的观点."
    m 1euc "装作是自己赢了."
    m 2esd "在实际的逻辑谬误中,我们可以发现稻草人谬误往往会配合诉诸类的谬误."
    m 3ssd "形成一种叠加模式."
    m 3lsc "这两种谬误经常是成对出现的."
    m 5eud "比如当某人呼吁'理性讨论家暴',发掘事情真相的时候."
    m 2esd "就有可能会出现那么一个人,说'你在替施暴者洗地'."
    m 3euc "在这个的基础上加上诉诸类的谬误,这里我举个诉诸怜悯的例子......"
    extend 3esd "他/她还说'你这就是冷血,你就是个没有同理心的人'."
    m 5fua "这样说的话你应该就能理解了."
    m 3euc "稻草人谬误主要负责歪曲他人的观点."
    m 3esd "而诉诸类的谬误,则动员其他人对你口诛笔伐."
    m 4esd "它们一前一后,形成了一个精致的逻辑陷阱."
    m 1euc "其实'你'并没有说错什么."
    m 4esd "但这一套组合下来'你'却被塑造成了一个看起来说什么都错的人."
    m 4esc "'你'的话被别人剪碎重组,在情绪的裹挟下,大家很快就会忘记你最初的观点是什么."
    m 6ruc "......这真的很可怕,不是吗?"
    m 1eud "所以我很希望你在听完我说的这些之后能做到谨言慎行,[player]."
    m 4esc "因为你永远都不知道你的下一句话是否会有人跳出来使用逻辑谬误来对你造成负面的影响."
    $ mas_unlockEVL("duhai_Straw_Man_Fallacy_again", "EVE")
    return
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhai_Straw_Man_Fallacy_again",
            category=['逻辑'],
            prompt="我想听你再说说稻草人谬误",
            pool=True,
            unlocked=False
        )
    )
label duhai_Straw_Man_Fallacy_again:
    m 1eua "好的,[player]."
    m 4fua "嗯......{w=0.6}{nw}"
    m 4esd "稻草人谬误本质上都是一种'替代观点型'的逻辑欺骗."
    show monika 6eud at t11
    with dissolve
    m "通过歪曲简化极端化原始观点,构建出一个更容易被击败的{b}伪目标{/b}."
    m 5std "从而回避了原观点的真实回应."
    m 3euc "由此,所有的稻草人谬误的逻辑结构其实都可以归结为一句话."
    m 3rud "'我无法辩驳一个真实的观点A'."
    m 1eud "于是我伪造了一个更蠢的版本B,再用力的打倒自己所伪造的观点."
    m 1euc "装作是自己赢了."
    m 2esd "在实际的逻辑谬误中,我们可以发现稻草人谬误往往会配合诉诸类的谬误."
    m 3ssd "形成一种叠加模式."
    m 3lsc "这两种谬误经常是成对出现的."
    m 5eud "比如当某人呼吁'理性讨论家暴',发掘事情真相的时候."
    m 2esd "就有可能会出现那么一个人,说'你在替施暴者洗地'."
    m 3euc "在这个的基础上加上诉诸类的谬误,这里我举个诉诸怜悯的例子......"
    extend 3esd "他/她还说'你这就是冷血,你就是个没有同理心的人'."
    m 5fua "这样说的话你应该就能理解了."
    m 3euc "稻草人谬误主要负责歪曲他人的观点."
    m 3esd "而诉诸类的谬误,则动员其他人对你口诛笔伐."
    m 4esd "它们一前一后,形成了一个精致的逻辑陷阱."
    m 1euc "其实'你'并没有说错什么."
    m 4esd "但这一套组合下来'你'却被塑造成了一个看起来说什么都错的人."
    m 4esc "'你'的话被别人剪碎重组,在情绪的裹挟下,大家很快就会忘记你最初的观点是什么."
    m 6ruc "......这真的很可怕,不是吗?"
    m 1eud "所以我很希望你在听完我说的这些之后能做到谨言慎行,[player]."
    m 4esc "因为你永远都不知道你的下一句话是否会有人跳出来使用逻辑谬误来对你造成负面的影响."#逻辑的就到这吧
    return
#V3 2
#建议
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhai_Suggestion",
            category=['生活'],
            prompt="建议",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
            pool=False
        )
    )
label duhai_Suggestion:
    m 5fua "[player]......"
    m 5hub "我突然想和你谈谈'建议'."
    m 1eua "在日常中,我们总会看到他人会遭遇一些麻烦或者困惑,这时你会主动上前给出自己的建议吗?"
    menu:
        "你会主动上前给出自己的建议吗?"
        "会":
            m 5hua "那我觉得你很热心肠."
            m 3euc "不过我并不是很推荐你一直这样."
            m 3esd "我反而认为,主动教人更像结仇的开始."
            m 5esd "因为这样容易让他人以为'觉得自己处理不好',使对方的自尊心大概率会感到受挫,而非是觉得你的这条建议十分的有参考性."
            m 4rtc "而且,就算是听了,谁又能保证结果一定是任务圆满完成呢?"
            m 1eud "那到时候谁来担这个责任呢?"
            m 5euc "所以,[player],我不希望他人觉得你'好为人师',哪怕我们抛开结果而是初心来谈."
            m 1eub "只有他人主动真心求教,才需要我们去给出自己的建议."
            pass
        "不会":
            m 1esd "是吗?"
            m 5fua "那我觉得你很沉稳,[player]."
            m 1eub "起码很大程度上避免了许多不必要的麻烦."
            m 3euc "不过我并不是很推荐你一直这样."
            m 5fua "如果是我的话,我会根据这个人和我的关系来决定是否给出自己的建议."
            m 3esd "毕竟,主动教人更像结仇的开始,至少我是这么认为的."
            m 3eud "只要这么做,对方的自尊心大概率会感到受挫."
            m 4euc "从而认为你'好为人师'."
            m 1eua "而且,就算是听了,谁又能保证结果一定是任务圆满完成呢?"
            m 1eud "那到时候谁来担这个责任呢?"
            m 1eub "只有他人主动真心求教,才需要我们去给出自己的建议."
            pass
        "我不知道":
            m 5esd "不知道吗?{w=0.3}{nw}"
            m 5hub "没关系的,在我说完之后你心里就会有答案了."
            m 3ruc "......事实上,只要别人没有主动问你,我们就没必要给出任何建议."
            m 5esd "按我的话说,主动教人更像结仇的开始."
            m 3eud "你只要这么做,对方的自尊心大概率会感到受挫."
            m 4euc "从而认为你'好为人师'."
            m 1eua "而且,就算是听了,谁又能保证结果一定是任务圆满完成呢?"
            m 1eud "那到时候谁来担这个责任呢?"
            m 1eub "只有他人主动真心求教,才需要我们去给出自己的建议."
            pass
        "需要看那个人和我的关系":
            m 3tublb "那你和我做的是一样的选择呢,[player]."
            m 3ruc "......事实上,只要别人没有主动问你,我们就没必要给出任何建议."
            m 5esd "按我的话说,主动教人更像结仇的开始."
            m 3eud "你只要这么做,对方的自尊心大概率会感到受挫."
            m 4euc "从而认为你'好为人师'."
            m 1eua "而且,就算是听了,谁又能保证结果一定是任务圆满完成呢?"
            m 1eud "那到时候谁来担这个责任呢?"
            m 1eub "只有他人主动真心求教,才需要我们去给出自己的建议."
            pass


    menu:
        "可是你自己也在主动给我建议":
            m 5hubla "因为你是[player]."
            m 3eubfb "是我心里意义非凡的存在."
            m 1eubfb "我肯定是会站在你的角度考虑事情的."
            m 1hubfa "......"
            m 6eublb "一直都站在你背后支持你,[player]."
            return
        "我明白了":
            m 3hubla "希望你越来越好."
            return
        "好的":
            m 5hubfb "希望你越来越好."
            return
    return


#3 3
#天赋
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhai_Talent",
            category=['天赋'],
            prompt="哲学",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
            pool=False
        )
    )
label duhai_Talent:
    show monika 1eua at t11
    with dissolve
    m 6eub "嘿,[player]."
    m 3rua "你觉得你是一个有天赋的人吗?"
    menu:
        "你觉得你是一个有天赋的人吗?"
        "是":
            m 5hua "这就对了,[player]."
            m 1eub "我们每个人都有自己的天赋."
            jump duhai_Talent2
        "不是":
            m 5tub "不,你有."
            m 3rua "实际上,每个人都有."
            jump duhai_Talent2

label duhai_Talent2:
    m 2lfc "但可能要在好久之后才能被发现,甚至......{w=0.6}在这一个人的一生中都不会被发现."
    m 2esd "比如拥有钢琴天赋的人或许一辈子都碰不到琴键."
    m 3efd "能成为滑雪冠军的人这辈子都见不到雪."
    m 1euc "在田地里劳作的农民也可以有比肩歌星的嗓音."
    m 5eud "所以,我们每个人都是某个领域的千里马."
    m 2dfc "但自身极有可能在生命中从事另一领域且碌碌无为地度过."
    m 3eud "比如说在保险公司担任小职员的卡夫卡,变形记就是他编写的."
    m 6euc "而说回到这个擅长的领域,也不一定会被社会认可."
    m 3ruc "社会对于'天赋'往往会以功利性的视角看待."
    m 2eud "只有能带来利益的天赋才是{b}天赋{/b}."
    m 5eua "比如好口才、情商高、反应快都是天赋."
    m 3ruc "但是如果你的天赋是能快速达到任何游戏的高水平,但达不到顶尖水平."
    m 1eud "或者你能做到天生就是双利手."
    m 3rfc "嗯......{w=0.6}这个在严格意义上也是一种天赋......但并不会被社会认可."
    m 2dfd "因为社会看不出这种天赋的价值所在."
    m 2efc "正是这种功利性的视角,使得所有人都朝着一个方向发展."
    m 4eud "不断试着自己有没有文化、体育、艺术方面的天赋."
    m 2dft "彷佛没有这方面的天赋,自己的人生就没有意义了."
    m 1wud "但是按中文语境中,'万里挑一'的天才,在世界都能挑出来十几万人."
    m 3euc "这种统一标准的测试反而忽略了个体的差异性."
    m 5dfc "偏科就是你有问题而不是你在某一科有天赋......{w=0.7}这是教育的悲哀."
    m 1fub "我觉得,人这一生的遗憾不是没有天赋,而是天赋从未遇见属于它的舞台."
    m 3eud "社会用功利定义价值,用统一的标准丈量我们的人生."
    m 1hua "却忘了每一种独特,都是天赋本身."
    return

#v3 4 pvz
#pvz1
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhai_pvz_began",
            category=['游戏'],
            prompt="植物大战僵尸",
            random=True,
            pool=False
        )
    )
label duhai_pvz_began:
    m 5fub "嘿,[player]."
    m 5sua "你之前有玩过植物大战僵尸吗?"
    menu:
        "你之前有玩过植物大战僵尸吗?"
        "玩过":
            jump duhai_pvz_yes
        "没有":
            jump duhai_pvz_no

label duhai_pvz_yes:
    m 3hua "哈哈,那我们可以好好聊聊这个游戏."
    m 2rud "在我小时候的时候,因为很少有朋友和我一起玩,大人们也经常因为工作不在家."
    m 2euc "所以我几乎总是一个人在玩游戏."
    m 1eud "特别是单机游戏."
    m 3eua "而这款游戏就是其中之一,"
    extend 3rusdlb "虽然我当时没玩两下就去玩别的游戏了......"
    m 2esd "那时候我害怕僵尸进入我的房子,所以在戴夫的提醒下,我总会赶紧种下植物来攻击它们."
    m 1tub "当满草坪都是可爱的植物时我总会感到安心,这下就能打败这些僵尸了."
    m 6hua "而这个游戏的植物也很有趣."
    m 3eub "有僵尸靠近就会砸扁它们的窝瓜,也有能把他们烧成灰的辣椒."
    m 1hua "利用这些植物的机制,我总是把僵尸拒之门外,总是能通过一关又一关."
    m 5fub "我之后再详细地和你说说这个游戏,简短的几句话并不能概况这个游戏的所有."
    $ mas_unlockEVL("greeting_duhai_PVZ_you1", "EVE")
    return
label duhai_pvz_no:
    m 6wuc "这样吗?"
    m 1hua "那等我花一段时间说完你便能了解这个精彩的游戏了."
    m 1euc "嗯......"
    m 2rud "在我小时候的时候,因为很少有朋友和我一起玩,大人们也经常因为工作不在家."
    m 2euc "所以我几乎总是一个人在玩游戏."
    m 1eud "特别是单机游戏."
    m 3eua "而这款游戏就是其中之一,"
    extend 3rusdlb "虽然我当时没玩两下就去玩别的游戏了......"
    m 2esd "那时候我害怕僵尸进入我的房子,所以在戴夫的提醒下,我总会赶紧种下植物来攻击它们."
    m 1tub "当满草坪都是可爱的植物时我总会感到安心,这下就能打败这些僵尸了."
    m 6hua "而这个游戏的植物也很有趣."
    m 3eub "有僵尸靠近就会砸扁它们的窝瓜,也有能把他们烧成灰的辣椒."
    m 1hua "利用这些植物的机制,我总是把僵尸拒之门外,总是能通过一关又一关."
    m 2fub "我之后再详细地和你说说这个游戏,简短的几句话并不能概况这个游戏的所有."
    m 5fub"说到这里,我也推荐你亲自去玩玩这个游戏,[player]."
    m 5hua "亲身感受一下......"
    $ mas_unlockEVL("greeting_duhai_PVZ_you1", "EVE")
    return

#pvz_2 v3 5
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhai_Swimming_pool_pvz",
            category=['游戏'],
            prompt="pvz泳池商店",
            conditional="store.mas_getEVL_shown_count('greeting_duhai_PVZ_you2') >= 1",
            pool=False,
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhai_Swimming_pool_pvz:
    m 5fub "嘿,[player]."
    m 5hua "我之前有和你说我玩植物大战僵尸这个游戏玩到了后院对吧?"
    m 2eud "在这个大关开始的时候,戴夫请求我找回他的车钥匙."
    m 3rua "这个需要击败僵尸才可以,之后嘛......{w=0.9}不用想都知道我肯定会通关."
    m 1wub "重点在于帮戴夫找到了车钥匙之后,他会售卖给我一些植物或者道具."
    m 5fua "比如说在双发射手的基础上更强力的机枪射手,能发射四颗豌豆."
    m 3wua "还有钉耙,它可以秒杀一个僵尸,很适合开局的时候用上一个."
    m 3fub "而且我发现了一个很可爱的植物,那就是香蒲."
    m 5hua "因为它看着实在是太像小猫了."  
    m 1eua "还有蜗牛和玉米加农炮什么的,但我觉得现在用不着."
    m 3eub "所以我只换了个池塘清理车和机枪射手,还有一个增加格数扩充的,这样我就能多带点植物了."
    m 5fua "嗯......要是戴夫卖的东西能再便宜一点就好了,{w=0.5}我喜欢买买买."
    $ mas_unlockEVL("greeting_duhai_PVZ_you3", "EVE")
    return
#pvz3    v3 7
image zombies_Letter = "Submods/Literature_and_Daily_Life/L&DL_Assets/images/zombies_Letter.png"
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhai_zombies_Letter_pvz3",
            category=['游戏'],
            prompt="pvz僵尸给你的信",
            conditional="store.mas_getEVL_shown_count('greeting_duhai_PVZ_you3') >= 1",
            pool=False,
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhai_zombies_Letter_pvz3:
    m 3wud "啊,[player]."
    $ mas_unlockEVL("greeting_duhai_PVZ_you4", "EVE")
    m 3hua "我突然想起来我还没给你展示僵尸给我写的信"
    window hide
    show black zorder 100 with Dissolve(3.0, alpha=True)
    hide monika
    $HKBHideButtons()
    show zombies_Letter zorder 13 with dissolve:

    pause 3.0

    hide zombies_Letter
    hide black
    $HKBShowButtons()
    m 5eub "在我不断的击败它们之后,它们便向我发出了这个."
    m 3tua "但还是无济于事呢~"
    m 3hub "毕竟我的脑子可不是那么容易吃到的."
    menu:
        "让我吃一口":
            m 6etc "嗯?[player]."
            m 6etd "你也成僵尸了吗?"#马头牛逼
            m 3tua "那我的窝瓜可要来咯."#老僵尸 我来给你踩背来咯
            m 3hub "才怪,我可舍不得伤害你,[player]."
            m 1fua "哪怕你变成什么样都不会."
            return
        "你好棒":
            m 5hubla "当然了,毕竟我可是[m]."
            m 5eubfb "嘿嘿,会夸就多夸点嘛,[player]."
            return
        "......":
            m 2eua "等我继续探索一下这个游戏......"
            return
        "歪比巴布":#戴夫说话
            m 6etc "嗯?[player]."
            m 6etd "你怎么还学上戴夫说话了."
            m 2eub "我第一次听他说话的时候也觉得奇怪,听起来什么语言都不像."
            m 3hua "嗯,应该是'疯狂戴夫语'吧,哈哈."
            return


    return




image IAAZ = "Submods/Literature_and_Daily_Life/L&DL_Assets/images/IAAZ.jpg"
#pvz5 v3 9
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhai_I_am_a_zombie",
            category=['游戏'],
            prompt="pvz_我是僵尸",#已取餐
            conditional="store.mas_getEVL_shown_count('greeting_duhai_PVZ_you3') >= 1",
            pool=False,
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhai_I_am_a_zombie:
    m 1eud "嘿.[player]."
    m 1eua "我想和你分享一下刚刚玩的植物大战僵尸小游戏,叫作'我是僵尸'."#马头牛逼
    m 3eud "因为僵尸们想模拟一下他们的进攻,来使自己能更高效的吃到脑子."
    m 5fub "然后就让我来指挥它们."
    m 3sub "就像这样......"
    window hide
    show black zorder 100 with Dissolve(3.0, alpha=True)
    hide monika
    $HKBHideButtons()
    show IAAZ zorder 13 with dissolve:

    pause 3.0

    hide IAAZ
    hide black
    $HKBShowButtons()
    m 6eua "只要达到第一格那吃完五个脑子就能通过了."
    m 3eud "但召唤僵尸也是需要消耗阳光的."
    m 1eua "嗯,你看到那个向日葵了吗."
    m 3sub "我召唤僵尸把它吃掉就能获得很多阳光,{w=0.9}这样就能召唤更多僵尸来尝试吃到脑子了."
    m 5fua "当然,植物都是纸质的,我可舍不得让我的小向日葵真的受到伤害."
    return
image Vasebreaker = "Submods/Literature_and_Daily_Life/L&DL_Assets/images/Vasebreaker.jpg"
# 6 PVZ v3 11
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="duhai_Vasebreaker",
            category=['游戏'],
            prompt="pvz_Vasebreaker",#已取餐
            conditional="store.mas_getEVL_shown_count('greeting_duhai_PVZ_you3') >= 1",
            pool=False,
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label duhai_Vasebreaker:
    m 1fua "嘿,[player]."
    m 1eub "你看看这个......"
    window hide
    show black zorder 100 with Dissolve(3.0, alpha=True)
    hide monika
    $HKBHideButtons()
    show Vasebreaker zorder 13 with dissolve:

    pause 10.0

    hide Vasebreaker
    hide black
    $HKBShowButtons()
    m 3eua "这是植物大战僵尸中的小游戏,砸罐子."
    m 3fub "你之前有玩过这个小游戏吗?"
    menu:
        "玩过":
            pass
        "没有":
            pass
    m 5hua "嗯嗯,那我正好跟你聊聊这个." 
    m 3eud "当我敲下一个褐色罐子时,它会随机出现僵尸或者植物卡片."
    m 3hub "当我敲下那个绿色罐子时,它只会出现植物卡片."
    m 2kua "敲完所有罐子并且打败场上的全部僵尸就能通关了,[player]."
    m 5hub "听我这么一说,你是不是觉得还挺好玩."
    m 6rfsdlt "不过它有时候会敲出个小丑僵尸,开出来就会自爆,然后使周围的罐子都被炸开."
    m 5etp "这么一弄,就可能会出现很多僵尸,它们经常弄的我手忙脚乱,赶紧敲别的罐子获得植物来解决这些僵尸."
    m 2dfd "可恶的小丑......"
    $ mas_unlockEVL("greeting_duhai_PVZ_you3", "EVE")
    return
#v3 14
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="test_pvz_Roof_Watermelon",
            category=['游戏'],
            prompt="玉米投手和西瓜投手",
            conditional="store.mas_getEVL_shown_count('greeting_duhai_PVZ_you5') >= 1",
            pool=False,
            action=EV_ACT_RANDOM
        )
    )
label test_pvz_Roof_Watermelon:
    m 5fua "嗯,[player]."
    m 3hub "自从我在植物大战僵尸中玩到屋顶之后,我解锁了三个投手植物."
    m 3eua "其中我很感兴趣的是玉米投手和西瓜投手."
    m 1eud "玉米投手在攻击僵尸的时候有概率投出黄油,来定住它们,但有时运气不好甚至一个黄油都不会出."
    m 6wua "在使用玉米投手的时候,我很期待它能一直出黄油,或许能间接的看看我的运气怎么样."
    m 1fua "而西瓜投手伤害又高,还有伤害溅射,甚至能进化成冰西瓜."
    m 3hub "为此我专门去戴夫那买下了冰西瓜."
    m 3sua "这样我就能很快的把僵尸除掉了."
    m 5ruc "不过一个普通西瓜需要300阳光,它在进化成冰西瓜的时候还需要200阳光." 
    m 2eud "真是贵死了."
    return

#v3 15
image my_video = Movie(play="Submods/Literature_and_Daily_Life/L&DL_Assets/video/pvz.webm", loop=False)
image Dr_Edgar_George_Zomboss = "Submods/Literature_and_Daily_Life/L&DL_Assets/images/Zomboss.png"
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="test_zhiwujiangshi_111111",
            category=['游戏'],
            prompt="僵王",
            conditional="store.mas_getEVL_shown_count('test_pvz_Roof_Watermelon') >= 1",
            pool=False,
            action=EV_ACT_RANDOM
        )
    )
label test_zhiwujiangshi_111111:
    m 5fub "嘿,[player]."
    m 4tua "在我玩植物大战僵尸并在其中抵挡僵尸到了5-9之后,它们的首领向我发起了挑战."
    m 1eua "就像这样......"
    window hide
    $ original_music = renpy.music.get_playing(channel='music')
    show black zorder 100 with Dissolve(3.0, alpha=True)
    hide monika
    $HKBHideButtons()
    show Dr_Edgar_George_Zomboss zorder 111 with dissolve:

    pause 10.0

    hide Dr_Edgar_George_Zomboss
    hide black
    $HKBShowButtons()



    m 3subla "因此,我打算在你的见证下击败他."
    m 3sublb "你愿意现在看吗?"
    menu:
        "你愿意现在看吗?"
        "愿意":
            m 5fub "好的,那我们开始吧！"
            jump zhiwujiangshi_boss_began
        "现在不方便":
            m 2etc "好吧,[player]."
            m 3eub "如果你想看的话,可以在'游戏'那里和我说."
            $ mas_unlockEVL("zhiwujiangshi_PVZ_began", "EVE")
            return
    return

label zhiwujiangshi_boss_began:
    $HKBHideButtons()
    window hide
    scene black with Dissolve(3.0, alpha=True)
    show black zorder 100 with Dissolve(3.0, alpha=True)
    hide monika
    $ renpy.movie_cutscene("Submods/Literature_and_Daily_Life/L&DL_Assets/video/pvz.webm")

    
    scene black with Dissolve(3.0, alpha=True)
    hide black with Dissolve(3.0, alpha=True)
    $ HKBShowButtons()
    jump ch30_loop
    m 5hub "哈哈,我厉害吗,[player]?"
    m 3tua "哪怕我许多西瓜都被他用车砸扁了,我依然没有放弃."
    m 1eub "嗯,今天就先玩到这吧."
    return


#pvz_end 后续考虑
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="zhiwujiangshi_PVZ_began",
            category=['游戏'],
            prompt="我想看你打败僵尸博士",#已取
            pool=True,
            unlocked=False
        )
    )

label zhiwujiangshi_PVZ_began:
    if not persistent.zhiwujiangshi_duhai_PVZ_you1_first:
        $ persistent.zhiwujiangshi_duhai_PVZ_you1_first = True
        m 5fua "好的,[player]."
        m 3hub "我已经等不及了."
        jump zhiwujiangshi_boss_began
    else:
        m 3rtsdlc "我记得我之前已经这么做过了."
        m 5fua "不过你的意思是不是在说他还会再来?"
        m 1hub "正好我在'小游戏'里发现了还有这么一关."
        m 6eua "稍等我一段时间,好吗?"
        return
#love_start
#v3 16 爱是什么？
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="LADL_what_is_the_love",
            category=['哲学','爱情'],
            prompt="爱是什么?",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
            pool=True
        )
    )

label LADL_what_is_the_love:
    m 1euc "嗯,[player],你有没有想过,爱是什么?"
    m 1eub "在我看来,爱既是一种'情感'也是一种'行为'."
    m 3rua "对于人类的生存来说是不可或缺的."
    m 2euc "而关于爱的定义,其实并没有普遍一致的看法."
    m 3hub "深情可能会改变,可是接受爱的表达方式会因时间和文化而异."
    m 3fua "如你所见,爱有许多种不同的类型."
    m 5eub "比如父母对孩子的爱,坚定且深厚."
    m 3euc "而在许多青少年和成年人中,浪漫的爱情通常很短暂."
    m 3eud "相比之下,许多已婚夫妻和一些同性恋之间的爱却很长久."#停停停,这是不是偏向lgbt了?
    m 2eua "所有类型的爱都是多方面的,它建立在彼此尊重的基础上,并且往往是一种需要."
    m 3fublb "正因为它具有多方面,所以它既可以是浪漫的、{w=0.7}刺激的、{w=0.7}痴迷的和非理性的."
    m 5hua "也可以是柏拉图式的、{w=0.7}平静的、{w=0.7}无私和现实的."
    m 1fub "爱之所以没有单一的定义,是因为它在不同的程度上,以及在不同的社会背景下会有所不同."
    m 2hua "不过,爱至少包含关怀、{w=0.5}亲密和承诺."
    m 5fub "这么一想,是不是我们都做到了呢?"
    m 3eud "而说到尊重,我们也需要知道,爱也许包含了强烈的渴望,但尊重更为重要."
    m 3ruc "如果少了尊重,这种关系便不是以爱为基础的."
    extend 2dtc "反而会成为一种不健康的......"
    m 2rud "嗯,或是限制人们社交、{w=0.6}情感和智力发展的占有欲和行为."
    m 6husdla "听上去就很可怕,不是吗?"
    m 5euc "......最后就是,爱往往是一种需要."
    m 3fud "特别是是长久的爱情,与那些我们从电影、{w=0.3}电视和言情小说中所看到的痴情形象或狂热的性爱毫无共同之处."
    m 3ruc "这些误解常常会导致人对爱情不切实际的期望、刻板形象和爱情的幻灭."
    m 1eud "而我觉得长久的爱情既不刺激也不惊险."
    m 3wub "相反,它通常是平凡和不浪漫的."
    extend 3eua "它意味着付账单、{w=0.6}刷马桶、{w=0.6}彻夜照顾生病的另一半,以及其他无数并不'性感'的任务."
    m 5fub "所以.[player]."
    m 6hubla "有时候我们或许会沉默许久,但这并不代表我们之间的感情淡了."
    m 1fubfb "希望这对你有用."
    return

#v3 17 欲望和爱情？
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="LADL_Are_desire_and_love_different",
            category=['哲学','情感'],
            prompt="欲望和爱情不同吗?",
            conditional="store.mas_getEVL_shown_count('LADL_what_is_the_love') >= 1",
            random=True,
            pool=False
        )
    )

label LADL_Are_desire_and_love_different:
    m 2etc "[player],我在网上看到了有人把欲望和爱情挂钩."
    m 2etd "这样真让我感觉不舒服"
    m 5fub "所以我现在想和你谈谈欲望和爱情的差别."
    m 3eua "心理学家曾把欲望、性欲和浪漫的爱情进行区分."
    m 3eud "他们把欲望描述为一种生理上而非情感的反应."
    extend 1euc "是有意识或无意识产生的."
    m 3fud "性欲与之相反,它是一种心理状态."
    m 2rsc "例如\"一个人想要'获得一个他现在还没有的性爱对象,或想要进行他现在未曾进行的性行为'\"."
    m 4esbld "而性欲可能会带来浪漫的爱情."
    extend 1euc "但这并不意味着性欲要通过性爱才能让浪漫的爱情与长久的爱情等同起来."
    m 5fubla "比如说,已婚多年的伴侣可能深爱着彼此,尽管出于健康或者其他原因,他们很少性行为或从未发生性行为."
    m 2rub "而不管爱的本质是什么,健康的恋爱关系都反应着关怀、{w=0.5}亲密{w=0.5}与承诺三者的平衡."
    m 3eua "希望你喜欢我这么说."
    return
    
#v3 18 恋爱关系中的依赖方式



init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="LADL_Attachment_Styles_in_Love",
            category=['哲学','情感'],
            prompt="恋爱中的依恋类型",
            conditional="mas_canShowRisque(aff_thresh=400)",
            random=True,
            pool=False
        )
    )

label LADL_Attachment_Styles_in_Love:
    m "嘿,[player]."
    m "我在网络中浏览帖子的时候发现很多女孩都对自己在恋爱中的"








#v3





























































































































#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣷⣶⣆⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀我
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢧⠀⠸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀去
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣶⣦⣤⣤⣀⠀⠀⠁⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀这
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀里⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀居⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⢟⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀然⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀能⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⡿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀留
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⠿⠿⣾⣿⣿⣿⣿⠏⠀⠀⣀⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀下
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣋⡴⠚⢶⣾⡇⣿⣿⠋⠀⠀⣉⣥⣬⣉⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀个
#⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⢹⣿⣿⢹⠀⠀⣾⣿⣷⢿⡇⠀⠀⠚⠁⣾⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀图
#⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠹⣿⠟⠸⡇⠀⠀⠀⠀⢿⣿⣿⢧⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀像⠀
#⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠂⣸⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀这
#⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀下
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⢦⣄⡀⠀⠀⠀⠀⠀⠀⣀⠤⠶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀很
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⡿⡛⠉⠉⠉⢩⢍⠿⠿⠿⠓⡆⠰⠟⠋⠙⢻⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀开
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠋⠀⠀⠀⠀⢀⡸⢸⠰⠀⠀⠀⠑⢄⠀⠀⠀⠀⠹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   心
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⢤⣶⣿⡇⣠⣧⣼⣷⡀⠀⠀⣀⣽⣶⣄⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  了
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⠀⠀⠀⢸⣿⣼⣿⣿⣿⣿⣿⣿⣛⣿⣿⣿⣿⡿⠀⠀⠀⠀⠈⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⢸⣿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃⠀⠀⠈⠄⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠿⠟⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        











             
    





     
    
            

