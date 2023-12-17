"""
Отримайте та прочитайте дані з 
"https://robotsparebinindustries.com/orders.csv". 
Увага! Файл має бути прочитаний з сервера кожного 
разу при запускі скрипта, не зберігайте файл локально.
2. Зайдіть на сайт "https://robotsparebinindustries.com/"
3. Перейдіть у вкладку "Order your robot"
4. Для кожного замовлення з файлу реалізуйте наступне:
    - закрийте pop-up, якщо він з'явився. 
    Підказка: не кожна кнопка його закриває.
    - оберіть/заповніть відповідні поля для замовлення
    - натисніть кнопку Preview та збережіть 
    зображення отриманого робота. 
    Увага! Зберігати треба тільки 
    зображення робота, а не всієї сторінки сайту.
    - натисніть кнопку Order та 
    збережіть номер чеку. Увага! 
    Інколи сервер тупить і видає помилку, 
    але повторне натискання кнопки частіше 
    всього вирішує проблему. Дослідіть цей кейс.
    - переіменуйте отримане зображення у 
    формат <номер чеку>_robot (напр. 123456_robot.jpg). 
    Покладіть зображення в директорію output 
    (яка має створюватися/очищатися під час запуску скрипта).
    - замовте наступного робота 
    (шляхом натискання відповідної кнопки)
"""
import os
from io import BytesIO
from pathlib import Path
import requests
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

BASE_URL = "https://robotsparebinindustries.com/"
OUTPUT_DIR_PATH = Path(__file__).parent / 'output'
OUTPUT_DIR_PATH = OUTPUT_DIR_PATH.resolve()

SERVICE = ChromeService(ChromeDriverManager().install())
WIDTH_IMAGE = 600
HEIGHT_IMAGE = 200


class RobotOrderAutomation:
    def __init__(self):
        self.output_directory = OUTPUT_DIR_PATH
        self.current_robot_image = None
        self.driver = webdriver.Chrome(service=SERVICE)
        self.driver.get(BASE_URL)
        self.initialize_output_directory()

    def initialize_output_directory(self):
        if os.path.exists(self.output_directory):
            shutil.rmtree(self.output_directory)
        os.makedirs(self.output_directory)

    def navigate_to_order_robot_page(self):
        page_links = self.driver.find_elements(By.CLASS_NAME, "nav-link")
        order_robot_link = page_links[-1]
        order_robot_link.click()

    def wait_for_element(self, xpath_element, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath_element))
        )

    def close_modal_popup(self):
        xpath = "//button[@class='btn btn-danger' and text()='I guess so...']"
        close_button = self.wait_for_element(xpath)
        close_button.click()

    def build_robot_order(self, order_data):
        head_value, body_value, legs_value, address_value = order_data
        input_elements = self.driver.find_elements(By.CLASS_NAME, "form-control")

        self.select_option_by_value(head_value)
        self.select_radio_by_value(body_value)

        legs_element = input_elements[0]
        self.enter_text(legs_element, legs_value)

        address_element = input_elements[1]
        self.enter_text(address_element, address_value)

    def select_option_by_value(self, value):
        option_element = self.driver.find_element(By.XPATH, f"//option[@value={value}]")
        option_element.click()

    def select_radio_by_value(self, value):
        radio_element = self.driver.find_element(By.XPATH, f"//input[@value={value}]/ancestor::label")
        radio_element.click()

    def enter_text(self, element, text):
        element.clear()
        element.send_keys(text)

    def click_preview_button(self, max_attempts=5):
        for _ in range(max_attempts):
            try:
                preview_button = self.driver.find_element(By.XPATH, '//button[@id="preview"]')
                self.driver.execute_script("arguments[0].click();", preview_button)

                xpath = "//div[@id='robot-preview-image']"
                image = self.wait_for_element(xpath).find_element(By.XPATH, xpath)
                
                if image:
                    break
            except Exception:
                pass

    def click_order_button(self):
        try:
            while True:
                order_button = self.driver.find_element(By.XPATH, '//button[@id="order"]')
                self.driver.execute_script("arguments[0].click();", order_button)
        except Exception:
            pass

    def get_order_number(self):
        xpath = "//p[@class='badge badge-success']"
        order_number_element = self.wait_for_element(xpath)
        return order_number_element.find_element(By.XPATH, xpath).text

    def create_robot_image(self, data_arg):
        image_urls = [
            f"https://robotsparebinindustries.com/{part}/{value}.png"
            for part, value in zip(["heads", "bodies", "legs"], data_arg)
        ]
        images = [
            Image.open(BytesIO(requests.get(url).content)).resize((HEIGHT_IMAGE, HEIGHT_IMAGE))
            for url in image_urls
        ]
        self.current_picture = Image.new(
            'RGB',
            (max(img.width for img in images), sum(img.height for img in images))
        )
        self.current_picture.paste(images[0], (0, 0))
        y_offset = images[0].height
        for img in images[1:]:
            self.current_picture.paste(img, (0, y_offset))
            y_offset += img.height

    def save_robot_image(self):
        if self.current_picture:
            order_number = self.get_order_number()
            file_name = f"output/{order_number}_robot.jpg"
            self.current_picture.save(file_name)
        else:
            print(" No image.")

    def make_all_robot_orders(self):
        data = self.get_order_data(BASE_URL)
        for data_item in data:
            self.close_modal_popup()
            self.build_robot_order(data_item)
            self.click_preview_button()
            self.create_robot_image(data_item)
            self.click_order_button()
            self.save_robot_image()
            self.click_order_another_robot()

    def click_order_another_robot(self):
        self.driver.find_element(By.XPATH, "//button[@id='order-another']").click()

    def start_automation(self):
        self.navigate_to_order_robot_page()
        self.make_all_robot_orders()

    @staticmethod
    def get_order_data(url):
        csv_url = "orders.csv"
        response = requests.get(url + csv_url)
        return [item.split(",")[1:] for item in response.text.split("\n")[1:]]

    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    robot_automation = RobotOrderAutomation()
    robot_automation.start_automation()
