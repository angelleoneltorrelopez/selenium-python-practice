from selenium.webdriver.common.by import By

from Config.GeneralMethod import GeneralMethod
from Config.config import TestData


class Login(GeneralMethod):
    username_input = (By.ID, "frmLogin_main_tbxUserName")
    password_input = (By.ID, "frmLogin_main_tbxPassword")
    singIn_button = (By.ID, "frmLogin_main_btnLogin")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def send_username(self, text):
        self.send_keys(self.username_input, text, 5)

    def send_password(self, text):
        self.send_keys(self.password_input, text, 5)

    def click_button_singin(self):
        self.click(self.singIn_button, 5)

