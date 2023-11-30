'''
Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть фантазію).
Наприклад вона може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.
'''
import sqlite3

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Teacher(Person):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.user_type = 'teacher'

class Student(Person):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.user_type = 'student'

def add_user_to_db(user):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)', (user.username, user.password, user.user_type))
    conn.commit()
    conn.close()

def authenticate_user():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        username = input("Введіть ваш логін: ")
        password = input("Введіть ваш пароль: ")
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user_data = cursor.fetchone()
    return user_data

class Book:
    def __init__(self, title, author, shelf, genre_or_subject, book_type):
        self.title = title
        self.author = author
        self.shelf = shelf
        self.genre_or_subject = genre_or_subject
        self.book_type = book_type

class ScienceBook(Book):
    @classmethod
    def input_book(cls):
        title = input('Введіть назву: ')
        author = input('Введіть автора: ')
        subject = input('Введіть предмет: ')
        while True:
            try:
                shelf = int(input('Введіть номер полиці: '))
                print('Ви успішно повернули книгу.')
                break
            except ValueError:
                print("Номер полиці має бути цілим числом.")
        return cls(title, author, shelf, subject, "Наукова")

class FictionBook(Book):
    @classmethod
    def input_book(cls):
        title = input('Введіть назву: ')
        author = input('Введіть автора: ')
        genre = input('Введіть жанр: ')
        while True:
            try:
                shelf = int(input('Введіть номер полиці: '))
                print('Ви успішно повернули книгу.')
                break
            except ValueError:
                print("Номер полиці має бути цілим числом.")
        return cls(title, author, shelf, genre, "Художня")

def get_all_titles():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT title FROM books')
        all_titles = cursor.fetchall()
        for title in all_titles:
            print(title[0])

def save_book_to_db(book):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO books (title, author, shelf, genre_or_subject, book_type)
            VALUES (?, ?, ?, ?, ?)
            ''', (book.title, book.author, book.shelf, book.genre_or_subject, book.book_type))

def delete_book_by_title(title):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE title = ?', (title,))

def choose_action():
    while True:
        print('1. Взяти книгу')
        print('2. Повернути книгу')
        action = input("Виберіть дію: ")
        if action in ['1', '2']:
            return action
        else:
            print('Не вірний формат вводу.')

def choose_action_teacher():
    while True:
        print('1. Взяти книгу')
        print('2. Повернути книгу')
        print('3. Отримати перелік доступних книг')
        action = input("Виберіть дію: ")
        if action in ['1', '2', '3']:
            return action
        else:
            print('Не вірний формат вводу.')

def choose_book_type():
    while True:
        print('1. Навчальні матеріали')
        print('2. Художня література')
        action = input("Виберіть дію: ")
        if action in ['1', '2']:
            if action == '1':
                science_book = ScienceBook.input_book()
                save_book_to_db(science_book)
            elif action == '2':
                fiction_book = FictionBook.input_book()
                save_book_to_db(fiction_book)
        else:
            print('Не вірний формат вводу.')

def start():
    while True:
        print('Шкільна бібліотека: ')
        print('1. Увійти')
        print('2. Зареєструватись')
        print('3. Вийти')
        check = input('Будь ласка виберіть дію: ')
        if check == '1':
            user_data = authenticate_user()
            if user_data:
                user_type = user_data[3]
                if user_type == 'teacher':
                    action = choose_action_teacher()
                    if action == '1':
                        delete_title = input("Введіть назву книги: ")
                        delete_book_by_title(delete_title)
                        print(f"Ви забрали книжку: '{delete_title}'.")
                    elif action == '2':
                        choose_book_type()
                        return
                    elif action == '3':
                        get_all_titles()
                        return
                elif user_type == 'student':
                    action = choose_action()
                    if action == '1':
                        delete_title = input("Введіть назву книги: ")
                        delete_book_by_title(delete_title)
                        print(f"Ви забрали книжку: '{delete_title}'.")
                    elif action == '2':
                        choose_book_type()
                        return
            else:
                print("Неправильний логін або пароль.")
        elif check == '2':
            print('Ви викладач чи учень?')
            print('1. Викладач')
            print('2. Учень')
            user_check = input('Введіть відповідь: ')
            if user_check == '1':
                username = input('Введіть новий логін: ')
                password = input('Введіть новий пароль: ')
                teacher = Teacher(username, password)
                add_user_to_db(teacher)
            elif user_check == '2':
                username = input('Введіть новий логін: ')
                password = input('Введіть новий пароль: ')
                student = Student(username, password)
                add_user_to_db(student)
            else:
                print('Не вірний формат вводу.')
        elif check == '3':
            print('Приємного читання!')
            return
        else:
            print('Введено некоректне значення, повторіть спробу.')
            print('')

start()