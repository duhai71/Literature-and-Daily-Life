#story 1
init 5 python:
    addEvent(
        Event(
            persistent._mas_story_database,
            eventlabel="ladl_add_mas_story_1",
            category=[mas_stories.TYPE_NORMAL],
            prompt="",
            unlocked=False),  
        code="STY")

label ladl_add_mas_story_1:
    call mas_story_begin                        
    m 1hua "赵云的故事吗?我很乐意和你说说他."
    m 3eud "."
    m 1eub "."
    m 3eua "."
    m 1hua ""
    m 1eka ""
    m 1hub "."
    pause 3
    m 1hub "[player]?"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_story_database,
            eventlabel="ladl_add_mas_story_2",
            category=[mas_stories.TYPE_NORMAL],
            prompt="遥远的街区",
            unlocked=False),  
        code="STY")

label ladl_add_mas_story_2:
    m 5hua "嗯,现在我们"

