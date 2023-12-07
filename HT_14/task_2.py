'''
Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
'''

import requests
from datetime import datetime, timedelta


def json_get(input_date):
    params = {'date': input_date}
    response = requests.get('https://api.privatbank.ua/p24api/exchange_rates?', params=params)
    if response.ok:
        json_data = response.json()['exchangeRate']
        return json_data
    else:
        print(f'Нажаль виникла помилка. Код помилки: {response.status_code}')


def date_range(start_date, end_date):
    start_datetime = datetime.strptime(start_date, '%d.%m.%Y')
    end_datetime = datetime.strptime(end_date, '%d.%m.%Y')

    current_date = start_datetime
    date_list = []
    while current_date <= end_datetime:
        date_list.append(current_date.strftime('%d.%m.%Y'))
        current_date += timedelta(days=1)
    return date_list


def one_date(input_date, input_currency):
    json_data = json_get(input_date)
    found = False
    for current_dict in json_data:
        if input_currency == current_dict['currency']:
            print(f"{input_date} курс {input_currency} до UAH, становив: {round(current_dict['saleRateNB'], 2)}грн")
            found = True
            break
    if not found:
        available_currency = [i['currency'] for i in json_data]
        print("Такої валюти немає в архіві, виберіть зі списку доступних:")
        print(f"{', '.join(available_currency)} \n")
    return found


def interval_date(start_date, end_date, input_currency):
    date_list = date_range(start_date, end_date)
    for date in date_list:
        if not one_date(date, input_currency):
            return False
    return True


def currency_check(input_date, input_currency):
    params = {'date': input_date}
    response = requests.get('https://api.privatbank.ua/p24api/exchange_rates?', params=params)
    if response.ok:
        json_data = response.json()['exchangeRate']
        available_currency = [i['currency'] for i in json_data]
        if input_currency in available_currency:
            return True
        else:
            print("Такої валюти немає в архіві, виберіть зі списку доступних:")
            print(f"{', '.join(available_currency)} \n")
    else:
        print(f'Нажаль виникла помилка. Код помилки: {response.status_code}')


def date_check(date_str):
    try:
        current_date = datetime.strptime(date_str, '%d.%m.%Y')
        if current_date <= datetime.now() and current_date.year >= datetime.now().year - 4:
            return True
    except ValueError:
        return False


def date_compare(start_date, end_date):
    start_date = datetime.strptime(start_date, '%d.%m.%Y')
    end_date = datetime.strptime(end_date, '%d.%m.%Y')
    if start_date >= end_date:
        return False
    else:
        return True


def one_date_menu():
    input_date = input('Введіть дату в форматі - дд.мм.рррр: ')
    if date_check(input_date):
        input_currency = input('Введіть бажану валюту в форматі - UAH: ')
        if one_date(input_date, input_currency):
            return True
    else:
        print('Некоректний формат дати. Введіть дату - дд.мм.рррр, за останні 4 роки. \n')


def interval_menu():
    start_date = input('Введіть початкову дату, в форматі - дд.мм.рррр: ')
    end_date = input('Введіть кінцеву дату, в форматі - дд.мм.рррр: ')
    if date_check(start_date) and date_check(end_date):
        if date_compare(start_date, end_date):
            input_currency = input('Введіть бажану валюту в форматі - UAH: ')
            if interval_date(start_date, end_date, input_currency):
                return True
        else:
            print('Початкова дата не може бути більшою ніж кінцева. \n')
    else:
        print('Некоректний формат дати. Введіть дату - дд.мм.рррр, за останні 4 роки. \n')


def start():
    while True:
        print('Архів курсів валют ПриватБанку, НБУ за останні 4 роки.')
        print('1. Дізнатись курс на конкретну дату')
        print('2. Дізнатись курс за певний інтервал')
        print('3. Вийти')
        check = input('Виберіть дію: ')
        if check == '1':
            if one_date_menu():
                break
        elif check == '2':
            if interval_menu():
                break
        elif check == '3':
            print('Гарного дня!')
            break
        else:
            print('Вибраного варіанту не існує, спробуйте ще раз. \n')

start()

