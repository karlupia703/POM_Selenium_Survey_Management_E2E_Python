import logging
import random
import re
import string
import time
import datetime
from re import search
import fake
from faker import Faker
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from config.config import Config
from test_data.translations import Translations


def normalize_version_text(text):
    # Remove spaces, hyphens, parentheses, and make lowercase
    return re.sub(r'[\s\-\(\)]', '', text).lower()

def is_version_match(version_text, preview_text):
    return normalize_version_text(version_text) == normalize_version_text(preview_text)


class SurveyPage:
    def __init__(self, driver):
        # self.faker = None
        self.faker = Faker()
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Selectors for create survey
    create_button = By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div[1]/button"
    survey_name_input_field = By.XPATH,"/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div/input"
    abbreviation_input_field = By.XPATH,"/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/div/input"
    category_dropdown_field = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[3]/div/div"
    SSTP_data = By.XPATH, "/html/body/div[4]/div[3]/ul/li[1]"
    SSAC_data = By.XPATH, "/html/body/div[4]/div[3]/ul/li[2]"
    modality_dropdown_field = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[4]/div/div/div"
    in_person = By.XPATH, "/html/body/div[4]/div[3]/ul/li[1]"
    virtual = By.XPATH, "/html/body/div[4]/div[3]/ul/li[2]"
    language_dropdown_field = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[5]/div/div/div"
    select_language_field = By.XPATH, "/html/body/div[4]/div[3]"
    create_inside_button = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"
    survey_cancel_btn = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[1]"
    survey_tab = By.XPATH, "/html/body/div[1]/div/div/div[1]/div/nav/a[1]/div/div[2]/span"

    # Version options case
    empty_template = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/span"
    continue_button = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"
    version_name_input = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div/input"
    version_abbreviation_input = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/div/input"
    accept_button = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[3]"
    version_cancel_button = By.XPATH, "/html/body/div[4]/div[3]/div/div[2]/button[1]"
    version_empty_template_cancel_btn = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"

    # Copy from another version case
    new_version = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/button"
    copy_from_another_version = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/span"
    continue_button_for_copy = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"
    survey_search_input = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div[1]/div/div"
    radio_button = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/table/tbody/tr/td[1]/span/input"
    no_surveys_msg = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div[3]/div/table/tbody/tr/td/div/div/p"
    preview_question_message = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/div[2]/div/div/div/span[1]"
    Version_copy_continue_btn = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[3]"
    Version_name_input_field = By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/div/div[1]/div/div/input"
    Version_abbre_input_field = By.XPATH,"/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div/div/input"
    all_option = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[3]/fieldset/div/label[3]/span[1]/input"
    mandatory_status = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[4]/label/span[1]/span[1]"
    accept_version_button = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[3]"

    # Open version and edit information
    version_name_link = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[2]/a"
    edit_version_name_input = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/input"
    content_mandatory_button = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/label/span[1]/span[1]"
    version_save_button = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/button[2]"
    version_save_dialog_box = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"

    # Selectors for create setting
    settings_page_btn = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/button[3]"
    create_setting_btn = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/div/div/div[1]/button"
    programs_dropdown = By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div[1]/div/div/div/div"
    language_dropdown = By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div[2]/div/div/div"
    organization_dropdown = By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div[3]/div/div/div"
    save_setting_btn = By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]/button[2]"
    cancel_setting_btn = By.XPATH, "/html/body/div[3]/div[3]/div/div/div[3]/button[2]"
    language_options = By.XPATH, "/html/body/div[4]/div[3]"
    change_language_dropdown = By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div[2]/div/div/div"
    organization_list = By.XPATH, "/html/body/div[4]/div[3]"
    edit_icon = By.XPATH, "//tbody/tr[1]/td[6]/div[1]/a[1]/button[1]"

    # Selectors for edit setting
    survey_setting_tab = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div"
    activity_toggle = By.XPATH, "/html/body/div[3]/div[3]/div/div/div[1]/label/span[1]"
    search_input_field = By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/div/input"
    filled_checkbox = By.CSS_SELECTOR, "[data-testid='CheckBoxIcon']"
    blank_checkbox = By.CSS_SELECTOR, "[data-testid='CheckBoxOutlineBlankIcon']"

    # Selectors for Questions
    question_tab = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/button[2]"
    create_question_btn = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div/button[2]"
    create_inside_ques_btn = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"
    question_type = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[1]/div/div"
    question_type_dropdown = By.XPATH, "/html/body/div[4]/div[3]/ul"
    abbreviation_question_field = By.XPATH,"/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/div/input"
    question_description = By.XPATH, "/html/body/div[3]/div[3]/div/div[1]/div/div[3]/div/div"
    save_question = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/button[2]"
    save_dilog_btn = By.XPATH, "/html/body/div[4]/div[3]/div/div[2]/button[2]"
    save_edit_dilog_btn = By.CSS_SELECTOR, ".MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-colorPrimary.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.MuiButton-colorPrimary.confirmation-modal_confirm-button__lZBTH.css-ger89v"

    # Selectors for edit question
    edit_question_icon = By.XPATH, "//tbody/tr[1]/td[8]/div[1]/button[1]"

    # Selectors for delete question
    remove_icon = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[8]/div/button[2]"
    inside_remove_icon = By.XPATH, "(//button[normalize-space()='Remove'] | //button[normalize-space()='Eliminar'] | //button[normalize-space()='Remover'])[1]"

    # Selectors for Add Questions
    add_icon = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div/button[1]"
    no_questions_found = By.XPATH, "//p[contains(@class, 'MuiTypography-noWrap') and (normalize-space(text())='No questions found' or normalize-space(text())='No se ha encontrado ninguna pregunta' or normalize-space(text())='Nenhuma pergunta encontrada')]"
    cancel_add_question_page = By.XPATH, "//button[(normalize-space(text())='Cancel' or normalize-space(text())='Cancelar') and contains(@class, 'MuiButton-root')]"
    select_all_checkbox = By.XPATH, "//input[@aria-label='Select all' or @aria-label='Seleccionar todo' or @aria-label='Selecionar tudo']"
    add_question_btn = By.XPATH, "//button[normalize-space(text())='Add' or normalize-space(text())='Agregar' or normalize-space(text())='Adicionar']"

    # Selectors for Search question
    search_field = By.XPATH, "//*[@id='simple-tabpanel-1']/div/div/div[1]/div/div[1]/div/div[1]/input"
    question_name = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[2]"
    search_cross_icon   = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/div/div[1]/div[2]/button"
    type_dropdown = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/div/div[2]/div[1]"
    clear_filter = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/div/div[2]/button"
    table_body = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div"
    abbreviation_dropdown = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/span"
    input = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/span/p"
    show_remove = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div[2]/label/span[2]"
    full_table = By.XPATH, "/table/tbody/div"

    # Selectors of preview question
    preview_button = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/button[1]"
    preview_cross_button = By.XPATH, "//button[@aria-label='close']"
    preview_no_question_msg = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/div/div/div/span[1]"
    dashboard_edit_icon = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[6]/div/a/button"

    # Selectors of restore question
    restore_button = By.XPATH, "//tbody/tr[2]/td[8]/div[1]/button[1]//*[name()='svg']"
    restore_popup_button = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"
    source  = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[1]"
    target  = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[1]"


    def select_random_abbreviation(self):
        self.driver.find_element(*self.abbreviation_dropdown).click()

    def generate_random_description(self, sentences=2):
        return self.faker.paragraph(nb_sentences=sentences)

    # method for create survey
    def click_on_create_button(self):
        self.driver.find_element(*self.create_button).click()

    def generate_random_string(self, length=3):
        """Generate a random string of digits with the given length."""
        characters = "0123456789"
        return ''.join(random.choices(characters, k=length))

    def enter_survey_name(self):
        survey_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.survey_name_input_field)
        )
        survey_name = "Survey" + self.generate_random_string(4)
        survey_input.send_keys(survey_name)
        print(f"Survey created with name: {survey_name}")

    def enter_abbreviation(self):
        abbreviation_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.abbreviation_input_field)
        )
        abbreviation = "Abbre" + self.generate_random_string(3)
        abbreviation_input.send_keys(abbreviation)
        print(f"Survey abbreviation created with name: {abbreviation}")

    def select_category(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.category_dropdown_field)
        )
        dropdown.click()
        # Randomly select SSTP or SSAC
        selected_option = random.choice([self.SSTP_data, self.SSAC_data])
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(selected_option)
        ).click()

    def select_modality(self):
        self.driver.find_element(*self.modality_dropdown_field).click()
        self.driver.find_element(*self.in_person).click()
        self.driver.find_element(*self.virtual).click()
        self.driver.find_element(By.TAG_NAME, "body").click()

    def select_language(self):
        self.driver.find_element(*self.language_dropdown_field).click()
        self.driver.find_element(*self.select_language_field).click()

    def click_on_inside_create_button(self):
        self.driver.find_element(*self.create_inside_button).click()

    def click_on_survey_cancel_button(self):
        self.driver.find_element(*self.survey_cancel_btn).click()

    def click_on_survey_tab(self):
        self.driver.find_element(*self.survey_tab).click()


    # method of empty version create
    def click_on_empty_template(self):
        self.driver.find_element(*self.empty_template).click()

    def click_on_continue_button(self):
        self.driver.find_element(*self.continue_button).click()

    def click_on_version_cancel_button(self):
        try:
            cancel_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.version_cancel_button)
            )
            cancel_btn.click()
        except TimeoutException:
            print("Cancel button not found or not clickable.")

    def click_on_version_empty_template_cancel_btn(self):
            cancel_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.version_empty_template_cancel_btn)
            )
            cancel_btn.click()

    def enter_version_name_input_field(self):
        version_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.version_name_input)
        )
        version_name = "Version" + self.generate_random_string(3)
        version_input.send_keys(version_name)
        print(f"Abbreviation created with name: {version_name}")

    def enter_version_abbreviation_name_input_field(self):
        version_abber_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.version_abbreviation_input)
        )
        version_abber_name = "VerAb" + self.generate_random_string(3)
        version_abber_input.send_keys(version_abber_name)
        print(f"Version abbreviation created with name: {version_abber_name}")

    def click_on_accept_button(self):
        self.driver.find_element(*self.accept_button).click()

    def click_on_new_version(self):
        self.driver.find_element(*self.new_version).click()


    # method of copy from another version
    def click_on_copy_from_another_version(self):
        self.driver.find_element(*self.copy_from_another_version).click()

    def click_on_continue_button_copy(self):
        self.driver.find_element(*self.continue_button_for_copy).click()

    def click_on_survey_search_field(self):
        search_input = self.driver.find_element(*self.survey_search_input)
        search_input.click()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(2)
        try:
            radio_button = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.radio_button)
            )
            radio_button.click()
        except:
            try:
                no_surveys_msg = self.driver.find_element(*self.no_surveys_msg)
                message_text = no_surveys_msg.text.strip()
                expected_messages = ["No surveys found", "No se encontraron encuestas", "Nenhuma pesquisa encontrada"]  # Add more languages here
                if message_text in expected_messages:
                    print("No surveys found. Trying next option...")

               # Re-opn dropdown and try to next item
                search_input.click()
                time.sleep(2)
                ActionChains(self.driver).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
                time.sleep(2)

                # Try again to find and click radio button
                radio_button = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located(self.radio_button)
                )
                radio_button.click()
                print("Radio button clicked after reattempt")
            except Exception as e:
                print("Unexpected issue: Neither radio button nor 'No surveys found' message was found.")
                print("Error:", str(e))

    def question_preview(self):
        try:
            no_preview_question_msg = self.driver.find_element(*self.preview_question_message)
            message_text = no_preview_question_msg.text.strip()
            expected_messages = ["This survey has no questions yet", "Esta encuesta aún no tiene preguntas", "Nenhuma pesquisa selecionada"]  # Add more languages here
            if message_text in expected_messages:
                print("This survey has no questions yet")
        except:
            print("Questions are available.")

    def click_on_version_popup_continue_btn(self):
        self.driver.find_element(*self.Version_copy_continue_btn).click()

    def enter_version_name(self):
        version_input = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.version_name_input)
        )
        version_input_name = "Version" + self.generate_random_string(3)
        version_input.send_keys(version_input_name)
        print(f"Version created with name: {version_input_name}")

    def enter_Abbreviation_name(self):
        Abbreviation_input = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.version_abbreviation_input)
        )
        Abbreviation_input_name = "Abbr" + self.generate_random_string(4)
        Abbreviation_input.send_keys(Abbreviation_input_name)
        print(f"Abbreviation created with name: {Abbreviation_input_name}")

    def click_on_all_option(self):
        self.driver.find_element(*self.all_option).click()

    def click_on_mandatory_status(self):
        self.driver.find_element(*self.mandatory_status).click()

    def click_on_version_accept_button(self):
        self.driver.find_element(*self.accept_version_button).click()


    # Method for Open version and edit information
    def click_on_version_name_link(self):
        self.driver.find_element(*self.version_name_link).click()

    def edit_version_name(self):
        version_name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.edit_version_name_input)
        )
        version_name_field.click()
        # Clear the field properly
        version_name_field.send_keys(Keys.CONTROL, "a")  # Select all text
        version_name_field.send_keys(Keys.DELETE)
        time.sleep(1)
        version_name = "Edit version" + self.generate_random_string(3)
        version_name_field.send_keys(version_name)
        print(f"Edited version name created with name: {version_name}")

    def click_on_version_mandatory_link(self):
        self.driver.find_element(*self.content_mandatory_button).click()

    def click_on_version_save_btn(self):
        self.driver.find_element(*self.version_save_button).click()

    def click_on_version_save_dialog_box(self):
        self.driver.find_element(*self.version_save_dialog_box).click()


    # Methods for already survey exist
    def click_create_button_already(self):
        self.wait.until(EC.element_to_be_clickable(self.create_button)).click()

    def fill_user_details(self, survey_name, abbre_name):
        self.wait.until(EC.visibility_of_element_located(self.survey_name_input_field)).send_keys(survey_name)
        self.wait.until(EC.visibility_of_element_located(self.abbreviation_input_field)).send_keys(abbre_name)


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
        print(f"Survey abbreviation created with name: {abbreviation}")

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

    def click_on_save_question(self):
        self.driver.find_element(*self.save_question).click()
        time.sleep(1)
        self.driver.find_element(*self.save_dilog_btn).click()
        time.sleep(1)


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


    def click_on_save_edit_question(self):
        self.driver.find_element(*self.save_question).click()
        time.sleep(2)
        self.driver.find_element(*self.save_edit_dilog_btn).click()
        time.sleep(1)


    # Method of Remove questions
    def click_on_remove_icon(self):
        self.driver.find_element(*self.remove_icon).click()
        self.driver.find_element(*self.inside_remove_icon).click()


    # Method of show remove question
    def handle_show_removed_functionality(self):
        self.driver.find_element(*self.show_remove).click()
        time.sleep(2)
        self.driver.find_element(*self.restore_button).click()
        time.sleep(1)
        self.driver.find_element(*self.restore_popup_button).click()
        time.sleep(2)

        # locate your elements
        source_row = self.driver.find_element(*self.source)
        target_row = self.driver.find_element(*self.target)

        # Perform drag and drop
        actions = ActionChains(self.driver)
        actions.click_and_hold(source_row).pause(1)
        actions.click_and_hold(source_row).move_to_element(target_row).release().perform()
        time.sleep(2)

        #common save button
        self.driver.find_element(*self.save_question).click()
        time.sleep(2)
        # save questions
        self.driver.find_element(*self.save_edit_dilog_btn).click()
        time.sleep(1)


    # Method for Add questions
    def handle_add_question_flow(self):
        self.driver.find_element(*self.add_icon).click()
        time.sleep(2)

        try:
            no_question_found_msg = self.driver.find_element(*self.no_questions_found)
            raw_text = no_question_found_msg.text
            message_text = raw_text.strip()
            print(f"Detected message: '{message_text}'")

            expected_messages = [
                "No questions found",
                "No se ha encontrado ninguna pregunta",
                "Nenhuma pergunta encontrada"
            ]

            if any(msg in message_text for msg in expected_messages):
            # if message_text in expected_messages:
                print("No questions found.")
                cancel_btn = self.driver.find_element(*self.cancel_add_question_page)
                cancel_btn.click()
                print("Clicked on cancel button.")
                return
        except:
            print("No 'no questions found' message, assuming questions are available.")

        # Step 3: Questions are available — select all and add
        self.driver.find_element(*self.select_all_checkbox).click()
        time.sleep(2)
        add_btn = self.driver.find_element(*self.add_question_btn)
        add_btn.click()
        self.driver.find_element(*self.save_question).click()
        time.sleep(2)
        self.driver.find_element(*self.save_edit_dilog_btn).click()
        time.sleep(1)


    # Method for search functionality
    def search_question_name_from_first_row(self):
            """Clicks search field, gets question name from first row, and performs search."""
            # Click the search field
            search_field_element = self.driver.find_element(*self.search_field)
            search_field_element.click()

            # Extract question name from first row
            question_name_element = self.driver.find_element(
                By.XPATH,
                "//table/tbody/tr[1]/td[2]/div"
            )
            question_name = question_name_element.text.strip()
            if not question_name:
                raise ValueError("No question name found in the first row.")

            # Enter question name into the search field
            search_field_element.send_keys(question_name)
            time.sleep(2)  # replace with explicit wait if needed

            return question_name

    def clear_search(self):
            """Clicks the cross icon to clear the search field."""
            cross_icon_element = self.driver.find_element(*self.search_cross_icon)
            cross_icon_element.click()
            time.sleep(1)

    # Method for search type option functionality
    def select_random_type_option(self):
            # Open the dropdown
            self.driver.find_element(*self.type_dropdown).click()
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
            # Click the selected option
            random_option.click()
            self.driver.find_element(*self.clear_filter).click()
            print(f"Selected option: {selected_text} ")
            return selected_value


    # Method for preview question
    def click_on_preview_and_cross_button(self):
        self.driver.find_element(*self.preview_button).click()
        time.sleep(1)
        try:
            no_preview_question_msg = self.driver.find_element(*self.preview_no_question_msg)
            message_text = no_preview_question_msg.text.strip()
            expected_messages = [
                "This survey has no questions yet",
                "Esta encuesta aún no tiene preguntas",
                "Esta pesquisa ainda não tem perguntas"
            ]
            if message_text in expected_messages:
                print("This survey has no questions yet")
                self.driver.find_element(*self.preview_cross_button).click()
                return

        except:
            print("Questions are available.")
            version_text = self.driver.find_element(By.CSS_SELECTOR, '.css-qswjcr').text
            preview_text = self.driver.find_element(By.CSS_SELECTOR, '.css-7g74ke').text

            print("Version Page Text: ", version_text)
            print("Preview Page Text:", preview_text)

            if is_version_match(version_text, preview_text):
                print("Version name matches!")
            else:
                print("Version name does not match.")
        self.driver.find_element(*self.preview_cross_button).click()
        time.sleep(1)


    # Method for create settings
    def click_on_edit_icon(self):
        self.driver.find_element(*self.edit_icon).click()

    def click_on_setting_page(self):
        self.driver.find_element(*self.settings_page_btn).click()

    def click_on_setting_create_btn(self):
        self.driver.find_element(*self.create_setting_btn).click()

    def click_on_programs_dropdown_field(self):
        program_drop = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.programs_dropdown)
        )
        program_drop.click()
        time.sleep(3)

        actions = ActionChains(self.driver)
        for _ in range(3):  # Select 3 options
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(3)

        parent_element = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div[1]/div/div/div/div")
        # Move to the parent element, offset by -10px in both directions, and click
        ActionChains(self.driver).move_to_element_with_offset(parent_element, -10, -10).click().perform()

    def click_on_language_dropdown(self):
        self.driver.find_element(*self.language_dropdown).click()
        options = self.driver.find_elements(*self.language_options)
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No options available in the dropdown.")

    def click_on_organization_dropdown(self):
        self.driver.find_element(*self.organization_dropdown).click()
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.organization_list)
        )
        if options:
            random_option = random.choice(options)
            random_option.click()
        else:
            print("No organization list in the dropdown.")

    def click_on_setting_save_btn(self):
        self.driver.find_element(*self.save_setting_btn).click()


    # Method for edit setting
    def click_on_Survey_setting_tab(self):
        self.driver.find_element(*self.survey_setting_tab).click()

    def click_on_edit_programs_dropdown(self):
        program_drop = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.programs_dropdown)
        )
        program_drop.click()


    # Method for search program
    def edit_programs_dropdown(self, cls=None):
            self.driver.find_element(*self.programs_dropdown).click()

            search = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.search_input_field)
            )
            search.click()
            time.sleep(0.5)

            # ← correct call here
            term = Translations.current_search_term()
            print(f"[DEBUG] Using search term: {term!r}")
            search.send_keys(term, Keys.ENTER)
            time.sleep(1)

            try:
                checkbox_filled = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='CheckBoxIcon']"))
                )
                if checkbox_filled.is_selected():
                    print(f"✅ Program 'Graphic Design' checkbox is filled (selected).")
            except NoSuchElementException:
                # If the filled checkbox is not found, check for the empty one
                try:
                    checkbox_empty = WebDriverWait(self.driver, 5).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='CheckBoxOutlineBlankIcon']"))
                    )
                    if checkbox_empty.is_selected():
                        print(f"⬜ Program 'Graphic Design' checkbox is empty (unselected).")
                except NoSuchElementException:
                    print("⬜ Both checkboxes not found!")

            # Click outside to close dropdown
            parent_element = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div/div[2]/div[1]/div/div/div/div")
            ActionChains(self.driver).move_to_element_with_offset(parent_element, -10, -10).click().perform()


    def edit_change_language(self):
            self.driver.find_element(*self.change_language_dropdown).click()
            options = self.driver.find_elements(*self.language_options)
            if options:
                random_option = random.choice(options)
                random_option.click()
            else:
                print("No options available in the dropdown.")
            time.sleep(3)
            self.driver.find_element(*self.save_setting_btn).click()
            time.sleep(1)

    def click_on_activity_toggle(self):
        self.driver.find_element(*self.activity_toggle).click()

    def assertTrue(self, is_selected, param):
        pass
















