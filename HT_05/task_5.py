'''
Ну і традиційно - калькулятор!
Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2).
Операції що мають бути присутні: +, -, *, /, %, //, **.
Не забудьте протестувати з різними значеннями на предмет помилок!
'''

def user_input(num1, num2):
        try:
            x = float(num1)
            y = float(num2)
            return x, y
        except ValueError:
            raise ValueError('Не вірний формат вводу.')

def calc(num1, num2, operator):
    try:
        x, y = user_input(num1, num2)
        if operator == '+':
            return x + y
        elif operator == '-':
            return x - y
        elif operator == '*':
            return x * y
        elif operator == '**':
            return x ** y
        elif operator == '/' or operator == ':':
            return x / y
        elif operator == '%':
            return x % y
        elif operator == '//':
            return x // y
        else:
            return 'Ви ввели неіснуючу операцію.'
    except ZeroDivisionError:
        return 'На нуль ділити не можна.'

num1, operator, num2 = input('Введіть бажану операцію: ').split()

print(calc(num1, num2, operator))
