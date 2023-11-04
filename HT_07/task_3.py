'''
На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів
   (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу(списку?) і, користуючись валідатором,
   перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
'''

class LoginReq(Exception):
    pass

users = [
        ('Andy', 'A12345678'),
        ('Bi', 'B23456781'),
        ('Carl', 'C3456'),
        ('Dean', 'DAsnajANJns'),
        ('Eric', 'qwerty12')
    ]

def log_valid(username, password):
    if len(username) < 3 or len(username) > 50:
        raise LoginReq('Не вірна довжина логіну.')

    if len(password) < 8 or password.isalpha():
        raise LoginReq('Пароль закороткий або не містить цифр.')

    #if any([user[0] == username for user in users]): - закоментував бо при такій перевірці
        #raise LoginReq('Такий користувач вже існує.')  всі наявні акаунти видадуть помилку в <status>.

    if 'qwerty' in password and len(password) < 10:
        raise LoginReq('Пароль занадто простий.')

    return 'OK'


for username, password in users:
    print(f'Name: {username}')
    print(f'Password: {password}')
    try:
        result = log_valid(username, password)
        print(f'Status: OK \n-----')
    except LoginReq as e:
        print(f'Status: {e} \n-----')
