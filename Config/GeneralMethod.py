from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expectedconditions
from selenium.webdriver.common.keys import Keys


class GeneralMethod:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator, time):
        WebDriverWait(self.driver, time).until(expectedconditions.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text, time):
        WebDriverWait(self.driver, time).until(expectedconditions.visibility_of_element_located(by_locator)).send_keys(
            text)

    def get_text(self, by_locator, time):
        element = WebDriverWait(self.driver, time).until(expectedconditions.visibility_of_element_located(by_locator))
        return element.text

    def enter(self, by_locator):
        WebDriverWait(self.driver, 10).until(expectedconditions.visibility_of_element_located(by_locator)).send_keys(
            Keys.ENTER)

    def is_enabled(self, by_locator, time):
        element = WebDriverWait(self.driver, time).until(expectedconditions.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title, time):
        WebDriverWait(self.driver, time).until(expectedconditions.title_is(title))
        return self.driver.title
