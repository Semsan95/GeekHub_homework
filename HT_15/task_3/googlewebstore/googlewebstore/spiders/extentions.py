'''
Використовуючи Scrapy, заходите на "https://chrome.google.com/webstore/sitemap", 
переходите на кожен лінк з тегів <loc>, з кожного лінка берете посилання на сторінки екстеншенів, 
парсите їх і зберігаєте в CSV файл ID, назву та короткий опис кожного екстеншена 
(пошукайте уважно де його можна взяти)
'''

import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class Extension:
    id: str
    name: str
    description: str

class ExtentionsSpider(scrapy.Spider):
    name = "extentions"
    allowed_domains = ["chrome.google.com", "chromewebstore.google.com"]
    start_urls = ["https://chrome.google.com/webstore/sitemap"]


    def parse(self, response):
        for link in self.parse_sitemap(response.text)[:5]:
            yield Request(url=link, callback=self.process_sitemap)


    def parse_sitemap(self, response_text):
        soup = BeautifulSoup(response_text, 'lxml')
        return [loc.text for loc in soup.find_all('loc')]


    def process_sitemap(self, response):
        for extension_link in self.parse_sitemap(response.text):
            yield Request(url=extension_link, callback=self.save_extension)


    def save_extension(self, response):
        yield Extension(
            id=response.url.split('/')[-1].split('?')[0],
            name=response.css('h1.e-f-w::text').get(),
            description=response.css('div.C-b-p-j-D.Ka-Ia-j.C-b-p-j-D-gi ::text').getall()
        )
