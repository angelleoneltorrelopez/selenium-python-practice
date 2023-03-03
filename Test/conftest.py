import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome"], scope='function')
def init_driver(request):
    if request.param == "chrome":
        options = Options()
        options.page_load_strategy = 'none'
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        web_driver.maximize_window()
    if request.param == "firefox":
        caps = DesiredCapabilities().FIREFOX
        caps["pageLoadStrategy"] = "none"
        web_driver = webdriver.Firefox(desired_capabilities=caps,
                                       service=FirefoxService(GeckoDriverManager().install()))
        web_driver.maximize_window()
    web_driver.implicitly_wait(1)
    request.cls.driver = web_driver
    yield
    web_driver.quit()
