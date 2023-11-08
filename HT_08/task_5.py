'''
Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих регістро-незалежних букв та цифр,
які зустрічаються в рядку більше ніж 1 раз. Рядок буде складатися лише з цифр та букв (великих і малих).
Реалізуйте обчислення за допомогою генератора.
    Example (input string -> result):
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі
'''

def str_counter(str_input):
    low_str = str_input.lower()
    x = {i: 1 for i in low_str if low_str.count(i) > 1}
    return len(x)

str_input = input('Введіть ваш рядок: ')
result = str_counter(str_input)

print(result)