import string
import time
import random
from lib2to3.pgen2 import driver
import fake
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_funcations.driver_manager import DriverManager
from page_object.survey_page import SurveyPage
from config.config import Config
from faker import Faker
import unittest

class SurveyTest:
    def __init__(self):
        self.faker = Faker()
        self.driver = DriverManager.get_driver()
        self.survey_page = SurveyPage(self.driver)
        self.setting_page = SurveyPage(self.driver)
        self.question_page = SurveyPage(self.driver)

    def generate_alphanumeric_string(self, length=4):
        """Generate a random alphanumeric string (letters + digits)."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))

    def create_survey(self):
        """Execute the test for creating a survey."""
        self.survey_page.click_on_create_button()
        time.sleep(3)
        self.survey_page.enter_survey_name()
        time.sleep(1)
        self.survey_page.enter_abbreviation()
        time.sleep(1)
        self.survey_page.select_category()
        time.sleep(1)
        self.survey_page.select_modality()
        time.sleep(1)
        self.survey_page.select_language()
        time.sleep(1)
        self.survey_page.click_on_inside_create_button()
        time.sleep(1)
        try:
            already_exists_msg = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((
                    By.XPATH,
                    "//div[contains(@class, 'MuiStack-root') and (contains(., 'Same resource already exists') or contains(., 'El mismo recurso ya existe') or contains(., 'O mesmo recurso já existe'))]"
                ))
            )
            if already_exists_msg.is_displayed():
                print("Same resource already exists.")
                self.survey_page.click_on_survey_cancel_button()
                time.sleep(2)

        except TimeoutException:
            print("Toaster not found — proceeding with template creation.")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.survey_page.empty_template)
            ).click()
            time.sleep(4)
            self.survey_page.click_on_continue_button()
            time.sleep(2)
            self.survey_page.enter_version_name_input_field()
            time.sleep(2)
            self.survey_page.enter_version_abbreviation_name_input_field()
            time.sleep(1)
            self.survey_page.click_on_accept_button()
            time.sleep(1)
            try:
                already_exists_msg1 = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((
                        By.XPATH,
                        "//div[contains(@class, 'MuiStack-root') and (contains(., 'Same resource already exists') or contains(., 'El mismo recurso ya existe') or contains(., 'O mesmo recurso já existe'))]"
                    ))
                )
                if already_exists_msg1.is_displayed():
                    print("Same resource already exists for version.")
                    self.survey_page.click_on_version_empty_template_cancel_btn()
                    time.sleep(3)

            except TimeoutException:
                print("Toaster not found for version — proceeding with template creation.")

    def create_survey_copy_from_another_version(self):
        """Execute the test for creating a survey with copy from another version."""
        self.survey_page.click_on_new_version()
        time.sleep(2)
        self.survey_page.click_on_copy_from_another_version()
        time.sleep(2)
        self.survey_page.click_on_continue_button_copy()
        time.sleep(4)
        self.survey_page.click_on_survey_search_field()
        time.sleep(2)
        self.survey_page.question_preview()
        time.sleep(2)
        self.survey_page.click_on_version_popup_continue_btn()
        time.sleep(2)
        self.survey_page.enter_version_name()
        time.sleep(2)
        self.survey_page.enter_Abbreviation_name()
        time.sleep(2)
        self.survey_page.click_on_all_option()
        time.sleep(2)
        self.survey_page.click_on_mandatory_status()
        time.sleep(2)
        self.survey_page.click_on_version_accept_button()
        time.sleep(2)

    def open_version_and_edit_content(self):
        """Execute the test of open version and edit the basic information"""
        self.survey_page.click_on_version_name_link()
        time.sleep(2)
        self.survey_page.edit_version_name()
        time.sleep(2)
        self.survey_page.click_on_version_mandatory_link()
        time.sleep(2)
        self.survey_page.click_on_version_save_btn()
        time.sleep(3)
        self.survey_page.click_on_version_save_dialog_box()
        time.sleep(3)

    def create_question(self):
        self.question_page.click_on_question_tab()
        time.sleep(2)
        self.question_page.click_on_create_question_button()
        time.sleep(2)
        self.question_page.click_on_question_inside_create_btn()
        time.sleep(2)
        self.question_page.click_on_question_type()
        time.sleep(2)
        self.question_page.click_on_abbreviation_question_field()
        time.sleep(1)
        self.question_page.enter_question_description()
        time.sleep(3)
        self.question_page.click_on_question_inside_create_btn()
        time.sleep(2)
        self.question_page.click_on_save_question()
        time.sleep(2)

    def create_multiple_questions(self, count=2):
        for i in range(count):
            self.create_question()
            print(f"Question {i + 1} created and saved successfully.")


    def edit_question(self):
        self.question_page.click_on_edit_question_icon()
        time.sleep(2)
        self.question_page.edit_question_field()
        time.sleep(2)
        self.question_page.click_on_question_inside_create_btn()
        time.sleep(3)
        self.question_page.click_on_save_edit_question()
        time.sleep(2)
        print("Question updated successfully.")

    def remove_question(self):
        self.question_page.click_on_remove_icon()
        time.sleep(2)
        self.question_page.click_on_save_edit_question()
        time.sleep(2)
        print("The question has been removed.")

    def handle_show_removed_questions(self):
        self.question_page.handle_show_removed_functionality()
        time.sleep(3)

    def add_questions(self):
        self.question_page.handle_add_question_flow()
        time.sleep(2)
        print("Question added successfully")

    def test_search_question_name(self):
        self.question_page.search_question_name_from_first_row()
        try:
            question_name = self.question_page.search_question_name_from_first_row()
            print(f"Searched for question name: {question_name}")
            self.question_page.clear_search()
        except NoSuchElementException as e:
            print(f"Error during search: {e}")

        self.question_page.select_random_type_option()
        time.sleep(2)

    def handle_preview_case(self):
        self.question_page.click_on_preview_and_cross_button()

    def create_settings(self):
        self.setting_page.click_on_setting_page()
        time.sleep(2)
        self.setting_page.click_on_setting_create_btn()
        time.sleep(2)
        self.setting_page.click_on_programs_dropdown_field()
        time.sleep(3)
        self.setting_page.click_on_language_dropdown()
        time.sleep(3)
        self.setting_page.click_on_organization_dropdown()
        time.sleep(2)
        self.setting_page.click_on_setting_save_btn()
        time.sleep(2)
        print("Setting created successfully")

    def edit_setting(self):
        self.setting_page.click_on_Survey_setting_tab()
        time.sleep(3)
        self.setting_page.edit_programs_dropdown()
        time.sleep(3)
        self.setting_page.edit_change_language()
        time.sleep(5)
        print("Configuration saved successfully")

        # Change the status of activity
        self.setting_page.click_on_Survey_setting_tab()
        time.sleep(3)
        self.setting_page.click_on_activity_toggle()
        time.sleep(3)
        print("Status change successfully")

    def already_exist_survey(self):
        survey_page = SurveyPage(self.driver)
        # Generate fixed names
        alphanumeric_suffix = self.generate_alphanumeric_string(4)
        survey_name = f"Survey{alphanumeric_suffix}"
        abbrev_name = f"Abbrev{alphanumeric_suffix}"
        # For redirect into survey home page
        survey_page.click_on_survey_tab()
        time.sleep(2)
        survey_page.click_on_create_button()
        time.sleep(2)
        survey_page.fill_user_details(survey_name, abbrev_name)
        time.sleep(2)
        survey_page.select_category()
        survey_page.select_modality()
        survey_page.select_language()
        survey_page.click_on_inside_create_button()
        time.sleep(3)
        survey_page.click_on_version_cancel_button()
        time.sleep(3)
        survey_page.click_on_survey_tab()
        time.sleep(2)

        # Attempt duplicate
        survey_page.click_on_create_button()
        survey_page.fill_user_details(survey_name, abbrev_name)
        survey_page.select_category()
        survey_page.select_modality()
        survey_page.select_language()
        survey_page.click_on_inside_create_button()
        time.sleep(2)
        try:
            already_exists_msg = self.driver.find_element(
                 By.XPATH,
                 "//div[contains(@class, 'MuiStack-root') and (contains(., 'Same resource already exists') or contains(., 'El mismo recurso ya existe') or contains(., 'O mesmo recurso já existe'))]"
            )
            if already_exists_msg.is_displayed():
                print("Same resource already exists.")
            else:
                print("Survey creation validation failed: duplicate name allowed.")
        except:
            print("Validation message for duplicate survey not found!")
        survey_page.click_on_survey_cancel_button()
        time.sleep(3)



