inventory = []  # Список
doors_opened = set()  # Множества
tasks_completed = set()
levels = {
    1: "Уровень 1: Найти ключ и открыть дверь",
    2: "Уровень 2: Победить монстра",
    3: "Уровень 3: Найти код и открыть сундук с сокровищами",
    4: "Уровень 4: Разгадать загадку старика",
    5: "Уровень 5: Перейти через мост, используя веревку",
    6: "Уровень 6: Открыть финальную дверь с помощью всех собранных ключей"
}
game_items = {
    "ключ": "Старый ключ от двери",
    "меч": "Острый меч для борьбы с врагами",
    "код": "Тайный код для сундука",            # Списки
    "зелье": "Зелье для восстановления сил",
    "веревка": "Веревка для переправы через мост",
    "фамильный ключ": "Древний ключ для финальной двери"
}

def level_1():
    """Первый уровень игры: Найти ключ и открыть дверь."""
    print(levels[1])
    while True:
        action = input("Введите команду (искать, инвентарь, использовать ключ): ").strip().lower()
        if action == "искать":
            if "ключ" not in inventory:
                inventory.append("ключ")
                print("Вы нашли ключ и добавили его в инвентарь.")
            else:
                print("Вы уже нашли ключ.")
        elif action == "инвентарь":
            print("В вашем инвентаре:", inventory)
        elif action == "использовать ключ":
            if "ключ" in inventory:
                doors_opened.add("дверь 1")
                print("Вы открыли дверь и прошли на следующий уровень.")
                break
            else:
                print("У вас нет ключа.")
        else:
            print("Неизвестная команда. Попробуйте снова.")

def level_2():
    """Второй уровень игры: Победить монстра."""
    print(levels[2])
    monster = True
    while True:
        action = input("Введите команду (искать, инвентарь, использовать меч): ").strip().lower()
        if action == "искать":
            if "меч" not in inventory:
                inventory.append("меч")
                print("Вы нашли меч и добавили его в инвентарь.")
            else:
                print("Вы уже нашли меч.")
        elif action == "инвентарь":
            print("В вашем инвентаре:", inventory)
        elif action == "использовать меч":
            if "меч" in inventory:
                if monster:
                    print("Вы победили монстра и прошли на следующий уровень!")
                    tasks_completed.add("победа над монстром")
                    break
                else:
                    print("Монстра больше нет.")
            else:
                print("У вас нет меча.")
        else:
            print("Неизвестная команда. Попробуйте снова.")

def level_3():
    """Третий уровень игры: Найти код и открыть сундук."""
    print(levels[3])
    code_found = False
    while True:
        action = input("Введите команду (искать, инвентарь, использовать код): ").strip().lower()
        if action == "искать":
            if not code_found:
                code_found = True
                inventory.append("код")
                print("Вы нашли код и добавили его в инвентарь.")
            else:
                print("Вы уже нашли код.")
        elif action == "инвентарь":
            print("В вашем инвентаре:", inventory)
        elif action == "использовать код":
            if "код" in inventory:
                print("Вы успешно открыли сундук с сокровищами и нашли фамильный ключ!")
                inventory.append("фамильный ключ")
                tasks_completed.add("открыт сундук")
                break
            else:
                print("У вас нет кода.")
        else:
            print("Неизвестная команда. Попробуйте снова.")

def level_4():
    """Четвертый уровень игры: Разгадать загадку старика."""
    print(levels[4])
    riddle_answer = "тишина"
    while True:
        action = input("Старик задает вам вопрос: 'Я - то, что можно сломать, не касаясь. Что я?' ").strip().lower()
        if action == riddle_answer:
            print("Верно! Вы разгадали загадку и старик пропускает вас дальше.")
            tasks_completed.add("загадка старика")
            break
        else:
            print("Неверно. Попробуйте снова.")

def level_5():
    """Пятый уровень игры: Перейти через мост, используя веревку."""
    print(levels[5])
    while True:
        action = input("Введите команду (искать, инвентарь, использовать веревку): ").strip().lower()
        if action == "искать":
            if "веревка" not in inventory:
                inventory.append("веревка")
                print("Вы нашли веревку и добавили ее в инвентарь.")
            else:
                print("Вы уже нашли веревку.")
        elif action == "инвентарь":
            print("В вашем инвентаре:", inventory)
        elif action == "использовать веревку":
            if "веревка" in inventory:
                print("Вы использовали веревку и успешно пересекли мост.")
                tasks_completed.add("пересечен мост")
                break
            else:
                print("У вас нет веревки.")
        else:
            print("Неизвестная команда. Попробуйте снова.")

def level_6():
    """Шестой уровень игры: Открыть финальную дверь с помощью всех ключей."""
    print(levels[6])
    while True:
        action = input("Введите команду (инвентарь, использовать фамильный ключ): ").strip().lower()
        if action == "инвентарь":
            print("В вашем инвентаре:", inventory)
        elif action == "использовать фамильный ключ":
            if "фамильный ключ" in inventory and "ключ" in inventory:
                print("Вы использовали все ключи и открыли финальную дверь. Поздравляем, вы прошли игру!")
                break
            else:
                print("У вас не хватает ключей.")
        else:
            print("Неизвестная команда. Попробуйте снова.")

def start_game():
    print("Добро пожаловать в игру-квест 'Замок загадок'!")
    print("Ваша цель - пройти все шесть уровней и раскрыть тайны замка.")
    current_level = 1

    while current_level <= 6:
        if current_level == 1:
            level_1()
        elif current_level == 2:
            level_2()
        elif current_level == 3:
            level_3()
        elif current_level == 4:
            level_4()
        elif current_level == 5:
            level_5()
        elif current_level == 6:
            level_6()
        current_level += 1

    print("Игра окончена. Спасибо за игру!")

start_game()