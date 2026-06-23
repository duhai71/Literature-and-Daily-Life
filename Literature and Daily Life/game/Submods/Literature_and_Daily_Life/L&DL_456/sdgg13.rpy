init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg13_13",
            category=["生活"],
            prompt="有害沉默",
            random=True
        )
    )

label lzp_monika_sdgg13_13:
    m 3eua "[player],我注意到在一些书中故事里."
    m 3eta "明明是和主人公很要好的朋友,遇到一些冲突的时候,会选择沉默."
    m 1ruc "但是沉默不能解决任何问题,这也成为了故事之后决裂的导火索."
    m 1luc "就像夏树和优里一样."
    m 1tuc "……"
    m 3tud "[player],我知道在朋友或家庭的关系里,打破沉默很难."
    m 3fubla "但是我相信你可以做到的."
    m 3eubla "感到冒犯就指出来,要是自己做得不对,就承认."
    m 1esbld "只要多和你的朋友、家人交流,他们一定会理解的."
    m 1tsblu "至少我永远会站在你这边."
    m 1tsblb "我永远不会对你保持沉默……"
    
    return