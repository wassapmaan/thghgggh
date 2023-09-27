toys = {
    "Мяч": ["Красный мяч", 10.99, 5],
    "Кукла": ["Розовая кукла", 15.99, 3],
    "Конструктор": ["Деревянный конструктор", 19.99, 7],
    "Пазл": ["10000000 элементов", 12.99, 10],
    "Машинка": ["Быстрая машинка", 9.99, 8],
    "Плюшевый мишка": ["Злой и пушистый", 14.99, 4]
}
def display_description():
    toy_name = input("Введи название игрушки: ")
    if toy_name in toys:
        description = toys[toy_name][0]
        print(f"Описание: {description}")
    else:
        print("Такой игрушки нет в магазине.")

def display_price():
    toy_name = input("Введи название игрушки: ")
    if toy_name in toys:
        price = toys[toy_name][1]
        print(f"Цена: {price} руб.")
    else:
        print("Такой игрушки нет в магазине.")

def display_quantity():
    toy_name = input("Введи название игрушки: ")
    if toy_name in toys:
        quantity = toys[toy_name][2]
        print(f"Количество: {quantity} шт.")
    else:
        print("Такой игрушки нет в магазине.")

def display_all():
    print("Информация о всех игрушках в магазине:")
    for toy_name, details in toys.items():
        description = details[0]
        price = details[1]
        quantity = details[2]
        print(f"Название: {toy_name}")
        print(f"Описание: {description}")
        print(f"Цена: {price} руб.")
        print(f"Количество: {quantity} шт.")
        print()

def purchase():
    total_price = 0
    while True:
        toy_name = input("Введи название игрушки (или 'FF' для выхода): ")
        if toy_name == 'FF':
            break
        elif toy_name not in toys:
            print("Такой игрушки нет в магазине.")
            continue
        quantity = int(input("Введи количество: "))
        if quantity > toys[toy_name][2]:
            print("Недостаточное количество товара.")
            continue
        price = toys[toy_name][1]
        total_price += price * quantity
        toys[toy_name][2] -= quantity
        print(f"Вы приобрели {quantity} шт. игрушки '{toy_name}'.")

    print(f"Сумма покупки: {total_price} руб.")
    print("Остаток товара в магазине:")
    display_all()

def main():
    while True:
        print("Меню:")
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Вся информация")
        print("5. Покупка")
        print("6. Выход")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            display_description()
        elif choice == '2':
            display_price()
        elif choice == '3':
            display_quantity()
        elif choice == '4':
            display_all()
        elif choice == '5':
            purchase()
        elif choice == '6':
            print("!!!!!!ВсЕгО ХоРоШеГо!!!!!!!")
            break
        else:
            print("Фигня. Давай снова.")

if __name__ == "__main__":
    main()
