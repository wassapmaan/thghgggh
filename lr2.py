def remove_text_in_brackets(text):
    # Проверяем, что введенное значение является строкой
    if not isinstance(text, str):
        print("Ошибка! Введите строку.")
        return None

    # Используем регулярное выражение для поиска текста в скобках
    import re
    pattern = r'\([^)]*\)'  # Шаблон для поиска текста в скобках
    result = re.sub(pattern, '', text)  # Удаляем текст в скобках

    return result


# Пример использования
input_text = input("Введите строку с текстом: ")
result_text = remove_text_in_brackets(input_text)

if result_text is not None:
    print("Результат:", result_text)
