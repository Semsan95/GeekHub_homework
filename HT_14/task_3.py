'''
http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
'''
import csv
import requests
from bs4 import BeautifulSoup


def author_to_dict():
    url_about = "https://quotes.toscrape.com" + section.find("a").get("href")
    resp_about = requests.get(url_about)
    soup_about = BeautifulSoup(resp_about.text, 'lxml')
    born_date = soup_about.find("span", class_="author-born-date").text
    born_location = soup_about.find("span", class_="author-born-location").text
    born_text = born_date + ' ' + born_location
    author_born[author] = born_text

with open('authors.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Born', 'Quote'])
    author_born = {}
    for page in range(1, 11):
        response = requests.get(f'https://quotes.toscrape.com/page/{page}')
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all("div", class_="quote")
        for section in data:
            author = section.find("small", itemprop="author").text.replace("\n", "")
            quote = section.find(itemprop="text").text
            if author not in author_born:
                author_to_dict()
            writer.writerow([author, author_born[author], quote])
            break