from faker import Faker
import time
from bs4 import BeautifulSoup
from faker.generator import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from Config.config import Config
from test_Data.translations import Translations


class SurveyDashboardPage:
    def __init__(self, driver):
        self.faker = Faker()
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Selectors for search survey
    search_input = By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/input"
    survey_name = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]"
    search_cross_icon = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/button"
    category_dropdown = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]"
    category_cross_icon = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/button"
    survey_tab = By.XPATH, "/html/body/div[1]/div/div/div[1]/div/nav/a[1]/div/div[2]/span"

    # Selectors for View survey
    view_icon = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/button"
    view_cancel_btn = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[1]"

    # Edit basic information
    dashboard_edit_icon = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/a/button"
    name_input = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div/input"
    language_field = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[6]/div/div/div"
    select_language_edit = By.XPATH, "/html/body/div[3]/div[3]/ul/li[6]"
    survey_save_button = By.XPATH, "//html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/button"
    save_survey_dialog_box = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"

    # Selectors for pagination
    right_arrow = By.XPATH, "//button[@aria-label='Go to the next page' or @aria-label='Ir a la página siguiente' or @aria-label='Ir para a próxima página']"
    left_arrow = By.XPATH, "//button[@aria-label='Go to the previous page' or @aria-label='Ir a la página anterior' or @aria-label='Ir para a página anterior']"

    #Selectors for navbar
    navbar_cross_icon = By.XPATH, "//button[contains(@class, 'Mui-selected')]//svg[@data-testid='CloseIcon']"


    def generate_random_string(self, length=3):
        """Generate a random string of digits with the given length."""
        characters = "0123456789"
        return ''.join(random.choices(characters, k=length))


    # Method for search functionality
    def search_survey_name(self):
        """Clicks search field, gets question name from first row, and performs search."""
        search_field_element = self.driver.find_element(*self.search_input)
        search_field_element.click()
        # Extract question name from first row
        survey_name_element = self.driver.find_element(
            By.XPATH,
            "//table/tbody/tr[1]/td[2]"
        )
        survey_name = survey_name_element.text.strip()
        if not survey_name:
            raise ValueError("No survey name found in the first row.")

        # Enter survey name into the search field
        search_field_element.send_keys(survey_name)
        time.sleep(2)
        return survey_name

    def clear_survey_name(self):
        """Clicks the cross icon to clear the search field."""
        cross_icon_element = self.driver.find_element(*self.search_cross_icon)
        cross_icon_element.click()


    # Method for search category option functionality
    def select_random_category_option(self):
        # Open the dropdown
        self.driver.find_element(*self.category_dropdown).click()
        # Wait for the dropdown menu to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[role='listbox']"))
        )
        # Get all the <li> options in the dropdown
        options = self.driver.find_elements(By.CSS_SELECTOR, "ul[role='listbox'] li[role='option']")
        if not options:
            raise Exception("No options found in the type dropdown.")
        # Pick a random option
        random_option = random.choice(options)
        selected_value = random_option.get_attribute("data-value")
        selected_text = random_option.text
        random_option.click()

        self.driver.find_element(*self.category_cross_icon).click()
        time.sleep(1)
        print(f"Selected option: {selected_text} ")
        return selected_value

    def click_on_survey_tab(self):
        self.driver.find_element(*self.survey_tab).click()


    # Method for view survey
    def click_on_survey_view(self):
        self.driver.find_element(*self.view_icon).click()
        time.sleep(1)

    def click_on_view_cancel_button(self):
        self.driver.find_element(*self.view_cancel_btn).click()
        time.sleep(1)


    # Method of edit basic information of survey
    def click_on_survey_name_field(self):
        self.driver.find_element(*self.dashboard_edit_icon).click()
        name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.name_input)
        )
        name_field.click()
        # Clear the field properly
        name_field.send_keys(Keys.CONTROL, "a")  # Select all text
        name_field.send_keys(Keys.DELETE)
        time.sleep(1)
        survey_name = "Edit survey" + self.generate_random_string(3)
        name_field.send_keys(survey_name)
        print(f"Edited survey created with name: {survey_name}")

    def change_language(self):
        self.driver.find_element(*self.language_field).click()

    def select_of_survey_language(self):
        self.driver.find_element(*self.select_language_edit).click()

    def click_on_save_button(self):
        self.driver.find_element(*self.survey_save_button).click()

    def click_on_save_survey_dilog_box(self):
        self.driver.find_element(*self.save_survey_dialog_box).click()


    # Methods for pagination
    def is_pagination_arrow_available(self, arrow_locator):
            elements = self.driver.find_elements(*arrow_locator)
            return len(elements) > 0

    def is_pagination_arrow_enabled(self, arrow_locator):
            arrow = self.driver.find_element(*arrow_locator)
            return arrow.is_enabled() and arrow.value_of_css_property("pointer-events") == "auto"

    def click_pagination_arrow(self, arrow_locator):
            arrow = self.driver.find_element(*arrow_locator)
            arrow.click()

    def is_right_arrow_available(self):
            return self.is_pagination_arrow_available(self.right_arrow)

    def is_right_arrow_enabled(self):
            return self.is_pagination_arrow_enabled(self.right_arrow)

    def click_right_arrow(self):
            self.click_pagination_arrow(self.right_arrow)

    def is_left_arrow_available(self):
            return self.is_pagination_arrow_available(self.left_arrow)

    def is_left_arrow_enabled(self):
            return self.is_pagination_arrow_enabled(self.left_arrow)

    def click_left_arrow(self):
            self.click_pagination_arrow(self.left_arrow)
