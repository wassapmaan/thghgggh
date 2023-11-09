def count_vowels(line):
    vowels = "аеиоуАЕИОУ"
    return sum(char in vowels for char in line)
def write_to_file(file_path):
    with open(file_path, 'w') as file:
        line_num = 1
        while True:
            line = input(f"Введи строку {line_num} или (или оставь пустую для завершения): ")
            if line.isdigit():
                print("Можно ввести только строку")
                continue
            try:
                number = int(line)
                if number < 0:
                    print("Можно ввести только строку")
                    continue
            except ValueError:
                pass
            if not line:
                break
            file.write(line+'\n')
            line_num +=1

def copy_to_file(source_path, destination_path):
    lines = []
    max_vowels_count = 0
    max_vowels_line_num = 0

    with open(source_path,'r') as source_file:
        for line_num, line in enumerate(source_file, 1):
            vowel_count = count_vowels(line)
            if vowel_count > max_vowels_count:
                max_vowels_count = vowel_count
                max_vowels_line_num = line_num
            else:
                lines.append(line)
    with open(destination_path, 'w') as dest_file:
                dest_file.writelines(lines)
    return max_vowels_line_num

try:
    source_file_path = "F1.txt"
    destination_file_path = "F2.txt"
    write_to_file(source_file_path)
    max_vowels_line_num = copy_to_file(source_file_path, destination_file_path)
    print("Файлы обработаны АХА")
    print(f"Строка с наибольшим колво гласных:{max_vowels_line_num}")
except Exception as e:
    print("Ошибка")
    print(e)

