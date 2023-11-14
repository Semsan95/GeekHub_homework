'''
Програма-банкомат.
   Використувуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних
      (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль).
      Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій
'''
import csv
import json

def login():
    """
    Перевіряємо чи користувач існує, якщо не існує то видаємо помилку

        Повертає:
            username (str): Логін користувача
    """
    count = 0
    while count < 3:
        username = input('Введіть логін: ')
        password = input('Введіть пароль: ')
        with open('users.csv', 'r') as users_dict:
            reader = csv.DictReader(users_dict)
            user_found = False
            for row in reader:
                if username == row['username'] and password == row['password']:
                    user_found = True
                    break
            if user_found:
                return username
            else:
                count += 1
                if count == 3:
                    raise PermissionError('доступ заборонено!')
                print('Користувача не існує або не правильний пароль.')
                print(f'Спроб залишилось: {3 - count}')


def current_balance(username):
    """
    Повертаємо баланс юзера в флоат. Якщо балансу не існує - повертаємо 0.0

        Параметри:
            username (str): Логін користувача

        Повертає:
            balance (float): Сума на рахунку користувача
    """
    with open(f'users_balance/{username}.txt', 'r') as user_balance:
        user_balance.seek(0)
        balance = user_balance.read()
        if not balance:
            balance = 0.0
        else:
            balance = float(balance)
        return balance


def show_balance(balance):
    """
    Виводимо баланс на екран.

        Параметри:
            balance (float): Сума на рахунку користувача
    """
    print(f'Ваш поточний баланс складає: {round(balance, 2)}$')


def deposit(username, balance):
    """
    Просимо суму і вносимо її на рахунок. Повертаємо результат операції.

        Параметри:
            username (str): Логін користувача
            balance (float): Сума на рахунку користувача
    """
    with open(f'users_balance/{username}.txt', 'w') as user_balance:
        promt = 'Введіть суму яку хочете внести: '
        amount = input_check(promt)
        balance += amount
        user_balance.write(str(balance))

        transaction = f'Внесено на рахунок: {amount}$'
        history_dump(username, transaction)

        print(f'Ваш поточний рахунок: {round(balance, 2)}$')


def withdraw(username, balance):
    """
    Просимо суму і знімаємо її з рахунку. Повертаємо результат операції.

        Параметри:
                username (str): Логін користувача
                balance (float): Сума на рахунку користувача
    """
    promt = 'Введіть суму яку хочете зняти: '
    while True:
        with open(f'users_balance/{username}.txt', 'w') as user_balance:
            amount = input_check(promt)
            if amount < balance:
                balance -= amount
                user_balance.write(str(balance))

                transaction = f'Знято з рахунку: {amount}$'
                history_dump(username, transaction)

                print(f'Ваш поточний рахунок: {round(balance, 2)}$')
                break
            else:
                print(f'Нажаль наш банк не дає кредити ;)')


def history_load(username):
    """
    Виводимо на екран історію всіх транзакцій.

        Параметри:
            username (str): Логін користувача
    """
    user_history = []
    with open(f'users_transactions/{username}.json', 'r') as file:
        for line in file:
            transaction = json.loads(line)
            user_history.append(transaction)
    for i in user_history:
        print(i)


def history_dump(username, transaction):
    """
    Вносимо інфу про транзакцію в {username}.json.

        Параметри:
            username (str): Логін користувача
            transaction (str): Сума яку було знято, або внесено на рахунок.
    """
    with open(f'users_transactions/{username}.json', 'a') as file:
        if file.tell() > 0:
            file.write('\n')
        json.dump(transaction, file)


def input_check(promt):
    """
    Перевірка вводу користувача на від'ємні значення і коректність даних.

        Параметри:
            promt (str): Унікальний рядок для операцій внесення/зняття коштів.
    """
    while True:
        try:
            amount = float(input(promt))
            if amount < 0:
                print('Введіть додатню суму.')
            else:
                return amount
        except ValueError:
            print('Введено некоректні дані.')


def start():
    print('Увійдіть у свій акаунт.')
    username = login()
    print(f'Вітаємо {username}!')
    while True:
        balance = current_balance(username)
        print('1. Перевірити баланс')
        print('2. Внести кошти')
        print('3. Зняти кошти')
        print('4. Історія транзакцій')
        print('5. Вийти')
        action = input('Будь ласка виберіть дію: ')
        if action == '1':
            show_balance(balance)
            print('')
        elif action == '2':
            deposit(username, balance)
            print('')
        elif action == '3':
            withdraw(username, balance)
            print('')
        elif action == '4':
            history_load(username)
            print('')
        elif action == '5':
            print('Бажаємо гарного дня!')
            return
        else:
            print('Введено некоректне значення. Повторіть вибір.')


start()












