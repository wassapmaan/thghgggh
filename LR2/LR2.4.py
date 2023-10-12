def divide_numbers(k, l):
    try:
        result = k / l
        print("результат деления:", result)
    except ZeroDivisionError:
        print("делить на ноль нельзя!")
    finally:
        print("конец программы!!!!")

def get_user_input():
    while True:
        try:
            k = float(input("введите делимое число: "))
            l = float(input("введите делитель: "))
            break
        except ValueError:
            print("ошибка, нужно ввести числа.")

    return k, l

k, l = get_user_input()
divide_numbers(k, l)