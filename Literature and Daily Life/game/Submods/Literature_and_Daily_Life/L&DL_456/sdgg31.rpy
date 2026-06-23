init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg31_31",
            category=["生活"],
            prompt="粥",
            random=True                      
        )
    )

label lzp_monika_sdgg31_31:
    m 3eua "[player],你喝过粥吗？"
    m 3eub "我觉得粥是一种非常温柔的食物."
    m 4euu "米香氤氲的白粥、绵密的小米粥,或是带着食材本味的蔬菜粥等等."
    m 1eua "[player],你知道粥经常在哪里出现吗？"
    pause 1.5
    m 1hua "猜到了吗？"
    m 1esd "是医院."
    m 2esc "因为粥,温和,易吸收."
    m 3esc "[player],人总有生病的时候.生病的时候总是什么都不想吃."
    m 3esp "但这样只会更坏."
    m 3tsp "[player],生病的时候至少喝一碗粥好吗？"
    m 3hsa "喝完之后,身体暖洋洋的,病自然也会好得快."
    m 3msa "要是我在你身边,我会为你熬一碗粥的."
    m 3tsu "会有这一天的."
 
    return