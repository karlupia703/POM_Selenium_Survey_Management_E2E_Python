from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverManager:
    _driver = None
    keep_browser_open = True

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            service = Service(ChromeDriverManager().install())
            cls._driver = webdriver.Chrome(service=service)
            cls._driver.maximize_window()
        return cls._driver