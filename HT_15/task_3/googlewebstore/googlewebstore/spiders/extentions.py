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

    def parse(self, response, **kwargs):
        for link in self.parse_sitemap(response.text)[:5]:
            yield Request(url=link, callback=self.process_sitemap)

    def process_sitemap(self, response):
        for extension_link in self.parse_sitemap(response.text):
            yield Request(url=extension_link, callback=self.save_extension)

    @staticmethod
    def parse_sitemap(response_text):
        soup = BeautifulSoup(response_text, 'lxml')
        return [loc.text for loc in soup.find_all('loc')]

    @staticmethod
    def save_extension(response):
        description = 'div.C-b-p-j-D.Ka-Ia-j.C-b-p-j-D-gi ::text'
        yield Extension(
            id=response.url.split('/')[-1].split('?')[0],
            name=response.css('h1.e-f-w::text').get(),
            description=response.css(description).getall()
        )
