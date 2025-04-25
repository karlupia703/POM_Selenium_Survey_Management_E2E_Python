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
from Page_Funcations.driver_manager import DriverManager
from Page_Object.survey_page import SurveyPage
from Page_Object.question_page import QuestionPage
from Config.config import Config
from faker import Faker

class QuestionTest:
    def __init__(self):
        self.faker = Faker()
        self.driver = DriverManager.get_driver()
        self.question_page = QuestionPage(self.driver)


    def create_question_page(self):
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

    def edit_question_page(self):
        self.question_page.click_on_edit_question_icon()
        time.sleep(2)
        self.question_page.edit_question_field()
        time.sleep(2)
        self.question_page.click_on_question_inside_create_btn()
        time.sleep(3)

    def try_to_delete_question(self):
        self.question_page.click_on_delete_and_cancel_icon()

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