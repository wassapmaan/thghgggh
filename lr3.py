def find_smallest_even_element(lst):
    if not isinstance(lst, list):
        print("Ошибка! Введите список.")
        return None

    even_elements = [num for num in lst if num % 2 == 0]
    if even_elements:
        smallest_even = min(even_elements)
        return smallest_even
    else:
        return lst[0]

def move_zeros_to_front(lst):
    if not isinstance(lst, list):
        print("Ошибка! Введите список.")
        return None

    # Перемещаем нулевые элементы в начало списка
    zero_elements = [num for num in lst if num == 0]
    non_zero_elements = [num for num in lst if num != 0]
    new_list = zero_elements + non_zero_elements

    return new_list

input_list = input("Введите список элементов через пробел: ")
lst = [int(num) for num in input_list.split()]  # Преобразование строк в целые числа

smallest_even = find_smallest_even_element(lst)
print("Наименьший четный элемент:", smallest_even)

new_list = move_zeros_to_front(lst)
print("Список с нулями в начале:", new_list)
