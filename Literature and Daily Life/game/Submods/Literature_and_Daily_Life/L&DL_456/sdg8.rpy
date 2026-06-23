init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg8",     
            category=['扮演'],                         
            prompt="[player]的女友",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg8:                       
    m 1wuc "？"
    m 1muc "……"
    m 1tud "不行哦~"
    m 1cud "我才不要扮演你女友."          
    m 1rusdrd "让我去扮演你的女友也太奇怪了吧."
    m 1husdrd "哈哈~"
    m 1dub "[player],你的女友当然是我啦！"

    return