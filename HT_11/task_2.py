'''
Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи,
які зберігатиме в відповідні змінні.
- Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
- Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession
(його не має інсувати під час ініціалізації).
'''

class Person:

    def __init__(self, age, name, surname, sex):
        self.age = age
        self.name = name
        self.surname = surname
        self.sex = sex

    def show_age(self):
        print(f"Вік користувача: {self.age}")

    def print_name(self):
        print(f"Прізвище і ім'я користувача: {self.surname} {self.name}")

    def show_all_information(self):
        print(f"Вік: {self.age}")
        print(f"Ім'я: {self.name}")
        print(f"Прізвище: {self.surname}")
        print(f"Стать: {self.sex}")

user_1 = Person(92, 'Боб', 'Сміт', 'Мужичара')
user_2 = Person(25, 'Іванка', 'Петросян', 'Жінка')

user_1.profession = 'Камєнщік'
user_2.profession = 'Стендаперша'

user_1.show_all_information()
print(f'Професія: {user_1.profession}')
user_2.print_name()
print(f'Професія: {user_2.profession}')