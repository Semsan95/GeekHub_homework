'''
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
'''

#Req - requirements
class LoginReq(Exception):
    pass

users = [
        ('Andy', 'A12345678'),
        ('Bill', 'B23456781'),
        ('Carl', 'C34567812'),
        ('Dean', 'D45678123'),
        ('Eric', 'E56781234')
    ]

def log_valid(username, password):
    if len(username) < 3 or len(username) > 50:
        raise LoginReq('Не вірна довжина логіну.')

    if 8 > len(password) or password.isalpha():
        raise LoginReq('Пароль закороткий або не містить цифр.')

    if any([user[0] == username for user in users]):
        raise LoginReq('Такий користувач вже існує.')

    return username, password


username = input('Введіть логін: ')
password = input('Введіть пароль: ')
result = log_valid(username, password)

print(result)

