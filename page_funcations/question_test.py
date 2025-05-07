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
from page_object.question_page import QuestionPage
from test_data.translations import Translations
from config.config import Config
from faker import Faker

class QuestionTest:
    def __init__(self):
        self.faker = Faker()
        self.driver = DriverManager.get_driver()
        self.question_page = QuestionPage(self.driver)


    def create_question_page(self):
        question_page = QuestionPage(self.driver)
        expected_texts = Translations.get_translation(Config.language)

        self.question_page.click_on_question_tab()
        time.sleep(2)
        self.question_page.click_on_create_question_button()
        time.sleep(2)
        self.question_page.click_on_question_inside_create_btn()
        time.sleep(2)

        assert question_page.is_create_question_title_text(expected_texts["createQuestionTitle"]), "Question title is mismatch"
        assert question_page.is_question_type_error_text(expected_texts["questionTypeError"]), "Question type error mismatch"
        assert question_page.is_abbreviation_name_error_text(expected_texts["abbreviationNameError"]), "Abbreviation name error mismatch"
        assert question_page.is_question_description_error_text(expected_texts["questionDescriptionError"]), "Question description error mismatch"
        print("all assertation is run successfully")

        self.question_page.click_on_question_type()
        time.sleep(2)
        self.question_page.click_on_abbreviation_question_field()
        time.sleep(1)
        self.question_page.enter_question_description()
        time.sleep(3)
        self.question_page.click_on_question_inside_create_btn()
        time.sleep(2)
        success_message = question_page.get_success_message1()
        print(f"Snackbar Text: {success_message}")

    def edit_question_page(self):
        question_page = QuestionPage(self.driver)
        expected_texts = Translations.get_translation(Config.language)

        self.question_page.click_on_edit_question_icon()
        time.sleep(2)
        assert question_page.is_edit_question_title_text(expected_texts["editTitle"]), "Edit title is  mismatch"

        self.question_page.edit_question_field()
        time.sleep(2)
        self.question_page.click_on_question_inside_create_btn()
        time.sleep(3)
        success_message = question_page.get_success_message_of_edit_question()
        print(f"Snackbar Text: {success_message}")

    def try_to_delete_question(self):
        question_page = QuestionPage(self.driver)
        expected_texts = Translations.get_translation(Config.language)

        self.question_page.click_on_delete_icon()
        time.sleep(1)
        assert question_page.is_delete_question_dialog_title_text(expected_texts["deleteDialogTitle"]), "Delete dialog text is mismatch"
        assert question_page.is_delete_question_dialog_body_text(expected_texts["deleteDialogBodyText"]), "Delete dialog body text is mismatch"
        self.question_page.click_on_cancel_button()
        time.sleep(1)


    def search_question_functionality(self):
        self.question_page.search_question_and_abbr_name()
        time.sleep(2)
        self.question_page.search_with_random_text_and_check_no_results()
        time.sleep(1)
        self.question_page.select_random_type_option()
        time.sleep(1)

    def question_pagination(self):
        self.question_page.click_on_question_tab()
        time.sleep(2)

        question_page = QuestionPage(self.driver)
        self.question_page.click_on_rows_per_page()
        time.sleep(2)
        if question_page.is_right_arrow_available():
            if question_page.is_right_arrow_enabled():
                print("Right pagination arrow is enabled.")
                question_page.click_right_arrow()
                time.sleep(3)
            else:
                print("Right pagination arrow is disabled.")
        else:
            print("Right pagination arrow is not available.")

        if question_page.is_left_arrow_available():
            if question_page.is_left_arrow_enabled():
                print("Left pagination arrow is enabled.")
                question_page.click_left_arrow()
                time.sleep(3)
            else:
                print("Left pagination arrow is disabled.")
        else:
            print("Left pagination arrow is not available.")