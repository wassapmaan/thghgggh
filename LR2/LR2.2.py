def process_data(data):
    if isinstance(data, set):
        return sum(data)
    elif isinstance(data, list):
        negatives = [num for num in data if num < 0]
        if len(negatives) >= 2:
            product = negatives[0] * negatives[1]
            data[data.index(negatives[0])] = negatives[1]
            data[data.index(negatives[1])] = negatives[0]
            return product, data
        else:
            return "Не хватает отрицательных чисел в списке!"
    elif isinstance(data, int):
        return sum(int(digit) for digit in str(data))
    elif isinstance(data, str):
        words = data.split()
        longest_word = max(words, key=len)
        return longest_word
    else:
        return "Плохой тип данных!"
def get_user_input():
    while True:
        data_type = input("Введите тип данных (set, list, int, str): ")
        if data_type not in ["set", "list", "int", "str"]:
            print("Плохой тип данных!")
            continue

        data = input("Введите данные: ")
        try:
            if data_type == "set":
                data = set(map(float, data.split()))
            elif data_type == "list":
                data = list(map(float, data.split()))
            elif data_type == "int":
                data = int(data)
            elif data_type == "str":
                data = str(data)
            break
        except ValueError:
            print("введи корректные значения.")

    return data

data = get_user_input()
result = process_data(data)
print(result)