def bank():
    while True:
        try:
            a = float(input("Введите размер вклада: "))
            years = int(input("Введите срок вклада (в годах): "))

            if a <= 0 or years <= 0:
                print("Фигня! Вклад и срок вклада должны быть числами > 0.")
            else:
                break
        except ValueError:
            print("Полная фигня! Введите числовые значения.")
    total = a
    for _ in range(years):
        total += total * 0.1  # 10%
    return total
result = bank()
print(f"Сумма на счету: {result} рублей")