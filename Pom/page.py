from selenium.webdriver.common.by import By

from Config.general_methods import GeneralMethod


class Page(GeneralMethod):
    a_element = (By.ID, "a")
    abbr_element = (By.ID, "abbr")
    button_element = (By.ID, "button")

    def __init__(self, driver):
        super().__init__(driver)

    def click_link(self):
        return self.click(self.a_element, 10)

    def click_link_js(self):
        return self.click_js(self.a_element, 10)

    def click_button(self):
        return self.click(self.button_element, 10)

    def get_text_alert(self):
        return self.alert_get_text(10)

    def moveto_element(self):
        return self.move_to_element(self.abbr_element)
