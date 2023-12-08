'''
http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
'''
import csv
import requests
from bs4 import BeautifulSoup


def author_to_dict(author, block):
    url_about = ''.join(["https://quotes.toscrape.com", block.find("a").get("href")])
    response_about = requests.get(url_about)
    soup_about = BeautifulSoup(response_about.text, 'lxml')
    born_date = soup_about.find("span", class_="author-born-date").text
    born_location = soup_about.find("span", class_="author-born-location").text
    born_text = ' '.join([born_date, born_location])
    return {author: born_text}


def csv_writer(author, quote, writer, block):
    author_born = {}
    if author not in author_born:
        author_born.update(author_to_dict(author, block))
    writer.writerow([author, author_born[author], quote])


def get_author_and_quote(block):
        author = block.find("small", itemprop="author").text.replace("\n", "")
        quote = block.find("span", itemprop="text").text
        return author, quote


def get_quote_blocks(soup):
    quote_blocks = soup.find_all("div", class_="quote")
    return quote_blocks


def next_page_check(soup):
    next_page = soup.find('li', class_='next')
    return next_page


def check_response(response):
    try:
        response.raise_for_status()
        return True
    except requests.HTTPError as err:
        print(f'Нажаль виникла помилка. Код помилки: {err.response.status_code}')
        return False


def scraper(writer):
    page_num = 0
    while True:
        url = 'https://quotes.toscrape.com/page/'
        page_num += 1
        response = requests.get(f'{url}{page_num}')
        if not check_response(response):
            break
        soup = BeautifulSoup(response.text, 'lxml')
        next_page = next_page_check(soup)
        if next_page and page_num != 11:
            quote_blocks = get_quote_blocks(soup)
            for block in quote_blocks:
                author, quote = get_author_and_quote(block)
                csv_writer(author, quote, writer, block)
            print(f'Page {page_num}: Complete.')
        else:
            break


def csv_open():
    with open('authors.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Born', 'Quote'])
        scraper(writer)
        print('End.')


def start():
    csv_open()


start()