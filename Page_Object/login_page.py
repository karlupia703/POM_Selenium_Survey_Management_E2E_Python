import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import Config

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Selectors
    language_dropdown = By.XPATH,"/html/body/div/div/div[3]/div/div"
    select_english_language = By.CSS_SELECTOR,"[data-test-id='text-language-option-English (EE.UU.)']"
    google_sign_in_button = By.XPATH,"/html/body/div/div/button/div/span"
    email_input = By.XPATH, "//input[@type='email']"
    email_next_button = By.XPATH, "//span[text()='Next']"
    password_input = By.XPATH, "//input[@type='password']"
    password_next_button = By.XPATH, "//span[text()='Next']"
    # Selectors for Assertions
    login_title = By.XPATH, "/html/body/div/div/div[1]/span"
    google_button_text = By.XPATH, "/html/body/div/div/button/div/span"
    access_text_of_survey_app = By.XPATH, "/html/body/div/div/div[2]/span[2]"
    sign_in_text = By.XPATH, "/html/body/div/div/div[2]/span[1]"

    def click_language_dropdown(self):
        self.driver.find_element(*self.language_dropdown).click()

    def select_language(self, language_code: str):
        language_option = (By.CSS_SELECTOR, f"[data-value='{language_code}']")
        self.driver.find_element(*language_option).click()

    def get_selected_language(self) -> str:
        try:
            language_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.language_dropdown)
            )
            return language_element.text.strip()
        except:
            print("Language dropdown not found")
            return None

    def click_on_google_sign_in_button(self):
            google_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.google_sign_in_button)
            )
            google_button.click()

    def enter_email_address(self, email: str):
        email_input = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.email_input)
        )
        email_input.send_keys(email)

    def click_email_next_button(self):
        self.driver.find_element(*self.email_next_button).click()

    def enter_password_address(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_input)
        )
        password_input.send_keys(password)

    def click_password_next_button(self):
        self.driver.find_element(*self.password_next_button).click()

    # Assertions methods
    def get_element_text(self, locator: tuple) -> str:
        return self.driver.find_element(*locator).text.strip()

    def is_title_correct(self, expected_title: str) -> bool:
        return self.get_element_text(self.login_title) == expected_title

    def is_access_with_google_text_correct(self, expected_text: str) -> bool:
        return self.get_element_text(self.google_button_text) == expected_text

    def is_access_with_survey_app_text(self, expected_text: str) -> bool:
        return self.get_element_text(self.access_text_of_survey_app) == expected_text

    def is_sign_in_button_text_correct(self, expected_text: str):
        return self.get_element_text(self.sign_in_text) ==expected_text
