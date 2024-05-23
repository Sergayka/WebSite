from DB.init_db import SessionLocal, Accessories, Shoes, Jacket, Pants, Shirt, TShirt, Shorts, Category, Item


def add_data(session):
    # Создание категорий
    categories = {
        "Шорты": Category(name="Шорты", description="Все виды шорт", photo_url="https://a.lmcdn.ru/product/M/P/MP002XM00APJ_22828720_1_v1_2x.jpg"),
        "Футболки": Category(name="Футболки", description="Все виды футболок", photo_url="https://a.lmcdn.ru/img600x866/R/T/RTLADG598101_22544744_4_v1_2x.jpg"),
        "Рубашки": Category(name="Рубашки", description="Все виды рубашек", photo_url="https://a.lmcdn.ru/product/M/P/MP002XM0SXFM_20159324_5_v1_2x.jpeg"),
        "Брюки": Category(name="Брюки", description="Все виды брюк", photo_url="https://a.lmcdn.ru/img600x866/M/P/MP002XM0073R_22479516_1_v1_2x.jpeg"),
        "Куртки": Category(name="Куртки", description="Все виды курток", photo_url="https://a.lmcdn.ru/product/R/T/RTLACZ834501_21238014_3_v1_2x.jpg"),
        "Обувь": Category(name="Обувь", description="Все виды обуви", photo_url="https://a.lmcdn.ru/img600x866/M/P/MP002XM001FL_22845111_4_v1.jpg"),
        "Аксессуары": Category(name="Аксессуары", description="Все виды аксессуаров", photo_url="https://a.lmcdn.ru/img600x866/R/T/RTLABK458304_22318029_1_v1_2x.jpg")
    }
    session.add_all(categories.values())
    session.commit()

    # Добавление шортов
    shorts_data = [
        {"name": "Шорты для плавания", "description": "Шорты для плавания", "price": 1299.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00JXF_23235720_1_v1_2x.jpg", "size": "S",
         "category_id": categories['Шорты'].id},
        {"name": "Спортивные шорты", "description": "Удобные спортивные шорты", "price": 1999.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00CHT_22990428_1_v1_2x.jpg", "size": "M",
         "category_id": categories['Шорты'].id},
        {"name": "Камуфляжные шорты", "description": "Шорты с камуфляжным принтом", "price": 1799.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00IUU_23164719_1_v1_2x.jpg", "size": "M",
         "category_id": categories['Шорты'].id},
        {"name": "Пляжные шорты", "description": "Яркие пляжные шорты", "price": 1499.99,
         "photo_url": "https://a.lmcdn.ru/product/R/T/RTLABC180201_16294183_1_v1_2x.jpg", "size": "L",
         "category_id": categories['Шорты'].id},
        {"name": "Шорты для бега", "description": "Легкие шорты для бега", "price": 2499.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00APJ_22828720_1_v1_2x.jpg", "size": "XL",
         "category_id": categories['Шорты'].id}
    ]

    for data in shorts_data:
        session.add(Shorts(**data))

    # Добавление футболок
    tshirts_data = [
        {"name": "Оранжевая футболка", "description": "Классическая белая футболка", "price": 999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM00LVV_23258467_4_v1_2x.jpeg", "color": "Оранжевый",
         "category_id": categories['Футболки'].id},
        {"name": "Черная футболка", "description": "Классическая черная футболка", "price": 999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADG598101_22544744_4_v1_2x.jpg", "color": "Черный",
         "category_id": categories['Футболки'].id},
        {"name": "Футболка с принтом", "description": "Футболка с оригинальным принтом", "price": 1499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLACV737101_20880413_4_v1_2x.jpg", "color": "Разноцветный",
         "category_id": categories['Футболки'].id},
        {"name": "Спортивная футболка", "description": "Дышащая спортивная футболка", "price": 1999.99,
         "photo_url": "https://a.lmcdn.ru/product/A/D/AD002EMLUFQ1_14164293_4_v2_2x.jpg", "color": "Синий",
         "category_id": categories['Футболки'].id}
    ]
    for data in tshirts_data:
        session.add(TShirt(**data))

    # Добавление рубашек
    shirts_data = [
        {"name": "Белая рубашка", "description": "Классическая белая рубашка", "price": 2499.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00MKA_23376595_4_v1_2x.jpg",
         "material": "Хлопок", "category_id": categories['Рубашки'].id},
        {"name": "Рубашка в клетку", "description": "Рубашка модная для повседневной носки", "price": 2999.99,
         "photo_url": "https://a.lmcdn.ru/product/R/T/RTLADK407701_23183171_1_v1.jpg",
         "material": "Фланель", "category_id": categories['Рубашки'].id},
        {"name": "Джинсовая рубашка", "description": "Стильная рубашка", "price": 3499.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM0SXFM_20159324_5_v1_2x.jpeg",
         "material": "Джинса", "category_id": categories['Рубашки'].id},
        {"name": "Льняная рубашка", "description": "Легкая льняная рубашка", "price": 3999.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00KFM_23286724_4_v1_2x.jpg",
         "material": "Лен", "category_id": categories['Рубашки'].id},
   ]
    for data in shirts_data:
        session.add(Shirt(**data))

    # Добавление брюк
    pants_data = [
        {"name": "Классические брюки", "description": "Классические черные брюки", "price": 2999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM00LTA_23368118_1_v1_2x.jpg", "length": "Длинные",
         "category_id": categories['Брюки'].id},
        {"name": "Спортивные брюки", "description": "Удобные спортивные брюки", "price": 1999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLAAU377601_15423268_1_v2_2x.jpg", "length": "Средние",
         "category_id": categories['Брюки'].id},
        {"name": "Джинсы", "description": "Стильные брюки", "price": 3499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM00FNA_23247395_1_v4_2x.jpg", "length": "Длинные",
         "category_id": categories['Брюки'].id},
        {"name": "Шорты-брюки", "description": "Официальные брюки", "price": 1499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM1RHHU_15031454_1_v1_2x.jpg", "length": "Короткие",
         "category_id": categories['Брюки'].id},
        {"name": "Льняные брюки", "description": "Легкие льняные брюки", "price": 3999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM0073R_22479516_1_v1_2x.jpeg", "length": "Длинные",
         "category_id": categories['Брюки'].id}
    ]
    for data in pants_data:
        session.add(Pants(**data))

    # Добавление курток
    jackets_data = [
        {"name": "Кожаная куртка", "description": "Крутая кожаная куртка", "price": 7999.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM256XO_21542971_3_v1_2x.jpg", "warmth_rating": 7,
         "category_id": categories['Куртки'].id},
        {"name": "Зимняя куртка", "description": "Теплая зимняя куртка", "price": 5999.99,
         "photo_url": "https://a.lmcdn.ru/product/R/T/RTLACZ834501_21238014_3_v1_2x.jpg", "warmth_rating": 10,
         "category_id": categories['Куртки'].id},
        {"name": "Межсезонная куртка", "description": "Модная джинсовая куртка", "price": 4499.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM1UB2J_20977965_3_v1.jpeg", "warmth_rating": 4,
         "category_id": categories['Куртки'].id},
        {"name": "Ветровка", "description": "Удобная ветровка", "price": 2999.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00F6E_23108979_3_v1_2x.jpg", "warmth_rating": 3,
         "category_id": categories['Куртки'].id},
        {"name": "Весенняя куртка", "description": "Легкая весенняя куртка", "price": 3999.99,
         "photo_url": "https://a.lmcdn.ru/product/R/T/RTLADO002101_23618500_3_v1_2x.jpg", "warmth_rating": 5,
         "category_id": categories['Куртки'].id}
    ]
    for data in jackets_data:
        session.add(Jacket(**data))

    # Добавление обуви
    shoes_data = [
        {"name": "Кроссовки", "description": "Удобные кроссовки для бега", "price": 4999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADL945301_23523976_3_v1.jpg", "size": "42",
         "category_id": categories['Обувь'].id},
        {"name": "Ботинки", "description": "Сланцы", "price": 6499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM1HAF7_13672438_4_v1.jpg", "size": "44",
         "category_id": categories['Обувь'].id},
        {"name": "Туфли", "description": "Классические туфли", "price": 3999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADI082901_22897585_3_v1_2x.jpg", "size": "43",
         "category_id": categories['Обувь'].id},
        {"name": "Сандалии", "description": "Легкие сандалии для лета", "price": 2999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM001FL_22845111_4_v1.jpg", "size": "41",
         "category_id": categories['Обувь'].id},
        {"name": "Спортивная обувь", "description": "Обувь для спортивных тренировок", "price": 5499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADC690501_21763471_3_v2_2x.jpg", "size": "42",
         "category_id": categories['Обувь'].id}
    ]
    for data in shoes_data:
        session.add(Shoes(**data))

    # Добавление аксессуаров
    accessories_data = [
        {"name": "Шапка", "description": "Теплая зимняя шапка", "price": 999.99,
         "photo_url": "https://via.placeholder.com/150", "type": "Головной убор",
         "category_id": categories['Аксессуары'].id},
        {"name": "Перчатки", "description": "Кожаные перчатки", "price": 1499.99,
         "photo_url": "https://via.placeholder.com/150", "type": "Рукавицы",
         "category_id": categories['Аксессуары'].id},
        {"name": "Шарф", "description": "Шерстяной шарф", "price": 1299.99,
         "photo_url": "https://via.placeholder.com/150", "type": "Шея", "category_id": categories['Аксессуары'].id},
        {"name": "Ремень", "description": "Кожаный ремень", "price": 1999.99,
         "photo_url": "https://via.placeholder.com/150", "type": "Пояс", "category_id": categories['Аксессуары'].id},
        {"name": "Солнцезащитные очки", "description": "Очки с УФ-защитой", "price": 2499.99,
         "photo_url": "https://via.placeholder.com/150", "type": "Глаза", "category_id": categories['Аксессуары'].id},
        {"name": "Часы", "description": "Крутые часы", "price": 29999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADN729901_23556056_1_v1_2x.jpg", "type": "Головной убор",
         "category_id": categories['Аксессуары'].id},
        {"name": "Солнцезащитные очки", "description": "Очки с УФ-защитой", "price": 2499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADJ937901_22853417_1_v1.jpg", "type": "Глаза",
         "category_id": categories['Аксессуары'].id},
        {"name": "Рюкзак", "description": "Кожанный рюкзак", "price": 8299.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLABK458304_22318029_1_v1_2x.jpg", "type": "Шея",
         "category_id": categories['Аксессуары'].id},
        {"name": "Сумка", "description": "Кожаная сумка", "price": 1499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADJ937901_22853417_1_v1.jpg", "type": "Рукавицы",
         "category_id": categories['Аксессуары'].id}
    ]
    for data in accessories_data:
        session.add(Accessories(**data))

    items_data = [
        {"name": "Шорты для плавания", "description": "Шорты для плавания", "price": 1299.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00JXF_23235720_1_v1_2x.jpg",
         "category_id": categories['Шорты'].id},
        {"name": "Спортивные шорты", "description": "Удобные спортивные шорты", "price": 1999.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00CHT_22990428_1_v1_2x.jpg",
         "category_id": categories['Шорты'].id},
        {"name": "Камуфляжные шорты", "description": "Шорты с камуфляжным принтом", "price": 1799.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00IUU_23164719_1_v1_2x.jpg",
         "category_id": categories['Шорты'].id},
        {"name": "Пляжные шорты", "description": "Яркие пляжные шорты", "price": 1499.99,
         "photo_url": "https://a.lmcdn.ru/product/R/T/RTLABC180201_16294183_1_v1_2x.jpg",
         "category_id": categories['Шорты'].id},
        {"name": "Шорты для бега", "description": "Легкие шорты для бега", "price": 2499.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00APJ_22828720_1_v1_2x.jpg",
         "category_id": categories['Шорты'].id},

        {"name": "Оранжевая футболка", "description": "Классическая белая футболка", "price": 999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM00LVV_23258467_4_v1_2x.jpeg",
         "category_id": categories['Футболки'].id},
        {"name": "Черная футболка", "description": "Классическая черная футболка", "price": 999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADG598101_22544744_4_v1_2x.jpg",
         "category_id": categories['Футболки'].id},
        {"name": "Футболка с принтом", "description": "Футболка с оригинальным принтом", "price": 1499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLACV737101_20880413_4_v1_2x.jpg",
         "category_id": categories['Футболки'].id},
        {"name": "Спортивная футболка", "description": "Дышащая спортивная футболка", "price": 1999.99,
         "photo_url": "https://a.lmcdn.ru/product/A/D/AD002EMLUFQ1_14164293_4_v2_2x.jpg",
         "category_id": categories['Футболки'].id},

        {"name": "Белая рубашка", "description": "Классическая белая рубашка", "price": 2499.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00MKA_23376595_4_v1_2x.jpg", "category_id": categories['Рубашки'].id},
        {"name": "Рубашка в клетку", "description": "Рубашка модная для повседневной носки", "price": 2999.99,
         "photo_url": "https://a.lmcdn.ru/product/R/T/RTLADK407701_23183171_1_v1.jpg", "category_id": categories['Рубашки'].id},
        {"name": "Джинсовая рубашка", "description": "Стильная рубашка", "price": 3499.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM0SXFM_20159324_5_v1_2x.jpeg", "category_id": categories['Рубашки'].id},
        {"name": "Льняная рубашка", "description": "Легкая льняная рубашка", "price": 3999.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00KFM_23286724_4_v1_2x.jpg", "category_id": categories['Рубашки'].id},

        {"name": "Классические брюки", "description": "Классические черные брюки", "price": 2999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM00LTA_23368118_1_v1_2x.jpg",
         "category_id": categories['Брюки'].id},
        {"name": "Спортивные брюки", "description": "Удобные спортивные брюки", "price": 1999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLAAU377601_15423268_1_v2_2x.jpg",
         "category_id": categories['Брюки'].id},
        {"name": "Джинсы", "description": "Стильные брюки", "price": 3499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM00FNA_23247395_1_v4_2x.jpg",
         "category_id": categories['Брюки'].id},
        {"name": "Шорты-брюки", "description": "Официальные брюки", "price": 1499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM1RHHU_15031454_1_v1_2x.jpg",
         "category_id": categories['Брюки'].id},
        {"name": "Льняные брюки", "description": "Легкие льняные брюки", "price": 3999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM0073R_22479516_1_v1_2x.jpeg",
         "category_id": categories['Брюки'].id},

        {"name": "Кожаная куртка", "description": "Крутая кожаная куртка", "price": 7999.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM256XO_21542971_3_v1_2x.jpg",
         "category_id": categories['Куртки'].id},
        {"name": "Зимняя куртка", "description": "Теплая зимняя куртка", "price": 5999.99,
         "photo_url": "https://a.lmcdn.ru/product/R/T/RTLACZ834501_21238014_3_v1_2x.jpg",
         "category_id": categories['Куртки'].id},
        {"name": "Межсезонная куртка", "description": "Модная джинсовая куртка", "price": 4499.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM1UB2J_20977965_3_v1.jpeg",
         "category_id": categories['Куртки'].id},
        {"name": "Ветровка", "description": "Удобная ветровка", "price": 2999.99,
         "photo_url": "https://a.lmcdn.ru/product/M/P/MP002XM00F6E_23108979_3_v1_2x.jpg",
         "category_id": categories['Куртки'].id},
        {"name": "Весенняя куртка", "description": "Легкая весенняя куртка", "price": 3999.99,
         "photo_url": "https://a.lmcdn.ru/product/R/T/RTLADO002101_23618500_3_v1_2x.jpg",
         "category_id": categories['Куртки'].id},

        {"name": "Кроссовки", "description": "Удобные кроссовки для бега", "price": 4999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADL945301_23523976_3_v1.jpg",
         "category_id": categories['Обувь'].id},
        {"name": "Ботинки", "description": "Сланцы", "price": 6499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM1HAF7_13672438_4_v1.jpg",
         "category_id": categories['Обувь'].id},
        {"name": "Туфли", "description": "Классические туфли", "price": 3999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADI082901_22897585_3_v1_2x.jpg",
         "category_id": categories['Обувь'].id},
        {"name": "Сандалии", "description": "Легкие сандалии для лета", "price": 2999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/M/P/MP002XM001FL_22845111_4_v1.jpg",
         "category_id": categories['Обувь'].id},
        {"name": "Спортивная обувь", "description": "Обувь для спортивных тренировок", "price": 5499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADC690501_21763471_3_v2_2x.jpg",
         "category_id": categories['Обувь'].id},

        {"name": "Шапка", "description": "Теплая зимняя шапка", "price": 999.99,
         "photo_url": "https://via.placeholder.com/150",
         "category_id": categories['Аксессуары'].id},
        {"name": "Перчатки", "description": "Кожаные перчатки", "price": 1499.99,
         "photo_url": "https://via.placeholder.com/150",
         "category_id": categories['Аксессуары'].id},
        {"name": "Шарф", "description": "Шерстяной шарф", "price": 1299.99,
         "photo_url": "https://via.placeholder.com/150",
         "category_id": categories['Аксессуары'].id},
        {"name": "Ремень", "description": "Кожаный ремень", "price": 1999.99,
         "photo_url": "https://via.placeholder.com/150",
         "category_id": categories['Аксессуары'].id},
        {"name": "Солнцезащитные очки", "description": "Очки с УФ-защитой", "price": 2499.99,
         "photo_url": "https://via.placeholder.com/150",
         "category_id": categories['Аксессуары'].id},
        {"name": "Часы", "description": "Крутые часы", "price": 29999.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADN729901_23556056_1_v1_2x.jpg",
         "category_id": categories['Аксессуары'].id},
        {"name": "Солнцезащитные очки", "description": "Очки с УФ-защитой", "price": 2499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADJ937901_22853417_1_v1.jpg",
         "category_id": categories['Аксессуары'].id},
        {"name": "Рюкзак", "description": "Кожанный рюкзак", "price": 8299.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLABK458304_22318029_1_v1_2x.jpg",
         "category_id": categories['Аксессуары'].id},
        {"name": "Сумка", "description": "Кожаная сумка", "price": 1499.99,
         "photo_url": "https://a.lmcdn.ru/img600x866/R/T/RTLADJ937901_22853417_1_v1.jpg",
         "category_id": categories['Аксессуары'].id}
    ]

    for data in items_data:
        session.add(Item(**data))

    session.commit()

    # Заполнение базы данных
with SessionLocal() as session:
    add_data(session)