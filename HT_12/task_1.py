import sqlite3
import random

class User:

    def __init__(self):
        pass

    @staticmethod
    def random_bonus():
        # З шансом 10% зараховує 50$ новому користувачу.
        chance = 10
        result = random.randint(0, 99)
        if chance > result:
            return True

    @staticmethod
    def new_user():
        # Перевіряємо чи існує користувач, якщо ні - створюємо нового.
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
                    if User.random_bonus():
                        balance = 50
                        cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (balance, username))
                        print(f'Вітаємо, ви отримали бонус: {balance}$')
                    break
                else:
                    print('Такий користувач вже існує.')

    @staticmethod
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

    def user_balance(self, username):
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

    def show_balance(self, balance):
        """
        Виводимо баланс на екран.

            Параметри:
                balance (float): Сума на рахунку користувача
        """
        print(f'Ваш поточний баланс складає: {balance}$')

    def input_check(self, promt):
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
                change = user_input % 10  # знаходимо решту
                amount = (user_input // 10) * 10  # сума яку може прийняти/видати банкомат
                if user_input < 0:
                    print('Введіть додатню кількість.')
                else:
                    return int(amount), round(change, 2), int(user_input)
            except ValueError:
                print('Введено некоректні дані.')

    def deposit(self, username, balance):
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
                amount, change, _ = self.input_check(promt)
                if amount >= 10:
                    balance += amount
                    cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (balance, username))

                    print(f'Ваш поточний рахунок: {balance}$')
                    if change > 0:
                        print(f'Ваша решта: {change}$')
                    break
                else:
                    print('Банкомат не приймає купюри менше 10.')

    def withdraw(self, username, balance):
        """
        Просимо суму і знімаємо її з рахунку. Повертаємо результат операції.

            Параметри:
                    username (str): Логін користувача
                    balance (int): Сума на рахунку користувача
        """
        promt = 'Введіть суму яку хочете зняти: '
        bank_balance = ATM.atm_balance()
        while True:
            _, _, amount = self.input_check(promt)
            if amount % 10 != 0:
                print('Введіть число кратне 10.')
            elif amount > bank_balance:
                print(f'Нажаль в банкоматі залишилось тільки {bank_balance}$')
            else:
                if amount <= balance:
                    ATM.atm_withdraw(amount, balance, username)
                    break
                else:
                    print(f'Нажаль наш банк не дає кредити ;)')

    def user_menu(self, username):
        while True:
            balance = self.user_balance(username)
            print('1. Перевірити баланс')
            print('2. Внести кошти')
            print('3. Зняти кошти')
            print('4. Вийти')
            action = input('Будь ласка виберіть дію: ')
            if action == '1':
                self.show_balance(balance)
                print('')
            elif action == '2':
                self.deposit(username, balance)
                print('')
            elif action == '3':
                self.withdraw(username, balance)
                print('')
            elif action == '4':
                print('Бажаємо гарного дня!')
                return
            else:
                print('Введено некоректне значення. Повторіть вибір.')
                print('')

class ATM:

    @staticmethod
    def atm_withdraw(amount, balance, username):
        nominals_amount = ATM.atm_nominal_amount()
        with sqlite3.connect('atm_data.db') as conn:
            cursor = conn.cursor()
            pay_comb = ATM.atm_nominals_check(amount, nominals_amount)
            if pay_comb is not None:
                for i in set(pay_comb):
                    cursor.execute('''
                    UPDATE atm_balance 
                    SET amount = amount - ? 
                    WHERE nominal = ?
                    ''',(pay_comb.count(i), i))
                print('Ваші купюри:')
                for i in sorted(set(pay_comb), reverse=True):
                    print(f'{i}$, {pay_comb.count(i)} шт.')
                balance -= amount
                cursor.execute('UPDATE users SET balance = ? WHERE username = ?', (balance, username))
                print(f'Ваш поточний рахунок: {balance}$')
            else:
                nominals = [key for key, nominal in nominals_amount.items() if nominal != 0]
                print('Нажаль в банкоматі закінчились необхідні номінали.')
                print(f'Доступні номінали: {", ".join(map(str, nominals))}')

    @staticmethod
    def atm_nominals_check(amount, balance, combination=[]): # Повертає список з комбінацією номіналів, які треба видати.
        comb_sum = sum(combination)
        if comb_sum == amount:
            return combination
        if comb_sum > amount:
            return None
        for key in balance:
            if balance[key] > combination.count(key):
                result = ATM.atm_nominals_check(amount, balance, combination + [key])
                if result is not None:
                    return result
        return None

    @staticmethod
    def atm_nominal_amount(): # Повертає з бази АТМ, словник {номінал: кількість}, посортований по спаданню.
        with sqlite3.connect('atm_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM atm_balance')
            tuples_list = cursor.fetchall()
            current_balance = {i[0]: i[1] for i in tuples_list}
            return dict(sorted(current_balance.items(), reverse=True))

    @staticmethod
    def atm_balance(): # Повертає загальний баланс банкомату.
        with sqlite3.connect('atm_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM atm_balance')
            tuples_list = cursor.fetchall()
            current_balance = sum(i[0] * i[1] for i in tuples_list)
            return current_balance

    @staticmethod
    def show_atm_balance():
        with sqlite3.connect('atm_data.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM atm_balance')
            current_balance = ATM.atm_balance()
            for row in cursor.fetchall():
                print(f'Купюра: {row[0]:<4} - Кількість: {row[1]}')
            print('-' * 28)
            print(f'Поточний баланс банкомату: {current_balance}$')

    @staticmethod
    def atm_update():
        while True:
            user_instance = User()
            nominal_promt = 'Введіть номінал купюри: '
            *_, nominal = user_instance.input_check(nominal_promt)

            nominals = [10, 20, 50, 100, 200, 500, 1000]
            if nominal in nominals:
                amount_promt = 'Введіть наявну кількість купюр: '
                *_, amount = user_instance.input_check(amount_promt)

                with sqlite3.connect('atm_data.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('UPDATE atm_balance SET amount = ? WHERE nominal = ?', (amount, nominal))

                current_balance = ATM.atm_balance()
                print(f'Поточний баланс банкомату: {current_balance}$')
                break
            else:
                print('Банкомат не підтримує такий номінал.')

    @staticmethod
    def admin_menu():
        while True:
            print('1. Перевірити баланс банкомату')
            print('2. Провести інкасацію')
            print('3. Вийти')
            action = input('Будь ласка виберіть дію: ')
            if action == '1':
                ATM.show_atm_balance()
                print('')
            elif action == '2':
                ATM.atm_update()
                print('')
            elif action == '3':
                print('Бажаємо гарного дня!')
                return
            else:
                print('Введено некоректне значення. Повторіть вибір.')

def start():
    while True:
        print('1. Увійти в акаунт')
        print('2. Створити новий акаунт')
        print('3. Вийти')
        check = input('Будь ласка виберіть дію: ')
        if check == '1':
            user_instance = User()
            username = user_instance.login()
            print('')
            print(f'Вітаємо {username}!')
            if username == 'admin':
                ATM.admin_menu()
                return
            else:
                user_instance.user_menu(username)
                return
        elif check == '2':
            User.new_user()
        elif check == '3':
            print('Бажаємо гарного дня!')
            return
        else:
            print('Введено некоректне значення, повторіть спробу.')
            print('')

start()