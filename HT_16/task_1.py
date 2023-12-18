'''
Автоматизувати процес замовлення робота за допомогою Selenium
1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv".
Увага! Файл має бути прочитаний з сервера кожного разу при запускі скрипта,
 не зберігайте файл локально.
2. Зайдіть на сайт "https://robotsparebinindustries.com/"
3. Перейдіть у вкладку "Order your robot"
4. Для кожного замовлення з файлу реалізуйте наступне:
    - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
    - оберіть/заповніть відповідні поля для замовлення
    - натисніть кнопку Preview та збережіть зображення отриманого робота. Увага!
    Зберігати треба тільки зображення робота, а не всієї сторінки сайту.
    - натисніть кнопку Order та збережіть номер чеку. Увага!
    Інколи сервер тупить і видає помилку,
    але повторне натискання кнопки частіше всього вирішує проблему. Дослідіть цей кейс.
    - переіменуйте отримане зображення у формат <номер чеку>_robot (напр. 123456_robot.jpg).
    Покладіть зображення в директорію output
    (яка має створюватися/очищатися під час запуску скрипта).
    - замовте наступного робота (шляхом натискання відповідної кнопки)
    '''

import os
import csv
import shutil
import requests
from time import sleep
from io import StringIO
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class OrderRobot:
    def __init__(self):
        self.url = 'https://robotsparebinindustries.com'
        self.driver = None
        self.check_num = None
        self.output_directory = Path(__file__).parent / 'output'
        self.output_directory = self.output_directory.resolve()
        self.orders_dicts = self.get_orders()

    def find_CSS_element(self, elem_link):
        element = self.driver.find_element(By.CSS_SELECTOR, elem_link)
        return element

    def wait_for_condition(self, elem_link):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.find_CSS_element(elem_link))
        )
        return element

    def open_browser(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(
            options=options,
            service=ChromeService(ChromeDriverManager().install())
        )
        self.driver.implicitly_wait(5)

    def create_output_dir(self):
        if (self.output_directory.exists()
                and self.output_directory.is_dir()):
            shutil.rmtree(self.output_directory)
        self.output_directory.mkdir(parents=True)

    def open_homepage(self):
        if not self.driver:
            self.open_browser()
        self.driver.get(self.url)

    def get_orders(self):
        response = requests.get(''.join([self.url, '/orders.csv']))
        reader = csv.DictReader(StringIO(response.text))
        orders_dict = [row for row in reader]
        return orders_dict

    def open_order_page(self):
        elem = self.wait_for_condition('a.nav-link[href="#/robot-order"]')
        elem.click()

    def skip_popup(self):
        alert = self.wait_for_condition('button.btn.btn-dark')
        alert.click()

    def select_head(self, order_value):
        select = Select(self.wait_for_condition('select[name="head"]'))
        select.select_by_value(order_value)

    def select_body(self, order_value):
        body = self.wait_for_condition(f'input[id="id-body-{order_value}"]')
        body.click()

    def select_legs(self, order_value):
        legs = self.wait_for_condition('input.form-control')
        legs.send_keys(order_value)

    def select_address(self, order_value):
        address = self.wait_for_condition('input#address')
        address.send_keys(order_value)

    def click_preview(self):
        preview = self.wait_for_condition('button#preview')
        self.driver.execute_script("arguments[0].click();", preview)

    def take_screenshot(self):
        robo_pic = self.wait_for_condition('div[id="robot-preview-image"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", robo_pic)
        sleep(1)
        robo_pic.screenshot(str(self.output_directory / 'temp_name.png'))

    def click_order(self):
        order_button = self.wait_for_condition('button#order')
        while True:
            try:
                self.driver.execute_script("arguments[0].click();", order_button)
                _ = self.wait_for_condition('div.alert.alert-danger')
            except NoSuchElementException:
                break

    def get_check_number(self):
        check_element = self.wait_for_condition('p.badge.badge-success')
        check_number = check_element.text
        return check_number

    def picture_rename(self):
        new_pic_name = f'{self.get_check_number()}.png'
        file_path = self.output_directory / 'temp_name.png'
        os.rename(file_path, self.output_directory / new_pic_name)

    def order_another_robot(self):
        order_another = self.wait_for_condition('button#order-another')
        self.driver.execute_script("arguments[0].click();", order_another)

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def load_robots(self):
        for order in self.orders_dicts:
            self.skip_popup()
            self.select_head(order['Head'])
            self.select_body(order['Body'])
            self.select_legs(order['Legs'])
            self.select_address(order['Address'])
            self.click_preview()
            self.take_screenshot()
            self.click_order()
            self.picture_rename()
            self.order_another_robot()

    def start(self):
        self.get_orders()
        self.create_output_dir()
        self.open_browser()
        self.open_homepage()
        self.open_order_page()
        self.load_robots()
        self.close_browser()

order = OrderRobot()
order.start()
