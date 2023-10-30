'''
Наприклад маємо рядок -->
"f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345"
 -> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)
'''

def cat_paws(long_string):
    """Please put your cat on the keyboard"""

    letters = [i for i in long_string if i.isalpha()]
    numbers = [int(i) for i in long_string if i.isdigit()]

    if 29 < len(long_string) < 51:
        print(f'Довжина рядка: {len(long_string)} \nКількість букв: {len(letters)} \nКількість цифр: {len(numbers)}')
    elif len(long_string) < 30:
        print(f"Сума всіх чисел: {sum(numbers)} \n{''.join(letters)}")
    else:
        print(f'Кількість унікальних символів: {len(set(long_string))}')


cat_paws("f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345")



