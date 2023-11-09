import re

def create_subjects_file(file_path):
    content = '''"Информатика": 100(л) 50(пр) 20(лаб) , "Физика": 30(л) 10(лаб) , "Физкультура": 30(пр)'''

    with open(file_path,'w') as file:
        file.write(content)

def create_subjects_dictionary(file_path):
    subjects_dict = {}

    try:
         with open(file_path,'r') as file:
           for line in file:
               line = line.strip()
               if line:
                  subject_info = line.split(":")
                  if len(subject_info) == 2:
                      subject = subject_info[0].strip()
                      lessons = subject_info[1].split()

                      total_lessons = 0
                      for lesson in lessons:
                          match = re.search(r'(\d+)\((.*?)\)', lesson)
                          if match:
                             quantity = int(match.group(1))
                             lesson_type = match.group(2)
                             if lesson_type in ['л','пр','лаб']:
                                total_lessons += quantity
                          elif lesson.isdigit():
                               total_lessons += int(lesson)

                               subjects_dict[subject] = total_lessons

         return subjects_dict
    except FileNotFoundError:
            print(f"файл '{file_path}' не найден")
    except Exception as e:
            print(f"ошибка чтения файла '{file_path}':")
            print (e)
            return None

file_path = "subjects.txt"
create_subjects_file(file_path)

subjects_dict = create_subjects_dictionary(file_path)
if subjects_dict is not None:
     print("Словарь")
for subject, total_lessons in subjects_dict.items():
     print(f"{subject}: {total_lessons}")
