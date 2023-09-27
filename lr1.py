number = input("Введи натуральное число: ")
if not number.isdigit():
    print("Ошибка! Введи натуральное число.")
    exit()
max_digit = 0
for digit in number:
    digit = int(digit)
    if digit > max_digit:
        max_digit = digit
print("Максимальная цифра в числе:", max_digit)
