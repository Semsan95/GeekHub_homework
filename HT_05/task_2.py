'''
Створiть 3 рiзних функцiї (на ваш вибiр).
Кожна з цих функцiй повинна повертати якийсь результат
(напр. інпут від юзера, результат математичної операції тощо).
Також створiть четверту ф-цiю, яка всередині викликає 3 попереднi,
обробляє їх результат та також повертає результат своєї роботи.
Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.
'''

def greetings():
    first_name = input('What is your name? ')
    last_name = input('What is your last name? ')
    return f'Hello, {first_name} {last_name}!'

def age():
    user_age = int(input('How old are you? '))
    age_in_hours = user_age * 8760
    return age_in_hours

def books():
    return int(input('How many books have you read? '))

def statistic():
    return f'{greetings()}, \nYour book reading speed is approximately: {books() / age()} book/hour'

print(statistic())