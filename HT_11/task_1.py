'''
1. Створити клас Calc, який буде мати атребут last_result та 4 методи.
Методи повинні виконувати математичні операції з 2-ма числами, а саме:
додавання, віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися до атребута last_result
він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повенен повернути результат виконання
ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
    ...
- Додати документування в клас.
'''

class Calc:
    """
    Клас для виконання математичних операцій з 2-ма числами.

    Атрибути:
        last_result (float or None): Зберігає результат останньої операції.
        temp_result (float or None): Проміжна змінна між resut i last_result.

    Методи:
        addition(x, y): Додає x до y.
        subtraction(x, y): Віднімає y від x.
        multiplication(x, y): Множить x на y.
        division(x, y): Ділить x на y.
    """


    def __init__(self):
        self.last_result = None
        self.temp_result = None

    def addition(self, x, y):
        """Додає x до y."""
        result = x + y
        self.buffer(result)
        return result

    def subtraction(self, x, y):
        """Віднімає y від x."""
        result = x - y
        self.buffer(result)
        return result

    def multiplication(self, x, y):
        """Множить x на y."""
        result = x * y
        self.buffer(result)
        return result

    def division(self, x, y):
        """Ділить x на y."""
        result = x / y
        self.buffer(result)
        return result

    def buffer(self, result):
        """Зберігає поточний результат у temp_result, а попередній у last_result."""
        self.last_result = self.temp_result
        self.temp_result = result


calc = Calc()
print(f'Останній результат: {calc.last_result}')
print(f'Результат додавання: {calc.addition(1, 1)}')

print(f'Останній результат: {calc.last_result}')
print(f'Результат множення: {calc.multiplication(2, 3)}')

print(f'Останній результат: {calc.last_result}')
print(f'Результат множення: {calc.multiplication(3, 4)}')

print(f'Останній результат: {calc.last_result}')
