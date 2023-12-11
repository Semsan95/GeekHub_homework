'''
Викорисовуючи requests, заходите на ось цей сайт "https://www.expireddomains.net/deleted-domains/"
(з ним будьте обережні), вибираєте будь-яку на ваш вибір доменну зону і парсите список  доменів
- їх там буде десятки тисяч (звичайно ураховуючи пагінацію). Всі отримані значення зберігти в CSV файл.
'''

import csv
import random
import requests
from time import sleep
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}


def random_sleep():
    delay = random.uniform(15, 30)
    sleep(delay)


def get_soup(next_page):
    url = 'https://www.expireddomains.net/deleted-domains/'
    final_url = ''.join([url, next_page])
    response = requests.get(final_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def next_page_check(soup): # якщо є - відкриваємо наступну сторінку
    next_page = soup.find('a', class_='next')
    return next_page


def get_domains(soup): # з супу обраної сторінки знаходить кожен домен і повертає його список
    domains_group = soup.find_all('td', class_='field_domain')
    domains_list = []
    for domain in domains_group:
        domain_name = domain.find('a').text
        domains_list.append(domain_name)
    return domains_list


def csv_writer(domains_list):
    with open('domains.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for domain in domains_list:
            writer.writerow([domain])


def csv_header():
    with open('domains.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Domains'])


def scraper():
    page_num = 0
    next_page = ''
    csv_header()
    while True:
        soup = get_soup(next_page)
        domains_list = get_domains(soup)
        csv_writer(domains_list)
        next_page = next_page_check(soup)
        if next_page:
            page_num += 25
            next_page = f'?start={str(page_num)}#listing'
            print(f'Зібрав домени з {int(page_num / 25)} сторінки.')
            random_sleep()
        else:
            print('Всі доступні домени зібрані.')
            break


scraper()