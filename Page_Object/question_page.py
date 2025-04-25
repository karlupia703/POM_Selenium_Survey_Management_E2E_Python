import string
from faker import Faker
import time
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


class QuestionPage:
    def __init__(self, driver):
        self.faker = Faker()
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Selectors for Questions
    question_tab = By.XPATH, "/html/body/div[1]/div/div/div[1]/div/nav/a[2]/div/div[2]"
    create_question_btn = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/button"
    create_inside_ques_btn = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"
    question_type = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div"
    question_type_dropdown = By.XPATH, "/html/body/div[4]/div[3]/ul"
    abbreviation_question_field = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/div/input"
    question_description = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[3]/div/div"

    # Selectors for edit question
    edit_question_icon = By.XPATH, "//tbody/tr[1]/td[6]/div/button[1]"

    # Selectors for delete question
    delete_icon = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/button[2]"
    cancel_button = By.XPATH, "//button[normalize-space()='Cancel' or normalize-space()='Cancelar']"

    # Selectors for search question
    search_input = By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/input"
    question_name = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]"
    search_cross_icon = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/button"
    type_dropdown = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]"
    type_cross_icon = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/button"
    survey_tab = By.XPATH, "/html/body/div[1]/div/div/div[1]/div/nav/a[1]/div/div[2]/span"

    # Selectors for pagination
    right_arrow = By.XPATH, "//button[@aria-label='Go to the next page' or @aria-label='Ir a la página siguiente' or @aria-label='Ir para a próxima página']"
    left_arrow = By.XPATH, "//button[@aria-label='Go to the previous page' or @aria-label='Ir a la página anterior' or @aria-label='Ir para a página anterior']"
    rows_par_page = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div"
    rows_par_20_page = By.XPATH, "/html/body/div[3]/div[3]/ul/li[2]"

    def generate_random_description(self, sentences=2):
        return self.faker.paragraph(nb_sentences=sentences)

    def generate_random_string(self, length=3):
        """Generate a random string of digits with the given length."""
        characters = "0123456789"
        return ''.join(random.choices(characters, k=length))


    # Method for create question
    def click_on_question_tab(self):
        self.driver.find_element(*self.question_tab).click()

    def click_on_create_question_button(self):
        self.driver.find_element(*self.create_question_btn).click()

    def click_on_question_inside_create_btn(self):
        self.driver.find_element(*self.create_inside_ques_btn).click()

    def click_on_question_type(self):
        self.driver.find_element(*self.question_type).click()
        options = self.driver.find_elements(*self.question_type_dropdown)
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options available in the dropdown.")
            time.sleep(3)

    def click_on_abbreviation_question_field(self):
        abbreviation_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.abbreviation_question_field)
        )
        abbreviation = "Abbr" + self.generate_random_string(4)
        abbreviation_input.send_keys(abbreviation)
        print(f"Abbreviation created with name: {abbreviation}")

    def enter_question_description(self):
        random_description = self.generate_random_description()
        # Target the actual <textarea> inside the div
        question_desc_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.MuiInputBase-inputMultiline"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_desc_field)
        time.sleep(0.5)
        question_desc_field.send_keys(random_description)
        print(f"Entered Description: {random_description}")


    # Method for edit question
    def click_on_edit_question_icon(self):
        self.driver.find_element(*self.edit_question_icon).click()

    def edit_question_field(self):
        random_description = self.generate_random_description()
        question_desc_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.MuiInputBase-inputMultiline"))
        )
        question_desc_field.send_keys(Keys.CONTROL, "a")  # Select all text
        question_desc_field.send_keys(Keys.DELETE)
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_desc_field)
        time.sleep(0.5)
        question_desc_field.send_keys(random_description)


    # Method of Remove questions
    def click_on_delete_and_cancel_icon(self):
        self.driver.find_element(*self.delete_icon).click()
        time.sleep(1)
        self.driver.find_element(*self.cancel_button).click()
        time.sleep(1)


    # Method for search functionality
    def search_question_and_abbr_name(self):
        """Searches question name and abbreviation name from the first row, one after the other."""
        search_field_element = self.driver.find_element(*self.search_input)
        search_field_element.click()

        # Extract question name (column 2)
        question_name = self.driver.find_element(
            By.XPATH, "//table/tbody/tr[1]/td[2]"
        ).text.strip()

        if not question_name:
            raise ValueError("No question name found in the first row.")

        # Enter question name into the search field
        search_field_element.send_keys(question_name)
        time.sleep(2)

        # Click cross icon to clear search
        self.driver.find_element(*self.search_cross_icon).click()
        time.sleep(1)

        # Search abbreviation name
        abbr_name = self.driver.find_element(
            By.XPATH, "//table/tbody/tr[1]/td[4]"
        ).text.strip()

        if not abbr_name:
            raise ValueError("No abbreviation name found in the first row.")

        search_field_element = self.driver.find_element(*self.search_input)
        search_field_element.click()
        search_field_element.send_keys(abbr_name)
        time.sleep(2)

        # Clear again
        self.driver.find_element(*self.search_cross_icon).click()
        return question_name, abbr_name

    def search_with_random_text_and_check_no_results(self):
        """Enters random text in the search field and checks for 'No results found' message."""
        # Generate random search text
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=7))

        # Enter into search field
        search_field_element = self.driver.find_element(*self.search_input)
        search_field_element.click()
        search_field_element.send_keys(random_text)
        time.sleep(2)

        # Check for 'No results found' message
        try:
            no_result_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/table/tbody/tr/td/div/div/p")
            if no_result_element.is_displayed():
                print(f"Message displayed: 'No results found' for search '{random_text}'")
            else:
                print("No results found' message is not visible.")
        except:
            print("No results found' element not found. Maybe results are unexpectedly present.")

        self.driver.find_element(*self.search_cross_icon).click()


    def select_random_type_option(self):
        self.driver.find_element(*self.type_dropdown).click()
        time.sleep(1)
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

        self.driver.find_element(*self.type_cross_icon).click()
        time.sleep(1)

        print(f"Selected option: {selected_text} ")
        return selected_value


    # Methods for pagination
    def click_on_rows_per_page(self):
        self.driver.find_element(*self.rows_par_page).click()
        self.driver.find_element(*self.rows_par_20_page).click()
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