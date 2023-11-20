'''
Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких файлів.
    Якщо в попередньому завданні ви добре продумали структуру програми то у вас не виникне проблем швидко адаптувати її до нових вимог.
    - на старті додати можливість залогінитися або створити новго користувача
    (при створенні новго користувача, перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
    - в таблиці (базі) з користувачами має бути створений унікальний користувач-інкасатор, який матиме розширені можливості
    (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена. Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти на рахунок лише сумму кратну мінімальному номіналу що підтримує банкомат.
    В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5).
    Але це не має впливати на баланс/кількість купюр банкомату, лише збільшуєтсья баланс користувача
    (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною
    (не вірний логін/пароль, недостатньо коштів на раунку, неможливо видати суму наявними купюрами тощо.)
'''

import sqlite3

def new_user(): # перевіряємо чи існує користувач, якщо ні - створюємо нового.
    while True:
        print('Meню реєстрації.')
        username = input('Введіть новий логін: ')
        password = input('Введіть новий пароль: ')
        if not username or not password:
            print('Логін та пароль повинні бути введені.')
            continue
        with sqlite3.connect('atm_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            check = cursor.fetchone()
            if not check:
                query = 'INSERT INTO users (username, password) VALUES (?, ?)'
                cursor.execute(query, (username, password))
                print('Акаунт створено.')
                break
            else:
                print('Такий користувач вже існує.')

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
        if not username or not password:
            print('Логін та пароль повинні бути введені.')
            continue
        with sqlite3.connect('atm_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
            check = bool(cursor.fetchone())
            if check:
                return username
            else:
                count += 1
                if count == 3:
                    raise PermissionError('доступ заборонено!')
                print('Користувача не існує або не правильний пароль.')
                print(f'Спроб залишилось: {3 - count}')

def user_balance(username):
    """
        Повертаємо баланс юзера в флоат.

            Параметри:
                username (str): Логін користувача

            Повертає:
                balance (int): Сума на рахунку користувача
        """
    with sqlite3.connect('atm_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username, balance FROM users WHERE username = ?', (username,))
        balance = cursor.fetchone()[1]
        return balance

def show_balance(balance):
    """
    Виводимо баланс на екран.

        Параметри:
            balance (float): Сума на рахунку користувача
    """
    print(f'Ваш поточний баланс складає: {balance}$')

def input_check(promt):
    """
    Перевірка вводу користувача на від'ємні значення і коректність даних.

        Параметри:
            promt (str): Унікальний рядок для операцій внесення/зняття коштів.
        Повертає:
            amount (int): Сума кратна 10
            change (float): Решта яка повернеться користувачу.
            user_input (int): Містить номінал або кількість купюр при інкасації.
    """
    while True:
        try:
            user_input = float(input(promt))
            change = user_input % 10 # знаходимо решту
            amount = (user_input // 10) * 10 # сума яку може прийняти/видати банкомат
            if user_input < 0:
                print('Введіть додатню кількість.')
            else:
                return int(amount), round(change, 2), int(user_input)
        except ValueError:
            print('Введено некоректні дані.')

def deposit(username, balance):
    """
    Просимо суму і вносимо її на рахунок. Повертаємо результат операції.

        Параметри:
            username (str): Логін користувача
            balance (int): Сума на рахунку користувача
    """
    with sqlite3.connect('atm_data.db') as conn:
        cursor = conn.cursor()
        promt = 'Введіть суму яку хочете внести: '
        while True:
            amount, change, _ = input_check(promt)
            if amount >= 10:
                balance += amount
                cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (balance, username))

                print(f'Ваш поточний рахунок: {balance}$')
                if change > 0:
                    print(f'Ваша решта: {change}$')
                break
            else:
                print('Банкомат не приймає купюри менше 10.')


def withdraw(username, balance):
    """
    Просимо суму і знімаємо її з рахунку. Повертаємо результат операції.

        Параметри:
                username (str): Логін користувача
                balance (int): Сума на рахунку користувача
    """
    promt = 'Введіть суму яку хочете зняти: '
    bank_balance = atm_balance()
    while True:
        with sqlite3.connect('atm_data.db') as conn:
            cursor = conn.cursor()
            _, _, amount = input_check(promt)
            if amount % 10 != 0:
                print('Введіть число кратне 10.')
            elif amount > bank_balance:
                print(f'Нажаль в банкоматі залишилось тільки {bank_balance}$')
            else:
                if amount <= balance:
                    balance -= amount
                    cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (balance, username))

                    print(f'Ваш поточний рахунок: {balance}$')
                    break
                else:
                    print(f'Нажаль наш банк не дає кредити ;)')

# Admin methods:

def atm_balance():
    with sqlite3.connect('atm_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM atm_balance')
        tuples_list = cursor.fetchall()
        current_balance = sum(i[0] * i[1] for i in tuples_list)
        return current_balance

def show_atm_balance():
    with sqlite3.connect('atm_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM atm_balance')
        current_balance = atm_balance()
        for row in cursor.fetchall():
            print(f'Купюра: {row[0]:<4} - Кількість: {row[1]}')
        print('-' * 28)
        print(f'Поточний баланс банкомату: {current_balance}$')

def atm_update():
    while True:
        nominal_promt = 'Введіть номінал купюри: '
        *_, nominal = input_check(nominal_promt)

        nominals = [10, 20, 50, 100, 200, 500, 1000]
        if nominal in nominals:
            amount_promt = 'Введіть наявну кількість купюр: '
            *_, amount = input_check(amount_promt)

            with sqlite3.connect('atm_data.db') as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE atm_balance SET amount = ? WHERE nominal = ?', (amount, nominal))

            current_balance = atm_balance()
            print(f'Поточний баланс банкомату: {current_balance}$')
            break
        else:
            print('Банкомат не підтримує такий номінал.')

# Start menu:

def admin_menu():
    while True:
        print('1. Перевірити баланс банкомату')
        print('2. Провести інкасацію')
        print('3. Вийти')
        action = input('Будь ласка виберіть дію: ')
        if action == '1':
            show_atm_balance()
            print('')
        elif action == '2':
            atm_update()
            print('')
        elif action == '3':
            print('Бажаємо гарного дня!')
            return
        else:
            print('Введено некоректне значення. Повторіть вибір.')

def user_menu(username):
    while True:
        balance = user_balance(username)
        print('1. Перевірити баланс')
        print('2. Внести кошти')
        print('3. Зняти кошти')
        print('4. Вийти')
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
            print('Бажаємо гарного дня!')
            return
        else:
            print('Введено некоректне значення. Повторіть вибір.')
            print('')

def start():
    while True:
        print('1. Увійти в акаунт')
        print('2. Створити новий акаунт')
        print('3. Вийти')
        check = input('Будь ласка виберіть дію: ')
        if check == '1':
            username = login()
            print('')
            print(f'Вітаємо {username}!')
            if username == 'admin':
                admin_menu()
                return
            else:
                user_menu(username)
                return
        elif check == '2':
            new_user()
        elif check == '3':
            print('Бажаємо гарного дня!')
            return
        else:
            print('Введено некоректне значення, повторіть спробу.')
            print('')


start()