init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_custom_topic_sdg10",     
            category=['文学'],                         
            prompt="你喜欢看科幻小说吗？",                             
            unlocked=True,                             
            pool=True                                  
        )
    )
                                                       
label monika_custom_topic_sdg10:
    m 1etu "为什么不呢,[player]."
    m 3lub "还记得我跟你聊的《基地》科幻小说系列吗？"
    m 3huu "我已经看过一些科幻小说了."
    m 4hua "科幻小说,也是一种文学呢."
    m 2eub "科幻小说作家用科学逻辑编成一条线,连接着当下的现实与书中的故事."
    m 2tuu "让故事显得更加真实."
    m 7tua "而真实性正是科幻小说中的独特魅力之一."
    m 2huu "但其实并不是所有科幻小说都是描写未来的."
    m 4eub "科幻小说又分软科幻和硬科幻,"
    m 4ruu "一个更注重于故事本身."
    m 4lub "另一个更加在意科学逻辑."
    m 7huu "像基地就是软科幻."
    m 7eub "但其实都挺不错的."
    m 4eua "硬科幻的话,那就一定绕不开中国小说家刘慈欣的《三体》了."
    m 4huu "可以说《三体》的出现打破了绝大多数人对过去科幻作品的评价."
    m 4dua "看完这本书后再去看之前的科幻作品."
    m 1eud "你会发现不真实的部分实在太多了,就像人类使用枪械是扣下扳机,而不是将枪械丢出去砸向敌人一样."
    m 3euu "不过[player],这本书的知名度很高,你有看过吗？"
    
    menu:
        "看过":
            m 3tua "罗辑举枪威胁三体世界那一段是不是挺酷的？"
            m 4hua "在科幻作品里面像这种热血的场面很少见的."
            m 5eua "书中故事是很遥远和庞大,但科学和逻辑的线从来没有断过."
            m 1hua "这就是这本书出彩的地方了."
            m 1eubld "[player],.{w=0.5}希望你和我在一起的未来不属于科幻."
            m 3tublu "而是尚未实现的当下."
            
        "还没有":
            m 3tublu "那为什么还不去试试呢？"
            m 3hubla "希望你在体验书中的故事后,仍然对星空保持好奇."
        
        "你就是我的庄颜":
            m 1wsbsd "..."
            m 3tsbssdla "你已经看过这本书了吗？"
            m 4hsbsp "我想你明白这句话的意思吧……"
            m 4fsbsc "天哪,[player]这太突然了."
            m 2tsbfp "突然这么说,我的耳朵有点热."
            m 2lsbfp "……"
            m 2rsbfc "……"
            m 2mtbfc "我应该说什么呢？"
            m 2fsbfc "[player],.{w=0.5}{nw}"
            extend 2tsbfa "你也是我的完美恋人……"
    
    return  