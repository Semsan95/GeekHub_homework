'''
Написати скрипт, який приймає від користувача два числа (int або float) і робить наступне:
    a. Кожне введене значення спочатку пробує перевести в int.
       У разі помилки - пробує перевести в float, а якщо і там ловить помилку - пропонує ввести значення ще раз
       (зручніше на даному етапі навчання для цього використати цикл while)
    b. Виводить результат ділення першого на друге.
       Якщо при цьому виникає помилка - оброблює її і виводить відповідне повідомлення
'''

while True:
    try:
        first_num = input('Enter first number: ')
        second_num = input('Enter second number: ')
        a = int(first_num)
        b = int(second_num)
    except:
        try:
            a = float(first_num)
            b = float(second_num)
        except:
            print('Please enter numbers again.')
        else:
            break
    else:
        break
try:
    print(f'{a} / {b} = {a / b}')
except Exception as e:
    print('Exception:', e)