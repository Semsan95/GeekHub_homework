'''
Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата,
і вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата та його діагональ.
'''

def square(x):
    p = 4 * x
    s = x ** 2
    d = x * (2 ** 0.5)
    return (p, s, d)

print(square(25))
