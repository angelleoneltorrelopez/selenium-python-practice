from Test.test_base import BaseTest
from Pom.login import Login


class Test_Login(BaseTest):

    def test_login(self):
        self.login = Login(self.driver)
        self.login.send_username("1000123456789")
        self.login.send_password("Kony@2020")
        self.login.click_button_singin()
