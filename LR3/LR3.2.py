# -*- coding: utf-8 -*-
total_cost = 0

try:
    num_items = int(input("введи число товаров:"))

    with open('prices.txt', 'a', encoding='utf-8') as file:
     for i in range(num_items):
         line = input("введи инфу о товаре в виде 'название колво стоимость':")
         elements = line.split()
         if len(elements) == 3:
            name = elements[0]
            quantity = int(elements[1])
            price_per_unit = float(elements[2])
            cost = quantity * price_per_unit
            total_cost += cost
            file.write(f"{name} {quantity} {price_per_unit}\n")
         else:
            print("неккоректный ввод")
            break

     print ("общая стоимость - ", total_cost)

except ValueError:
    print("ошибка преобразования")
except Exception as e:
    print("ошибка", str(e))
