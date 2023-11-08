'''
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції. Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
P.S. Повинен вертатись генератор.
P.P.S. Для повного розуміння цієї функції -
    можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)).
    Подивіться як веде себе стандартний range в таких випадках.
'''

def my_range(*args):
    if len(args) == 1:
        start, (stop,), step = 0, args, 1
    elif len(args) == 2:
        start, stop = args
        step = 1
    elif len(args) == 3:
        start, stop, step = args
    elif len(args) == 0:
        raise TypeError(f'my_range expected 1 arguments, got 0')
    elif len(args) > 3:
        raise TypeError(f'my_range expected at most 3 arguments, got {len(args)}')

    if not all(isinstance(value, int) for value in (start, stop, step)):
        raise TypeError('one or more arguments cannot be interpreted as an integer')
    else:
        while (start < stop and step > 0) or (start > stop and step < 0):
            yield start
            start += step


for i in my_range(0, 10, 2):
    print(i)