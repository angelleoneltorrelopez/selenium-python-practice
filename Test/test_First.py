from Test.test_base import BaseTest
from Pom.page import Page


class Test_First(BaseTest):

    def test_click_icon_search(self):
        self.page = Page(self.driver)
        self.page.click_icon_search()
        self.page.send_search("java")
