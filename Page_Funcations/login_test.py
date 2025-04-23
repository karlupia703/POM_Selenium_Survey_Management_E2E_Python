import time
from selenium.webdriver.support.wait import WebDriverWait
from Page_Funcations.driver_manager import DriverManager
from Page_Object.login_page import LoginPage
from Config.config import Config
from test_Data.translations import Translations

class LoginTest:
    def __init__(self):
        self.base_url = Config.base_url

    def setup_method(self):
        self.driver = DriverManager.get_driver()
        time.sleep(2)
        self.driver.get(self.base_url)
        time.sleep(3)
        self.page = LoginPage(self.driver)
        time.sleep(3)

    def test_login_user(self):
        expected_texts = Translations.get_translation(Config.language)
        if not expected_texts:
            raise ValueError(f"Language '{Config.language}' not found in translations")
        self.switch_language_if_needed(Config.language, expected_texts)
        self.page.click_on_google_sign_in_button()
        time.sleep(3)
        self.handle_google_login()
        time.sleep(3)

    def switch_language_if_needed(self, target_language, expected_texts):
        current_language = self.page.get_selected_language().strip().split("(")[0].strip()

        if current_language.lower() != target_language.lower():
            self.page.click_language_dropdown()
            time.sleep(2)
            self.page.select_language(target_language)
            time.sleep(2)
        self.verify_login_texts(expected_texts)

    def verify_login_texts(self, expected_texts):
        assert self.page.is_title_correct(expected_texts["title"]), "Title text mismatch"
        assert self.page.is_access_with_google_text_correct(expected_texts["googleButton"]), "Google button text mismatch"
        assert self.page.is_access_with_survey_app_text(
            expected_texts["accessWithGoogle"]), "Access with survey management text mismatch"
        assert self.page.is_sign_in_button_text_correct(expected_texts["signInButton"]), "Sign in text mismatch"
        print("All assertions passed successfully.")

    def handle_google_login(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 15).until(lambda d: len(d.window_handles) > 1)

        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

        time.sleep(3)
        self.page.enter_email_address(Config.Email)
        time.sleep(3)
        self.page.click_email_next_button()
        time.sleep(3)
        self.page.enter_password_address(Config.Password)
        time.sleep(3)
        self.page.click_password_next_button()
        time.sleep(3)
        self.driver.switch_to.window(original_window)
        time.sleep(3)
