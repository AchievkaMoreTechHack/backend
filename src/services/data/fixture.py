fixtures = [
    {  # 1
        "story_male": '["Привет! Сейчас ты пройдешь увлекательную историю. Но перед тем, как начать, введи свое имя и выбери свой пол"]',
        "story_female": '["Привет! Сейчас ты пройдешь увлекательную историю. Но перед тем, как начать, введи свое имя и выбери свой пол"]',
        "action_type": "edittext",
        "action_data_male": '["Введите ваше имя", "str"]',
        "action_data_female": '["Введите ваше имя", "str"]',
        "background": "cinema.png",
    },
    {  # 2
        "story_male": '["Выбери свой пол"]',
        "story_female": '["Выбери свой пол"]',
        "action_type": "gender",
        "action_data_male": '["Мужчина", "Женщина"]',
        "action_data_female": '["Мужчина", "Женщина"]',
        "background": "white_background.png",
    },
    {  # 3
        "story_male": '["В слегка потных от волнения руках ты держишь телефон, который внезапно стал очень тяжелым", "На экране ярким голубым цветом выделяется крупное число, обозначающее количество денег на счете", "Ты переключаешь вкладку и тянешься пальцем к кнопке \'Купить\'"]',
        "story_female": '["В слегка потных от волнения руках ты держишь телефон, который внезапно стал очень тяжелым", "На экране ярким голубым цветом выделяется крупное число, обозначающее количество денег на счете", "Ты переключаешь вкладку и тянешься пальцем к кнопке \'Купить\'"]',
        "action_type": "button",
        "action_data_male": '["нажать", "4", "не нажимать", "5"]',
        "action_data_female": '["нажать", "4", "не нажимать", "5"]',
        "background": "phone.png",
    },
    {  # 4
        "story_male": '["Нажимаешь. Сердце замирает от ожидания", "— Неужели я решился/решилась на это? Потратить такую большую сумму за одно нажатие!", "Отвлекаясь от мыслей, ты замечаешь резкое изменение графика на экране. Все тело зависло в воздухе и..."]',
        "story_female": '["Нажимаешь. Сердце замирает от ожидания", "— Неужели я решился/решилась на это? Потратить такую большую сумму за одно нажатие!", "Отвлекаясь от мыслей, ты замечаешь резкое изменение графика на экране. Все тело зависло в воздухе и..."]',
        "background": "phone.png",
    },
    {  # 5
        "story_male": '["Спокойно убираешь палец и задумываешься", "Спокойно убираешь палец и задумываешься", "Отвлекаясь от мыслей, ты замечаешь резкое изменение графика на экране. Все тело зависло в воздухе и..."]',
        "story_female": '["Спокойно убираешь палец и задумываешься", "Спокойно убираешь палец и задумываешься", "Отвлекаясь от мыслей, ты замечаешь резкое изменение графика на экране. Все тело зависло в воздухе и..."]',
        "background": "phone.png",
    },
    {  # 6
        "story_male": '["— Потолок, кровать, утро. Я спал/спала! Это все был сон!", "— Фух", "Ты полностью расслабляешься, сердце перестает колотиться, а в голове пробегает мысль полежать в постели еще немного", "— Почему мне снятся такие странные сны? Я никогда всерьез не задумывался об инвестициях. Наверное, я..."]',
        "story_female": '["— Потолок, кровать, утро. Я спал/спала! Это все был сон!", "— Фух", "Ты полностью расслабляешься, сердце перестает колотиться, а в голове пробегает мысль полежать в постели еще немного", "— Почему мне снятся такие странные сны? Я никогда всерьез не задумывался об инвестициях. Наверное, я..."]',
        "action_type": "button",
        "action_data_male": '["хочу заработать", "7", "хочу сберечь деньги", "7", "еще не определился", "7"]',
        "action_data_female": '["хочу заработать", "7", "хочу сберечь деньги", "7", "еще не определилась", "7"]',
        "background": "white_background.png",
    },
    {  # 7
        "story_male": '["Резкий звонок в дверь заставил тебя прервать размышления, посмотреть время и возмутиться тому, что кто-то беспокоит тебя в раннее утро пятницы", "Переваливаясь с одного бока на другой ты встаешь, босиком идешь до двери открываешь и видишь на пороге довольного собой друга"]',
        "story_female": '["Резкий звонок в дверь заставил тебя прервать размышления, посмотреть время и возмутиться тому, что кто-то беспокоит тебя в раннее утро пятницы", "Переваливаясь с одного бока на другой ты встаешь, босиком идешь до двери открываешь и видишь на пороге довольного собой друга"]',
        "background": "room.png",
    },
    {  # 8
        "story_male": '["Д— Добрейшее утречко!", "— Привет, Максим. Ты знаешь, что сегодня у меня выходной? Я планировал/планировала поспать до 12...", "Д— Конечно знаю! А еще у тебя сегодня день рождения, это есть в твоих планах?", "— О, у меня это совсем вылетело из головы", "Тут ты заметил, что Максим держит что-то за спиной", "Он не заставил тебя долго ждать и выставил вперед торт со свечками. Решив проверить, знает ли он твой возраст, ты насчитал"]',
        "story_female": '["Д— Добрейшее утречко!", "— Привет, Максим. Ты знаешь, что сегодня у меня выходной? Я планировал/планировала поспать до 12...", "Д— Конечно знаю! А еще у тебя сегодня день рождения, это есть в твоих планах?", "— О, у меня это совсем вылетело из головы", "Тут ты заметила, что Максим держит что-то за спиной", "Он не заставил тебя долго ждать и выставил вперед торт со свечками. Решив проверить, знает ли он твой возраст, ты насчитала"]',
        "action_type": "edittext",
        "action_data_male": '["25", "int"]',
        "action_data_female": '["25", "int"]',
        "background": "room.png",
        "character": "friend.png",
        "position": "side",
    },
    {  # 9
        "story_male": '["— Спасибо за тортик. Давай..."]',
        "story_female": '["— Спасибо за тортик. Давай..."]',
        "action_type": "button",
        "action_data_male": '["сядем чай попьем", "10", "сначала в парке погуляем", "1000", "сначала сходим в кино", "16"]',
        "action_data_female": '["сядем чай попьем", "10", "сначала в парке погуляем", "1000", "сначала сходим в кино", "16"]',
        "background": "room.png",
        "character": "friend.png",
        "position": "side",
    },
    {  # 10
        "story_male": '["Д— Хорошо, давай"]',
        "story_female": '["Д— Хорошо, давай"]',
        "background": "room.png",
        "character": "friend.png",
        "position": "side",
    },
    {  # 11
        "story_male": '["— Слушай, мне сегодня такой странный сон приснился. У меня была большая сумма денег на счету и я пытался решить, инвестировать ли их", "Д— Это явно что-то значит, ведь он приснился тебе с четверга на пятницу!", "— Пфф, я не верю в такие вещи. Наверное, мне просто хочется побольше денег", "Д— Да, лишние деньги никому никогда не мешали!", "Д— Да, лишние деньги никому никогда не мешали!", "Д— Ты можешь либо покупать акции и тем самым зарабатывать, либо покупать облигации и тем самым сохранять свой капитал во время инфляции", "Ты посмотрел удивленным взглядом на Максима, выгнув одну бровь", "— Ты откуда все это знаешь?", "Д— Да у меня папа увлекается инвестициями, постоянно что-то говорит о них", "Д— Мне эта тема не интересна, но он повторял это настолько часто, что я все назубок выучил", "Вы оба усмехнулись этой странной ситуации"]',
        "story_female": '["— Слушай, мне сегодня такой странный сон приснился. У меня была большая сумма денег на счету и я пыталась решить, инвестировать ли их", "Д— Это явно что-то значит, ведь он приснился тебе с четверга на пятницу!", "— Пфф, я не верю в такие вещи. Наверное, мне просто хочется побольше денег", "Д— Да, лишние деньги никому никогда не мешали!", "Д— Да, лишние деньги никому никогда не мешали!", "Д— Ты можешь либо покупать акции и тем самым зарабатывать, либо покупать облигации и тем самым сохранять свой капитал во время инфляции", "Ты посмотрела удивленным взглядом на Максима, выгнув одну бровь", "— Ты откуда все это знаешь?", "Д— Да у меня папа увлекается инвестициями, постоянно что-то говорит о них", "Д— Мне эта тема не интересна, но он повторял это настолько часто, что я все назубок выучил", "Вы оба усмехнулись этой странной ситуации"]',
        "background": "room.png",
        "character": "friend.png",
        "position": "side",
    },
    {  # 12
        "story_male": '["Максим взял пульт от телевизора и включил его", "По каналу шел мультик про белок"]',
        "story_female": '["Максим взял пульт от телевизора и включил его", "По каналу шел мультик про белок"]',
        "background": "room.png",
        "character": "friend.png",
        "position": "side",
    },
    {  # 13 хз + решительный и хз + нерешительный
        "story_male": '["Одна белка вернулась с прогулки и решила закопать примерно сотую часть своих желудей, забыла про них и через время на том же месте увидела выросшие дубы", "А ее подруга-белка решила не закапывать часть желудей, а отдать ее на хранение желудиному барону, который каждый год ей выдает дополнительно десятую часть желудей от того, что белка принесла", "— Какие странные мультики сейчас показывают по телевизору...", "Тебя вдруг осенило. Это же как акции и облигации!", "Одна белка откладывает часть доходов и инвестирует ее (нет высокой вероятности, что закопанные желуди помогут получить новые). А ее подруга пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не так велик."]',
        "story_female": '["Одна белка вернулась с прогулки и решила закопать примерно сотую часть своих желудей, забыла про них и через время на том же месте увидела выросшие дубы", "А ее подруга-белка решила не закапывать часть желудей, а отдать ее на хранение желудиному барону, который каждый год ей выдает дополнительно десятую часть желудей от того, что белка принесла", "— Какие странные мультики сейчас показывают по телевизору...", "Тебя вдруг осенило. Это же как акции и облигации!", "Одна белка откладывает часть доходов и инвестирует ее (нет высокой вероятности, что закопанные желуди помогут получить новые). А ее подруга пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не так велик."]',
        "description": "Тебе стоит использовать проверенный «Метод шести кувшинов» - подход, помогающий грамотно распределять доход.\nМетод распределяет финансы следующим образом:\n1 кувшин: 55% - необходимые/текущие траты\n2 кувшин: 10% - развлечения\n3 кувшин: 10% - инвестиции\n4 кувшин: 10% - образование\n5 кувшин: 10% - финансовая подушка безопасности\n6 кувшин: 5% - подарки, благотворительность\nЕсли все твои кувшины хранят необходимый процент от дохода, финансы точно будут под контролем.",
        "description_preview": "Ты можешь вкладывать в инвестиции около 10% от своей прибыли.",
        "background": "room.png",
        "character": "squirrel.png",
        "position": "side",
    },
    {  # 14 заработать + нерешительный + решительный
        "story_male": '["Одна белка вернулась с прогулки и решила закопать примерно сотую часть своих желудей, забыла про них и через время на том же месте увидела выросшие дубы", "— Какие странные мультики сейчас показывают по телевизору...", "Тебя вдруг осенило. Это же работает как акции!", "Тебя вдруг осенило. Это же работает как акции!"]',
        "story_female": '["Одна белка вернулась с прогулки и решила закопать примерно сотую часть своих желудей, забыла про них и через время на том же месте увидела выросшие дубы", "— Какие странные мультики сейчас показывают по телевизору...", "Тебя вдруг осенило. Это же работает как акции!", "Тебя вдруг осенило. Это же работает как акции!"]',
        "description": "Тебе стоит использовать проверенный «Метод шести кувшинов» - подход, помогающий грамотно распределять доход.\nМетод распределяет финансы следующим образом:\n1 кувшин: 55% - необходимые/текущие траты\n2 кувшин: 10% - развлечения\n3 кувшин: 10% - инвестиции\n4 кувшин: 10% - образование\n5 кувшин: 10% - финансовая подушка безопасности\n6 кувшин: 5% - подарки, благотворительность\nЕсли все твои кувшины хранят необходимый процент от дохода, финансы точно будут под контролем.",
        "description_preview": "Ты можешь вкладывать в инвестиции до 10% от своей прибыли.",
        "background": "room.png",
        "character": "squirrel.png",
        "position": "side",
    },
    {  # 15 сохранение
        "story_male": '["Белка решила отдать часть своих желудей на хранение желудиному барону, который каждый год выдает дополнительно десятую часть орешков от того количества, что принесла белка.", "— Какие странные мультики сейчас показывают по телевизору...", "Тебя вдруг осенило. Это же похоже на облигации!", "Белка пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не очень велик."]',
        "story_female": '["Белка решила отдать часть своих желудей на хранение желудиному барону, который каждый год выдает дополнительно десятую часть орешков от того количества, что принесла белка.", "— Какие странные мультики сейчас показывают по телевизору...", "Тебя вдруг осенило. Это же похоже на облигации!", "Белка пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не очень велик."]',
        "description": "Тебе стоит использовать проверенный «Метод шести кувшинов» - подход, помогающий грамотно распределять доход.\nМетод распределяет финансы следующим образом:\n1 кувшин: 55% - необходимые/текущие траты\n2 кувшин: 10% - развлечения\n3 кувшин: 10% - инвестиции\n4 кувшин: 10% - образование\n5 кувшин: 10% - финансовая подушка безопасности\n6 кувшин: 5% - подарки, благотворительность\nЕсли все твои кувшины хранят необходимый процент от дохода, финансы точно будут под контролем.",
        "description_preview": "Ты можешь вкладывать в инвестиции до 10% от своей прибыли.",
        "background": "room.png",
        "character": "squirrel.png",
        "position": "side",
    },
    {  # 16 Кино хз решительность + нет
        "story_male": '["В мультфильме главная героиня-белка вернулась с прогулки и решила закопать примерно сотую часть своих желудей, забыла про них и через время на том же месте увидела выросшие дубы", "А ее подруга-белка решила не закапывать часть желудей, а отдать ее на хранение желудиному барону, который каждый год выдает дополнительно десятую часть желудей от того количества, что белка принесла", "Какие странные мультики сейчас показывают в кинотеатрах...", "- А мне понравилось. В твоем сне инвестиции, в мультфильме инвестиции. Это какой-то знак", "Причем здесь инвестиции?", "- Одна белка откладывает часть доходов и инвестирует ее (нет высокой вероятности, что закопанные желуди помогут получить новые). А ее подруга пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не так велик. Первая зверушка вкладывает в акции, вторая - в инвестиции.", "Хах, а классно они это придумали, я даже сначала и не понял..."]',
        "story_female": '["В мультфильме главная героиня-белка вернулась с прогулки и решила закопать примерно сотую часть своих желудей, забыла про них и через время на том же месте увидела выросшие дубы", "А ее подруга-белка решила не закапывать часть желудей, а отдать ее на хранение желудиному барону, который каждый год выдает дополнительно десятую часть желудей от того количества, что белка принесла", "Какие странные мультики сейчас показывают в кинотеатрах...", "- А мне понравилось. В твоем сне инвестиции, в мультфильме инвестиции. Это какой-то знак", "Причем здесь инвестиции?", "- Одна белка откладывает часть доходов и инвестирует ее (нет высокой вероятности, что закопанные желуди помогут получить новые). А ее подруга пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не так велик. Первая зверушка вкладывает в акции, вторая - в инвестиции.", "Хах, а классно они это придумали, я даже сначала и не понял..."]',
        "description": "Тебе стоит использовать проверенный «Метод шести кувшинов» - подход, помогающий грамотно распределять доход.\nМетод распределяет финансы следующим образом:\n1 кувшин: 55% - необходимые/текущие траты\n2 кувшин: 10% - развлечения\n3 кувшин: 10% - инвестиции\n4 кувшин: 10% - образование\n5 кувшин: 10% - финансовая подушка безопасности\n6 кувшин: 5% - подарки, благотворительность\nЕсли все твои кувшины хранят необходимый процент от дохода, финансы точно будут под контролем.",
        "description_preview": "Ты можешь вкладывать в инвестиции до 10% от своей прибыли.",
        "background": "cinema.png",
        "character": "squirrel.png",
        "position": "side",
    },
    {  # 17 Кино заработок решительность + нет
        "story_male": '["В мультфильме главная героиня-белка вернулась с прогулки и решила закопать примерно сотую часть своих желудей, забыла про них и через время на том же месте увидела выросшие дубы", "Какие странные мультики сейчас показывают в кинотеатрах...", "- А мне понравилось. В твоем сне инвестиции, в мультфильме инвестиции. Это какой-то знак", "Причем здесь инвестиции?", "- Белка откладывает часть доходов и инвестирует ее (нет абсолютной гарантии, что закопанные желуди помогут получить новые орешки). Зверушка вкладывает в акции", "Хах, а классно они это придумали, я даже сначала и не понял..."]',
        "story_female": '["В мультфильме главная героиня-белка вернулась с прогулки и решила закопать примерно сотую часть своих желудей, забыла про них и через время на том же месте увидела выросшие дубы", "Какие странные мультики сейчас показывают в кинотеатрах...", "- А мне понравилось. В твоем сне инвестиции, в мультфильме инвестиции. Это какой-то знак", "Причем здесь инвестиции?", "- Белка откладывает часть доходов и инвестирует ее (нет абсолютной гарантии, что закопанные желуди помогут получить новые орешки). Зверушка вкладывает в акции", "Хах, а классно они это придумали, я даже сначала и не понял..."]',
        "description": "Тебе стоит использовать проверенный «Метод шести кувшинов» - подход, помогающий грамотно распределять доход.\nМетод распределяет финансы следующим образом:\n1 кувшин: 55% - необходимые/текущие траты\n2 кувшин: 10% - развлечения\n3 кувшин: 10% - инвестиции\n4 кувшин: 10% - образование\n5 кувшин: 10% - финансовая подушка безопасности\n6 кувшин: 5% - подарки, благотворительность\nЕсли все твои кувшины хранят необходимый процент от дохода, финансы точно будут под контролем.",
        "description_preview": "Ты можешь вкладывать в инвестиции до 10% от своей прибыли.",
        "background": "cinema.png",
        "character": "squirrel.png",
        "position": "side",
    },
    {  # 18 Кино сохранение решительность + нет
        "story_male": '["В мультфильме главная героиня-белка вернулась с прогулки и решила закопать примерно сотую часть своих желудей, забыла про них и через время на том же месте увидела выросшие дубы", "А ее подруга-белка решила не закапывать часть желудей, а отдать ее на хранение желудиному барону, который каждый год выдает дополнительно десятую часть желудей от того количества, что белка принесла", "Какие странные мультики сейчас показывают в кинотеатрах...", "- А мне понравилось. В твоем сне инвестиции, в мультфильме инвестиции. Это какой-то знак", "Причем здесь инвестиции?", "- Одна белка откладывает часть доходов и инвестирует ее (нет высокой вероятности, что закопанные желуди помогут получить новые). А ее подруга пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не так велик. Первая зверушка вкладывает в акции, вторая - в инвестиции.", "Хах, а классно они это придумали, я даже сначала и не понял..."]',
        "story_female": '["В мультфильме главная героиня-белка вернулась с прогулки и решила закопать примерно сотую часть своих желудей, забыла про них и через время на том же месте увидела выросшие дубы", "А ее подруга-белка решила не закапывать часть желудей, а отдать ее на хранение желудиному барону, который каждый год выдает дополнительно десятую часть желудей от того количества, что белка принесла", "Какие странные мультики сейчас показывают в кинотеатрах...", "- А мне понравилось. В твоем сне инвестиции, в мультфильме инвестиции. Это какой-то знак", "Причем здесь инвестиции?", "- Одна белка откладывает часть доходов и инвестирует ее (нет высокой вероятности, что закопанные желуди помогут получить новые). А ее подруга пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не так велик. Первая зверушка вкладывает в акции, вторая - в инвестиции.", "Хах, а классно они это придумали, я даже сначала и не понял..."]',
        "description": "Тебе стоит использовать проверенный «Метод шести кувшинов» - подход, помогающий грамотно распределять доход.\nМетод распределяет финансы следующим образом:\n1 кувшин: 55% - необходимые/текущие траты\n2 кувшин: 10% - развлечения\n3 кувшин: 10% - инвестиции\n4 кувшин: 10% - образование\n5 кувшин: 10% - финансовая свобода (или деньги на инвестиции)\n6 кувшин: 5% - подарки, благотворительность\nЕсли все твои кувшины хранят необходимый процент от дохода, финансы точно будут под контролем.",
        "description_preview": "Ты можешь вкладывать в инвестиции около 10% от своей прибыли.",
        "background": "cinema.png",
        "character": "squirrel.png",
        "position": "side",
    },
    {  # 19 Парк хз решительность + нет
        "story_male": '["Гуляя по парку, ты с другом замечаешь трех белочек", "Друг: Посмотри на первую, что закапывает желуди. Она скоро забудет про них, но через время на этом же месте могут появиться дубы.", "Точно! Посмотри, другие две тоже чем-то занимаются.", "Друг: Одна из белок напоминает мне какого-то барона из-за своих пышных форм. А если это так и есть? Представь, одна белочка отдает часть своих желудей этому барону, а он каждый год выдает дополнительно десятую часть орешков от того количества, что принесла эта белка.", "Ну и фантазия у тебя!", "Тебя вдруг осенило. Это же как акции и облигации!", "Одна белка откладывает часть доходов и инвестирует ее (нет высокой вероятности, что закопанные желуди помогут получить новые). А ее подруга пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не так велик."]',
        "story_female": '["Гуляя по парку, ты с другом замечаешь трех белочек", "Друг: Посмотри на первую, что закапывает желуди. Она скоро забудет про них, но через время на этом же месте могут появиться дубы.", "Точно! Посмотри, другие две тоже чем-то занимаются.", "Друг: Одна из белок напоминает мне какого-то барона из-за своих пышных форм. А если это так и есть? Представь, одна белочка отдает часть своих желудей этому барону, а он каждый год выдает дополнительно десятую часть орешков от того количества, что принесла эта белка.", "Ну и фантазия у тебя!", "Тебя вдруг осенило. Это же как акции и облигации!", "Одна белка откладывает часть доходов и инвестирует ее (нет высокой вероятности, что закопанные желуди помогут получить новые). А ее подруга пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не так велик."]',
        "description": "Тебе стоит использовать проверенный «Метод шести кувшинов» - подход, помогающий грамотно распределять доход.\nМетод распределяет финансы следующим образом:\n1 кувшин: 55% - необходимые/текущие траты\n2 кувшин: 10% - развлечения\n3 кувшин: 10% - инвестиции\n4 кувшин: 10% - образование\n5 кувшин: 10% - финансовая свобода (или деньги на инвестиции)\n6 кувшин: 5% - подарки, благотворительность\nЕсли все твои кувшины хранят необходимый процент от дохода, финансы точно будут под контролем.",
        "description_preview": "Ты можешь вкладывать в инвестиции около 10% от своей прибыли.",
        "background": "park.png",
        "character": "three_squirrels.png",
        "position": "side",
    },
    {  # 20 Парк заработать решительность + нет
        "story_male": '["Гуляя по парку, ты с другом замечаешь белочку", "Друг: Посмотри на нее, она закапывает желуди. Белка скоро забудет про них, но через время на этом же месте могут появиться дубы.", "- Точно!", "Тебя вдруг осенило. Это же работает как акции!", "Белка откладывает часть доходов и инвестирует ее (нет абсолютной гарантии, что закопанные желуди помогут получить новые орешки)."]',
        "story_female": '["Гуляя по парку, ты с другом замечаешь белочку", "Друг: Посмотри на нее, она закапывает желуди. Белка скоро забудет про них, но через время на этом же месте могут появиться дубы.", "- Точно!", "Тебя вдруг осенило. Это же работает как акции!", "Белка откладывает часть доходов и инвестирует ее (нет абсолютной гарантии, что закопанные желуди помогут получить новые орешки)."]',
        "description": "Тебе стоит использовать проверенный «Метод шести кувшинов» - подход, помогающий грамотно распределять доход.\nМетод распределяет финансы следующим образом:\n1 кувшин: 55% - необходимые/текущие траты\n2 кувшин: 10% - развлечения\n3 кувшин: 10% - инвестиции\n4 кувшин: 10% - образование\n5 кувшин: 10% - финансовая свобода (или деньги на инвестиции)\n6 кувшин: 5% - подарки, благотворительность\nЕсли все твои кувшины хранят необходимый процент от дохода, финансы точно будут под контролем.",
        "description_preview": "Ты можешь вкладывать в инвестиции около 10% от своей прибыли.",
        "background": "park.png",
        "character": "squirrel.png",
        "position": "side",
    },
    {  # 21 Парк сохранить решительность + нет
        "story_male": '["Гуляя по парку, ты с другом замечаешь двух белочек", "Друг: Одна из белок напоминает мне какого-то барона из-за своих пышных форм. А если это так и есть? Представь, белочка отдает часть своих желудей этому барону, а он каждый год выдает дополнительно десятую часть орешков от того количества, что принесла эта белка.", "- Ну и фантазия у тебя!", "Тебя вдруг осенило. Это же похоже на облигации!", "Белка пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не так велик."]',
        "story_female": '["Гуляя по парку, ты с другом замечаешь двух белочек", "Друг: Одна из белок напоминает мне какого-то барона из-за своих пышных форм. А если это так и есть? Представь, белочка отдает часть своих желудей этому барону, а он каждый год выдает дополнительно десятую часть орешков от того количества, что принесла эта белка.", "- Ну и фантазия у тебя!", "Тебя вдруг осенило. Это же похоже на облигации!", "Белка пользуется проверенным методом, который точно сохраняет всю вложенную желудиную валюту, но коэффициент роста не так велик."]',
        "description": "Тебе стоит использовать проверенный «Метод шести кувшинов» - подход, помогающий грамотно распределять доход.\nМетод распределяет финансы следующим образом:\n1 кувшин: 55% - необходимые/текущие траты\n2 кувшин: 10% - развлечения\n3 кувшин: 10% - инвестиции\n4 кувшин: 10% - образование\n5 кувшин: 10% - финансовая свобода (или деньги на инвестиции)\n6 кувшин: 5% - подарки, благотворительность\nЕсли все твои кувшины хранят необходимый процент от дохода, финансы точно будут под контролем.",
        "description_preview": "Ты можешь вкладывать в инвестиции около 10% от своей прибыли.",
        "background": "park.png",
        "character": "family_squirrel.png",
        "position": "side",
    },

]

'''
    {
        "story_male": '',
        "story_female": '',
        "description": "",
        "description_preview": "",
        "action_type": "",
        "action_data_male": '',
        "action_data_female": '',
        "background": "",
        "character": "",
        "position": "",
    },
'''
