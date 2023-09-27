def create_char_count_dict(string):
    if not isinstance(string, str):
        print("Ошибка! Введена неправильная строка.")
        return None

    char_count_dict = {}
    for char in string:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1

    return char_count_dict

input_string = input("Введи строку: ")
result_dict = create_char_count_dict(input_string)

if result_dict is not None:
    print("Результат:")
    for key, value in result_dict.items():
        print(f"{key}: {value}")