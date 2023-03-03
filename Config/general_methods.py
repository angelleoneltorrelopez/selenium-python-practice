from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class GeneralMethod:
    def __init__(self, driver):
        self.driver = driver

    def element_wait(self, by_locator, time):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(by_locator))

    def click(self, by_locator, time):
        self.element_wait(by_locator, time)
        element = WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(by_locator))
        element.click()
        return True

    def click_js(self, by_locator, time):
        element = self.element_wait(by_locator, time)
        self.driver.execute_script("arguments[0].click();", element)
        return True

    def send_keys(self, by_locator, text, time):
        element = self.element_wait(by_locator, time)
        element.send_keys(text)

    def get_text(self, by_locator, time):
        element = self.element_wait(by_locator, time)
        return element.text

    def enter(self, by_locator):
        element = self.element_wait(by_locator, 10)
        element.send_keys(Keys.ENTER)

    def is_visible(self, by_locator, time):
        element = self.element_wait(by_locator, time)
        return bool(element)

    def get_title(self, title, time):
        WebDriverWait(self.driver, time).until(expected_conditions.title_is(title))
        return self.driver.title

    def alert_accept(self, time):
        alert = WebDriverWait(self.driver, time).until(expected_conditions.alert_is_present())
        alert.accept()

    def alert_cancel(self, time):
        alert = WebDriverWait(self.driver, time).until(expected_conditions.alert_is_present())
        alert.dismiss()

    def alert_get_text(self, time):
        alert = WebDriverWait(self.driver, time).until(expected_conditions.alert_is_present())
        text = alert.text
        alert.accept()
        return text

    def alert_send_keys(self, text, time):
        alert = WebDriverWait(self.driver, time).until(expected_conditions.alert_is_present())
        alert.send_keys(text)
        alert.accept()

    def move_to_element(self, by_locator):
        element = self.element_wait(by_locator, 10)
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        return True

    def load_url(self, url):
        self.driver.get(url)
        self.wait_page_load()

    def wait_page_load(self):
        try:
            WebDriverWait(self.driver, 1).until(
                lambda driver: driver.execute_script("return document.readyState").equals("interactive"))
            WebDriverWait(self.driver, 1).until(
                lambda driver: driver.execute_script("return document.readyState").equals("complete"))
        except:
            print("")

    def switch_to_frame(self, by_locator):
        iframe = self.driver.find_element(By.XPATH, by_locator)
        self.driver.switch_to.frame(iframe)

    def leaving_frame(self):
        self.driver.switch_to.default_content()
