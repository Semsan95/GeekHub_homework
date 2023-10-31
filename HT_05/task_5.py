'''
Ну і традиційно - калькулятор!
Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2).
Операції що мають бути присутні: +, -, *, /, %, //, **.
Не забудьте протестувати з різними значеннями на предмет помилок!
'''

def user_input():
    while True:
        try:
            num1, operator, num2 = input('Введіть бажану операцію: ').split()
            num1 = float(num1)
            num2 = float(num2)
            return num1, operator, num2
        except ValueError as e:
            print(f'Помилка: {e}. Не вірний формат вводу.')

def calc():
    try:
        num1, operator, num2 = user_input()
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '**':
            return num1 ** num2
        elif operator == '/' or operator == ':':
            return num1 / num2
        elif operator == '%':
            return num1 % num2
        elif operator == '//':
            return num1 // num2
        else:
            return 'Ви ввели неіснуючу операцію.'
    except ZeroDivisionError:
        return 'На нуль ділити не можна.'


print(calc())
