'''
    Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів.
Файл також додайте в репозиторій.
    На екран повинен вивестись список із трьома блоками
- символи з початку, із середини та з кінця файлу.
    Кількість символів в блоках
- та, яка введена в другому параметрі.
    Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі
або, наприклад, файл із двох символів і треба вивести по одному символу,
то що виводити на місці середнього блоку символів?).
Не забудьте додати перевірку чи файл існує.
'''

def read_file(file_path, user_input):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            if len(content) < user_input:
                print('Введено більше символів ніж є у файлі.')

            begin = content[:user_input]
            mid_point = int((len(content) / 2) - (user_input / 2))
            middle = content[mid_point:mid_point + user_input]
            end = content[-user_input:]

            if len(content) == 2:
                print(f'{begin}\n--\n{end}')
            else:
                print(f'{begin}\n{middle}\n{end}')

    except FileNotFoundError as e:
        print(f'{e} файлу не існує.')

file_name = 'text_file.txt'
user_input = int(input('Скільки символів вивести? '))
read_file(file_name, user_input)
