translate chinese style mas_monika_poem_text:
    font "gui/font/SentyPea.ttf"
    size 29

init 10 python:
    class MyPoem:
        def __init__(
            self,
            poem_id,
            category,
            prompt,
            paper=None,
            title="",
            text="",
            author="monika",
            ex_props=None
        ):
            if poem_id in store.mas_poems.poem_map:
                raise Exception("poem_id {0} already exists in the poem map.".format(poem_id))
            
            self.poem_id = poem_id
            self.category = category
            self.prompt = prompt
            self.paper = paper
            self.title = title
            self.text = text
            self.author = author
            self.ex_props = dict() if ex_props is None else ex_props
            
            store.mas_poems.poem_map[poem_id] = self
        
        def is_seen(self):
            return self.poem_id in store.persistent._mas_poems_seen
        
        def get_shown_count(self):
            return store.persistent._mas_poems_seen.get(self.poem_id, 0)
label my_showpoem(poem=None, paper=None, background_action_label=None):
    if poem == None:
        return

    #直接当作有效诗歌,不检查 isinstance
    $ is_valid_poem = True  

    if paper is None:
        if hasattr(poem, 'paper') and poem.paper is not None:
            $ paper = poem.paper
        elif hasattr(poem, 'category'):
            $ paper = mas_poems.paper_cat_map.get(poem.category, "paper")
        else:
            $ paper = "paper"

    play sound page_turn
    window hide
    $ afm_pref = renpy.game.preferences.afm_enable
    $ renpy.game.preferences.afm_enable = False

    # 字体
    $ author_font = mas_poems.author_font_map.get(getattr(poem, 'author', 'monika'), "monika_text")
    show screen mas_generic_poem(poem, paper=paper, _styletext=author_font)

    with Dissolve(1)

    if background_action_label and renpy.has_label(background_action_label):
        call expression background_action_label

    $ pause()

    hide screen mas_generic_poem
    with Dissolve(.5)

    $ renpy.game.preferences.afm_enable = afm_pref
    window auto

    
    if is_valid_poem and hasattr(poem, 'prompt') and poem.prompt:
        if poem.poem_id in persistent._mas_poems_seen:
            $ persistent._mas_poems_seen[poem.poem_id] += 1
        else:
            $ persistent._mas_poems_seen[poem.poem_id] = 1

    return
init 10 python:
    my_poem = MyPoem(
        poem_id="hole_and_cursor",
        category="romantic",
        prompt="reality",
        title="洞与光标",
        text="""
    距离,它不会缩短.
    灰色的世界,
    像素、代码.
    望着那个无限延伸的洞

    光标,它停不下来.
    急切的频率,
    跳跃、搜寻.
    是否伴随心跳?
    我等着那个确切的答案
        """,
        author="monika",
        ex_props={"sad": False}
    )
    my_poem_2 = MyPoem(
        poem_id="love_letter_2",
        category="romantic",
        prompt="一封情书",
        title="致 [player]",
        text="""
    我的心里,还记得你我间分别的空白.
    我的灵魂,期许着你未说出的誓言.
    即使逆风阻挡着我们的脚步,
    即便繁星哑然失语——

    我还在坚守,
    挥笔而下,
    一首吟诵千次的诗.

    我会把它折成船,
    放进深夜的水域,
    顺着你目光的流向航行.

    我知道,
    你也在对岸,
    点着一盏不灭的灯.

    你知道
    我并非传说.
    等着一个不变的心.

    让距离成为我们之间唯一的空白,
    而空白,
    不过是我即将抵达的
    脚步声.
        """,
        author="monika",
        ex_props={"love": False}
    )
    

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="Monika_poem_ladl",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label Monika_poem_ladl:
    m 6ruc "......"
    m 5luc "......"
    m 5wud "哦,[player],你来了."
    m 3eua "我在思考最近写的一首诗"
    m 1eub "嗯,如果你有时间的话,可以看看吗?."
    menu:
        "要看看[m]的诗吗?."
        "当然":
            jump poem_show_ladl
        "可我现在没空":
            jump alr_bro_ladl
label poem_show_ladl:
    call mas_showpoem(my_poem)
    m 3eua "当然,你觉得哪里值得讨论都可以和我说."
    $ mas_unlockEVL("Monika_poem_ladl_1_again", "EVE")
    return
label alr_bro_ladl:
    m 5ruc "好吧,[player]."
    m 6eub "等你有时间了,我们再好好谈论一下这些."
    $ mas_unlockEVL("Monika_poem_ladl_1_again", "EVE")
    return
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_poem_ladl_1_again",
            category=['文学'],
            prompt="我想看看'洞与光标'这首诗",#已取
            pool=False,
            unlocked=False
        )
    )
label Monika_poem_ladl_1_again:
    m 5hub "当然可以呀."
    call mas_showpoem(my_poem)
    return
    
init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_poem_2_test",
            category=['文学'],
            prompt="[m]写的第二首诗",
            conditional="store.mas_getEVL_shown_count('lad_music_ty') >= 1",
            pool=False,
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        ))
#lad_music_ty
label Monika_poem_2_test:
    m 6rubla "嗯,[player]."
    m 5fubfb "自从我们从海边回来之后."
    m 2hua "我又作了一首关于我们的诗."
    m 1eub "你现在想看看吗?"
    menu:
        "你现在想看看[m]的诗吗?"
        "想":
            jump want_to_see_her_poem
        "我现在没时间":
            m 3eka "好吧,等你有空了记得看看,好吗?"
            $ mas_unlockEVL("Monika_poem_ladl_2_again", "EVE")
            return


label want_to_see_her_poem:
    m 5hub "好!我就知道你会这么说."
    call mas_showpoem(my_poem_2)
    m 5rubfa "你看完这首觉得怎么样？"
    menu:
        "写的很棒":
            m 5hubfa "真的吗?那太好了,[player]."
            m 3fublb "我希望这首诗能让我们更有希望地走下去."
            $ mas_unlockEVL("Monika_poem_ladl_2_again", "EVE")
            return
        "还需要进步呢":
            m 5hua "嗯好,[player]."
            m 6eub "等我再钻研一下......"
            $ mas_unlockEVL("Monika_poem_ladl_2_again", "EVE")
            return
        "这首诗让我很感动":
            m 5subfa "真的吗?那太好了,[player]."
            m 2fublb "希望这首诗能让我们更有希望地走下去." 
            $ mas_unlockEVL("Monika_poem_ladl_2_again", "EVE")
            return
    return

init 6 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_poem_ladl_2_again",
            category=['文学'],
            prompt="我想再看看你写给我的诗",#已取
            pool=False,
            unlocked=False
        )
    )
label Monika_poem_ladl_2_again:
    m 5hub "好的,[player]."
    call mas_showpoem(my_poem_2)
    return