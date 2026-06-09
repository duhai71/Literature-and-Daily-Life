init -10 python:
    #音乐
    audio.beach_park = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/BGM00043.mp3"#海边小公园
    audio.beach_music = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/refreshing_moning.mp3"
    audio.beach_bgm = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/summer_sea.mp3"#开场用
    audio.beach_event = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/Sunset_Bridge.mp3"
    audio.city_event = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/color_your_night.mp3"
    audio.city_bgm = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/color_your_night.mp3"   
    audio.beach_bgm_2 = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/L&DL_00043.mp3"   #轻松  
    audio.hill_use = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/秋_木.mp3"
    audio.hill_play = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/walk_hill.mp3"
    audio.tamsu03_play = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/tamsu03.mp3"#旅馆后院用
    audio.tam_n17_play = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/tam_n17.mp3"
    audio.Dream = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/dream.mp3"#未响度统一
    audio.dream_after = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/dream_after.mp3"
    audio.Walking_Path = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/Walking_Path.mp3"
    audio.Frieren = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/勇者.mp3"#浴室用
    audio.want_to_be_close = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/want_to_be_close.mp3"
    audio.joy = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/joy.mp3"
    audio.date_Renai_Circulation = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/恋爱循环.mp3"
    audio.date_2001 = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/2001.mp3"
    audio.Beneath_the_Mask = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/Beneath_the_Mask.mp3"
    audio.closer = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/closer.mp3"
    audio.sea = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_music/sea.mp3"
    #后续加p3r 小曲进入v4约会内容
    renpy.music.register_channel("LADL", "music", loop=True, tight=True)#循环
    renpy.music.register_channel("LADL_1", "sfx", loop=False, tight=True)
    # 音效
    audio.waves = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_sound/waves.mp3"      # 海浪声
    audio.wihh = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_sound/walking_in_high_heels.mp3"        # 高跟鞋走路声
    audio.subway = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_sound/subway.mp3"  # 地铁
    audio.footstep_beach = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_sound/walking_on_the_beach.mp3"  #沙滩走路
    audio.bird_sound = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_sound/mus_birdnoise.mp3"#鸟叫
    audio.knock_on_the_door_sound = "Submods/Literature_and_Daily_Life/L&DL_date/L&DL_date_sound/敲门.mp3"#敲门
    

    renpy.music.register_channel("LADL_sfx1", "sfx", loop=False, tight=True)
    renpy.music.register_channel("LADL_sfx2", "sfx", loop=True, tight=True)  # 用于循环
#label start:
#    play music bgm_main fadein 3.0
    
    
    # 切换音乐
#    play music bgm_romance fadeout 2.0 fadein 2.0
    
 #   "浪漫的场景..."
    
 #   play ambience "audio/ambience/forest.ogg" volume 0.3
    
 #   "在森林中..."
    
    # 停止环境音
 #   stop ambience fadeout 1.0
    


    #label beach_scene:
 #   play music beach_bgm fadein 2.0
  #  play sfx2 waves volume 0.3  # 循环海浪声
   # "我们来到了海边..."
    
    #play sfx1 seagull volume 0.5
   # "#海鸥从头顶飞过。"
    
   # play sfx2 wind volume 0.2  # 循环风声
    #"微风轻轻吹拂..."
    
   # stop sfx2 fadeout 1.0  # 停止环境音效
    #"我们离开了海边。"