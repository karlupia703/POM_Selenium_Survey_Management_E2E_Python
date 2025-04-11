import random
import time
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SurveyPage:
    def __init__(self, driver):
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

    # Edit basic information
    name_input = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div/input"
    language_field = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[6]/div/div/div"
    select_language_edit = By.XPATH, "/html/body/div[3]/div[3]/ul/li[6]"
    survey_save_button = By.XPATH, "//html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/button"
    save_survey_dialog_box = By.XPATH, "/html/body/div[3]/div[3]/div/div[2]/button[2]"

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
    organization_list = By.XPATH, "/html/body/div[4]/div[3]"
    edit_icon = By.XPATH, "//tbody/tr[1]/td[6]/div[1]/a[1]/button[1]"

    # Selectors for edit setting
    survey_setting_tab = By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div"
    activity_toggle = By.XPATH, "/html/body/div[3]/div[3]/div/div/div[1]/label/span[1]"

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
            print("cancel button clicked")
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


    # Method of edit basic information of survey
    def click_on_survey_name_field(self):
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
        # actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        print("Checkboxes selected successfully")

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


    # Edit setting
    def click_on_Survey_setting_tab(self):
        self.driver.find_element(*self.survey_setting_tab).click()

    def click_on_edit_programs_dropdown(self):
        program_drop = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.programs_dropdown)
        )
        program_drop.click()

    def click_on_activity_toggle(self):
        self.driver.find_element(*self.activity_toggle).click()
