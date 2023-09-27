def remove_text_in_brackets(text):

    if not isinstance(text, str):
        print("Ошибка! Введите строку.")
        return None

    import re
    pattern = r'\([^)]*\)'  # Шаблон для поиска текста в скобках
    result = re.sub(pattern, '', text)

    return result

input_text = input("Введите строку с текстом: ")
result_text = remove_text_in_brackets(input_text)

if result_text is not None:
    print("Результат:", result_text)
