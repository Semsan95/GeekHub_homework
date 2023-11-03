'''
Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
'''


def fibonacci(number):
    x = 0
    y = 1
    z = 0
    my_list = []
    while z < number:
        my_list.append(x)
        z = x + y
        x, y = y, z
    my_list.append(x)

    return my_list


number = int(input('Enter number: '))

print(f'All fibonacci numbers:', *fibonacci(number))
