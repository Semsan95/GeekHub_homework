'''
Написати функцію, яка приймає на вхід список (через кому),
підраховує кількість однакових елементів у ньомy і виводить результат.
Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
'''

def counter(elements):
    amount_dict = {}
    for i in elements:
        temp = str(i)
        if temp in amount_dict:
            amount_dict[temp] = amount_dict[temp] + 1
        else:
            amount_dict[temp] = 1

    result = ', '.join([f'{key} -> {value}' for key, value in amount_dict.items()])
    return result

elements = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]

print(counter(elements))