'''
Ну і традиційно - калькулятор!
Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі разом - типу 1 + 2).
Операції що мають бути присутні: +, -, *, /, %, //, **.
Не забудьте протестувати з різними значеннями на предмет помилок!
'''

def cal(num1: int, operator: str, num2: int):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '/' and num2 != 0:
        return num1 / num2
    elif operator == '%' and num2 != 0:
        return num1 % num2
    elif operator == '//' and num2 != 0:
        return num1 // num2
    else:
        return 'Невірний ввід даних. Повторіть.'

print(cal(1, '+', 0))