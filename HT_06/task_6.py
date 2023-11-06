'''
Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
Тобто функція приймає два аргументи: список і величину зсуву
(якщо ця величина додатня - пересуваємо з кінця на початок,
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
   fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
   fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
'''


def shift(user_list, steps):

    if steps > len(user_list) or steps < 0:
        steps = steps % len(user_list)

    shifted_list = user_list[-steps:] + user_list[:-steps]

    return shifted_list

user_list = input('Введіть елементи через пробіл: ').split()
steps = int(input('Введіть величину зсуву: '))

result = shift(user_list, steps)

print(f'Ваш список:       {user_list}')
print(f'Посунутий список: {result}')