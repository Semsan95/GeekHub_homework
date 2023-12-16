# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class GooglewebstorePipeline:
    def __init__(self):
        self.csv_file = open('extentions.csv', 'w',
                             newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['id', 'name', 'description'])

    def process_item(self, item, spider):
        self.csv_writer.writerow([item.id, item.name, item.description])
        return item

    def close_spider(self, spider):
        self.csv_file.close()
