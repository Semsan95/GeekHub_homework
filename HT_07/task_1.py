'''
Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено коректну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція вертає False
        якщо silent == False -породжується виключення LoginException (його також треба створити =))
'''


class LoginException(Exception):
    pass


def login(username, password, silent=False):
    users = [
        ('Andy', '123'),
        ('Bill', '1234'),
        ('Carl', '12345'),
        ('Dean', '123456'),
        ('Eric', '1234567')
    ]
    check = (username, password)

    if check in users:
        return True
    else:
        if silent:
            return False
        else:
            raise LoginException('Неправильний логін або пароль!')


username = input('Введіть ваш логін: ')
password = input('Введіть ваш пароль: ')

result = login(username, password, silent=False)

print(result)
