def create_merged_tuple(tuple1, tuple2):

    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        print("Ошибка! Введите кортежи.")
        return None

    merged_tuple = tuple1 + tuple2
    return merged_tuple

input_tuple1 = input("Введите элементы первого кортежа через пробел: ")
tuple1 = tuple(input_tuple1.split())

input_tuple2 = input("Введите элементы второго кортежа через пробел: ")
tuple2 = tuple(input_tuple2.split())

merged_tuple = create_merged_tuple(tuple1, tuple2)

if merged_tuple is not None:
    print("Третий кортеж (объединение):", merged_tuple)
