from selenium.webdriver.common.by import By

from Config.GeneralMethod import GeneralMethod
from Config.config import TestData


class Page(GeneralMethod):
    buttonsearch = (By.XPATH, "//div[@class = 'search']")
    inputsearch = (By.XPATH, "//input[@name = 'q']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_page_title(self, title):
        return self.get_title(title, 10)

    def click_icon_search(self):
        self.click(self.buttonsearch, 10)

    def send_search(self, text):
        self.send_keys(self.inputsearch, text, 10)
        self.enter(self.inputsearch)
