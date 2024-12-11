import datetime

# Данные пользователей
users = [
    {'username': 'admin', 'password': 'admin', 'role': 'admin'},
    {'username': 'john_doe', 'password': '1234', 'role': 'user', 'history': [], 'created_at': '2024-12-01'}
]

# Данные услуг
services = [
    {'id': 1, 'name': 'Тур в Париж', 'price': 1000, 'rating': 4.5, 'added_date': '2024-12-01'},
    {'id': 2, 'name': 'Тур в Рим', 'price': 800, 'rating': 4.0, 'added_date': '2024-11-25'}
]

def authenticate():
    username = input("Логин: ")
    password = input("Пароль: ")
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    print("Неверный логин или пароль.")
    return None

def user_menu(user):
    while True:
        print("\nМеню пользователя:")
        print("1. Просмотреть доступные туры")
        print("2. Найти тур")
        print("3. Сортировать туры по цене или рейтингу")
        print("4. Купить тур")
        print("5. Посмотреть историю покупок")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            view_services()
        elif choice == "2":
            search_service()
        elif choice == "3":
            sort_services()
        elif choice == "4":
            buy_service(user)
        elif choice == "5":
            view_history(user)
        elif choice == "6":
            break
        else:
            print("Неверный выбор.")

def admin_menu():
    while True:
        print("\nМеню администратора:")
        print("1. Просмотреть доступные туры")
        print("2. Добавить тур")
        print("3. Удалить тур")
        print("4. Изменить данные о туре")
        print("5. Управление пользователями")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            view_services()
        elif choice == "2":
            add_service()
        elif choice == "3":
            delete_service()
        elif choice == "4":
            edit_service()
        elif choice == "5":
            manage_users()
        elif choice == "6":
            break
        else:
            print("Неверный выбор.")

def view_services():
    print("\nДоступные туры:")
    for service in services:
        print(
            f"ID: {service['id']}, Название: {service['name']}, Цена: {service['price']}, Рейтинг: {service['rating']}")


def search_service():
    query = input("Введите название тура для поиска: ").lower()
    results = filter(lambda s: query in s['name'].lower(), services)
    results = list(results)
    if results:
        for service in results:
            print(
                f"ID: {service['id']}, Название: {service['name']}, Цена: {service['price']}, Рейтинг: {service['rating']}")
    else:
        print("Туры не найдены.")


def sort_services():
    criterion = input("Сортировать по (цена/рейтинг): ").lower()
    if criterion == "цена":
        sorted_services = sorted(services, key=lambda s: s['price'])
    elif criterion == "рейтинг":
        sorted_services = sorted(services, key=lambda s: s['rating'], reverse=True)
    else:
        print("Неверный критерий.")
        return
    for service in sorted_services:
        print(
            f"ID: {service['id']}, Название: {service['name']}, Цена: {service['price']}, Рейтинг: {service['rating']}")


def buy_service(user):
    view_services()
    service_id = int(input("Введите ID тура для покупки: "))
    for service in services:
        if service['id'] == service_id:
            user.setdefault('history', []).append(service['name'])
            print(f"Вы купили тур: {service['name']}")
            return
    print("Тур не найден.")


def view_history(user):
    print("\nВаша история покупок:")
    for item in user.get('history', []):
        print(item)


# Административные функции
def add_service():
    name = input("Название тура: ")
    price = float(input("Цена: "))
    rating = float(input("Рейтинг: "))
    new_service = {
        'id': max(s['id'] for s in services) + 1,
        'name': name,
        'price': price,
        'rating': rating,
        'added_date': datetime.date.today().isoformat()
    }
    services.append(new_service)
    print("Тур добавлен.")


def delete_service():
    view_services()
    service_id = int(input("Введите ID тура для удаления: "))
    global services
    services = [s for s in services if s['id'] != service_id]
    print("Тур удален.")


def edit_service():
    view_services()
    service_id = int(input("Введите ID тура для редактирования: "))
    for service in services:
        if service['id'] == service_id:
            service['name'] = input("Новое название: ")
            service['price'] = float(input("Новая цена: "))
            service['rating'] = float(input("Новый рейтинг: "))
            print("Тур обновлен.")
            return
    print("Тур не найден.")


def manage_users():
    global users
    print("\nСписок пользователей:")
    for user in users:
        print(f"Логин: {user['username']}, Роль: {user['role']}")
    action = input("Добавить/удалить пользователя (д/у)? ").lower()
    if action == "д":
        username = input("Логин: ")
        password = input("Пароль: ")
        role = input("Роль (admin/user): ")
        users.append({'username': username, 'password': password, 'role': role})
        print("Пользователь добавлен.")
    elif action == "у":
        username = input("Логин пользователя для удаления: ")
        users = [u for u in users if u['username'] != username]
        print("Пользователь удален.")
    else:
        print("Неверный выбор.")


# Основной цикл
def main():
    print("Добро пожаловать в туристическое агентство!")
    user = None
    while not user:
        user = authenticate()

    if user['role'] == 'user':
        user_menu(user)
    elif user['role'] == 'admin':
        admin_menu()


if __name__ == "__main__":
    main()