init -990 python:
    store.mas_submod_utils.Submod(
        author="LADL团队",
        name="Literature And Daily Life V3",
        description="包含了大量话题的Submod,涵盖了文学、科学、心理学、生活、情感、闲聊、逻辑、音乐、哲学、约会、游戏等方面,以及人声曲目、钢琴曲目、约会、与MTTS的联动内容.",
        version='3.1.2',
        settings_pane="LADL_setting_pane"
    )


init -951 python:
    import os
    import shutil
    try:
        if os.path.exists(renpy.config.basedir + "/game/Submods/CareStress"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/CareStress")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/CareStress"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/CareStress")    
        if os.path.exists(renpy.config.basedir + "/game/Submods/CoffeeCaffeine"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/CoffeeCaffeine")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/CoffeeCaffeine"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/CoffeeCaffeine")      
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/CoffeeCaffeine"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/CoffeeCaffeine")                  
        if os.path.exists(renpy.config.basedir + "/game/Submods/Consciousness"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Consciousness")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/Consciousness"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/Consciousness")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/Consciousness"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/Consciousness")                     
        if os.path.exists(renpy.config.basedir + "/game/Submods/Monika_Piano_Eternity"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Monika_Piano_Eternity")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/Monika_Piano_Eternity"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/Monika_Piano_Eternity")            
        if os.path.exists(renpy.config.basedir + "/game/Submods/MorningBaking"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/MorningBaking")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/MorningBaking"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/MorningBaking") 
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/MorningBaking"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/MorningBaking")                       
        if os.path.exists(renpy.config.basedir + "/game/Submods/Peachblossom"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Peachblossom")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/Peachblossom"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/Peachblossom")            
        if os.path.exists(renpy.config.basedir + "/game/Submods/PoetryWithMonika"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/PoetryWithMonika")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/PoetryWithMonika"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/PoetryWithMonika") 
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/PoetryWithMonika"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/PoetryWithMonika")                       
        if os.path.exists(renpy.config.basedir + "/game/Submods/Support"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Support")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/Support"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/Support")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/Support"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/Support")                       
        if os.path.exists(renpy.config.basedir + "/game/Submods/TopicGinkgo"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/TopicGinkgo")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/TopicGinkgo"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/TopicGinkgo")            
        if os.path.exists(renpy.config.basedir + "/game/Submods/wisdom_library_ready"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/wisdom_library_ready")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/wisdom_library_ready"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/wisdom_library_ready")  
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/wisdom_library_ready"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/wisdom_library_ready")                      
        if os.path.exists(renpy.config.basedir + "/game/Submods/Nightowl"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Nightowl")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/Nightowl"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/Nightowl")
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/lzp_sdg_sdgg_456"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/lzp_sdg_sdgg_456") 
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/Monika_Piano_Eternity"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/Monika_Piano_Eternity") #                                  
        if os.path.exists(renpy.config.basedir + "/game/mod_assets/music/everythinggoeson.ogg"):
            os.remove(renpy.config.basedir + "/game/mod_assets/music/everythinggoeson.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/Nightowl/topic_nightowl_neuron.rpy"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/Nightowl/topic_nightowl_neuron.rpy" ) 
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/Nightowl/topic_nightowl_neuron.rpyc"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_moon/Nightowl/topic_nightowl_neuron.rpyc" )            
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/All_I_want_for_Christmas_is_You.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/All_I_want_for_Christmas_is_You.ogg" )                                                               
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Are_You_Lost.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Are_You_Lost.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Caught_in_a_Tropical.rar.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Caught_in_a_Tropical.rar.ogg" )#
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Cornfield_Chase.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Cornfield_Chase.ogg" )    
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Golden_Hour.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Golden_Hour.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Kami_no_Mani_Mani.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Kami_no_Mani_Mani.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Love_Me_Like_You_Do.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Love_Me_Like_You_Do.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Odoru_Pompokolin.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Odoru_Pompokolin.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/One_Last_Kiss.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/One_Last_Kiss.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Secret.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Secret.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Shelter_piano.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/Shelter_piano.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/You_Belong_With_Me(piano).ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/You_Belong_With_Me(piano).ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/you_hear_piano.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/you_hear_piano.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/如果爱忘了_piano.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/如果爱忘了_piano.ogg" )
        if os.path.exists(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/everythinggoeson.ogg"):
            os.remove(renpy.config.basedir + "/game/Submods/Literature_and_Daily_Life/L&DL_Assets/music/everythinggoeson.ogg" )
    except Exception as l:
        store.mas_submod_utils.submod_log.error("删除旧版本遗留文件出错：{}".format(l))

define LADL_authors = """\
度海、moon、456、Kxiangtang、哞尼卡、君翌、俩fish、龟酱、Lasagna、华猫、stary.
"""

define LADL_thanks = """\
特别感谢以下人员：
- 测试人员:白莫、庭有枇杷树、最初の心、8天67t9
- 技术支持:最初の心、璀辰、Sir.P、群阿巴阿巴、EdgeInfinity
- 翻译帮助:stary
"""

screen LADL(message, ok_action):
    zorder 225
    modal True
    style_prefix "confirm"

    frame:
        vbox:
            ymaximum 300
            xmaximum 800
            xfill True
            yfill False
            spacing 5

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK") action ok_action

screen LADL_setting_pane():
    vbox:
        xmaximum 800
        xfill True
        style_prefix "check"
        
        textbutton ">团队成员":
            ypos 1
            selected False
            action Show(screen="LADL", message=LADL_authors, ok_action=Hide("LADL"))

        textbutton ">特别感谢":
            ypos 1
            selected False
            action Show(screen="LADL", message=LADL_thanks, ok_action=Hide("LADL"))            