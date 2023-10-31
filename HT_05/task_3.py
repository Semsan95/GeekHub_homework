'''
Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями.
Створiть просту умовну конструкцiю (звiсно вона повинна бути в тiлi ф-цiї),
пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" та у випадку нервіності - виводити ще і різницю.
    Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      вiдповiдь - "х дорiвнює y"
'''
def user_input():
    try:
        x = float(input('Введіть перше число: '))
        y = float(input('Введіть друге число: '))
        return x, y
    except ValueError:
        raise ValueError('Введіть цифру.')


def equalizer():
    x, y = user_input()
    if x > y:
        z = x - y
        return f"{x} бiльше нiж {y}, на {z}"
    elif x < y:
        z = y - x
        return f"{y} бiльше нiж {x}, на {z}"
    else:
        return f"{x} дорiвнює {y}"

print(equalizer())
