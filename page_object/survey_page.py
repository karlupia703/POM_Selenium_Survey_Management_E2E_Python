
import random
import re
import time
from faker import Faker
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data.translations import Translations


def normalize_version_text(text):
    # Remove spaces, hyphens, parentheses, and make lowercase
    return re.sub(r'[\s\-\(\)]', '', text).lower()

def is_version_match(version_text, preview_text):
    return normalize_version_text(version_text) == normalize_version_text(preview_text)


class SurveyPage:
    def __init__(self, driver):
        self.faker = Faker()
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    # Selectors for create survey
    create_button = By.CSS_SELECTOR, "[data-test-id='btn-open-create-survey-dialog']"
    survey_name_input_field =By.CSS_SELECTOR,"[data-test-id=input-create-survey-name]"
    abbreviation_input_field = By.CSS_SELECTOR, "[data-test-id='input-create-survey-abbreviation']"
    category_dropdown_field = By.CSS_SELECTOR, "[data-test-id='select-create-survey-category']"
    SSTP_data =By.CSS_SELECTOR, "[data-test-id='text-create-survey-category-select-input-option-5fa59a04-45d0-4a09-90a8-de08325bc16b']"
    SSAC_data = By.CSS_SELECTOR, "[data-test-id='text-create-survey-category-select-input-option-bbe26d7a-e22f-4f2a-bf4d-09c4dfcf5c9b']"
    modality_dropdown_field = By.CSS_SELECTOR,"[data-test-id='select-create-survey-modality']"
    in_person = By.CSS_SELECTOR, "[data-test-id='text-create-survey-modality-select-input-option-in_person']"
    virtual = By.CSS_SELECTOR, "[data-test-id='text-create-survey-modality-select-input-option-virtual']"
    language_dropdown_field = By.CSS_SELECTOR, "[data-test-id='select-create-survey-language-display']"
    select_language_option_field = By.CSS_SELECTOR, "[data-test-id^='list-item-create-survey-language-option']"
    create_inside_button = By.CSS_SELECTOR, "[data-test-id='btn-submit-create-survey']"
    survey_cancel_btn = By.CSS_SELECTOR, "[data-test-id='btn-cancel-create-survey']"
    survey_tab = By.CSS_SELECTOR, "[data-test-id='text-navlink-surveys']"

    # Version options case
    empty_template = By.CSS_SELECTOR, "[data-test-id='title-create-survey-version-empty-template']"
    continue_button = By.CSS_SELECTOR, "[data-test-id='btn-continue-version-options']"
    version_name_input = By.CSS_SELECTOR, "[data-test-id='input-create-version-name']"
    version_abbreviation_input = By.CSS_SELECTOR, "[data-test-id='input-create-version-abbreviation']"
    accept_button = By.CSS_SELECTOR, "[data-test-id='btn-create-survey-version']"
    version_cancel_button = By.CSS_SELECTOR, "[data-test-id='btn-cancel-version-options']"
    version_empty_template_cancel_btn = By.CSS_SELECTOR, "[data-test-id='btn-cancel-create-survey-version']"

    # Copy from another version case
    new_version = By.CSS_SELECTOR, "[data-test-id='btn-open-create-new-version-dialog']"
    copy_from_another_version = By.CSS_SELECTOR, "[data-test-id='title-copy-survey-version']"
    continue_button_for_copy = By.CSS_SELECTOR, "[data-test-id='btn-continue-version-options']"
    survey_search_input = By.CSS_SELECTOR, "[data-test-id='survey-version-select-input']"
    radio_button = By.CSS_SELECTOR, "[data-test-id='checkbox-select-row-1']"
    no_surveys_msg = By.CSS_SELECTOR, "[data-test-id='no-data-title']"
    preview_question_message = By.CSS_SELECTOR, "[data-test-id='text-no-data-found-primary-message']"
    Version_copy_continue_btn = By.CSS_SELECTOR, "[data-test-id='btn-continue-copy-survey-version']"
    Version_name_input_field = By.CSS_SELECTOR, "[data-test-id='input-create-version-name']"
    Version_abbre_input_field = By.CSS_SELECTOR, "[data-test-id='input-create-version-abbreviation']"
    all_option = By.CSS_SELECTOR, "[data-test-id='create-version-option-all']"
    mandatory_status = By.CSS_SELECTOR, "[data-test-id='input-create-survey-version-mandatory']"
    accept_version_button = By.CSS_SELECTOR, "[data-test-id='btn-create-survey-version']"

    # Open version and edit information
    version_name_link = By.CSS_SELECTOR, "[data-test-id='link-navigate-to-survey-version-1']"
    edit_version_name_input = By.CSS_SELECTOR, "[data-test-id='input-version-information-name']"
    content_mandatory_button = By.CSS_SELECTOR, "[data-test-id='switch-survey-version-mandatory']"
    version_save_button = By.CSS_SELECTOR, "[data-test-id='btn-save-survey']"
    version_save_dialog_box = By.CSS_SELECTOR, "[data-test-id='btn-confirm-survey']"

    # Selectors for Questions
    question_tab = By.CSS_SELECTOR, "[data-test-id='tab-survey-version-questions']"
    create_question_btn = By.CSS_SELECTOR, "[data-test-id='btn-open-create-survey-question-dialog']"
    create_inside_ques_btn = By.CSS_SELECTOR, "[data-test-id='btn-create-survey-question']"
    question_type = By.CSS_SELECTOR, "[data-test-id='select-create-survey-question-question-type-display']"
    question_type_dropdown = By.CSS_SELECTOR, "[data-test-id='dropdown-create-survey-question-question-type-list']"
    abbreviation_question_field = By.CSS_SELECTOR, "[data-test-id='input-create-survey-question-abbreviation']"
    question_description = By.CSS_SELECTOR, "[data-test-id='input-create-survey-question-description']"
    save_question = By.CSS_SELECTOR, "[data-test-id='btn-save-survey']"
    save_dilog_btn = By.CSS_SELECTOR, "[data-test-id='btn-confirm-survey']"

    # Selectors for edit question
    edit_question_icon = By.CSS_SELECTOR, "[data-test-id='btn-edit-survey-question-row-1']"
    edit_question_save = By.CSS_SELECTOR, "[data-test-id='btn-edit-survey-question']"
    save_edit_dilog_btn = By.CSS_SELECTOR, "[data-test-id='btn-confirm-survey']"


    # Selectors for delete question
    remove_icon = By.CSS_SELECTOR, "[data-test-id='btn-delete-survey-question-row-1']"
    inside_remove_icon = By.CSS_SELECTOR, "[data-test-id='btn-confirm-survey-question-remove']"
    save_delete_question = By.CSS_SELECTOR, "[data-test-id='btn-save-survey']"
    save_dilog_delete_question = By.CSS_SELECTOR, "[data-test-id='btn-confirm-survey']"

    # Selectors for Add Questions
    add_icon = By.CSS_SELECTOR, "[data-test-id='btn-open-add-survey-question-dialog']"
    no_questions_found = By.CSS_SELECTOR, "[data-test-id='no-data-title']"
    cancel_add_question_page = By.CSS_SELECTOR, "[data-test-id='btn-sidedrawer-cancel-add-survey-question']"
    select_all_checkbox = By.CSS_SELECTOR, "[data-test-id='checkbox-select-all-rows']"
    add_question_btn = By.CSS_SELECTOR, "[data-test-id='btn-sidedrawer-add-survey-question']"


    # Selectors for Search question
    search_field = By.CSS_SELECTOR, "[data-test-id='search-filter-survey-question-filters']"
    search_cross_icon   = By.CSS_SELECTOR, "[data-test-id='btn-clear-survey-question-filters-search-input']"
    type_dropdown = By.CSS_SELECTOR, "[data-test-id='select-filter-type-survey-question-filters']"
    clear_filter = By.CSS_SELECTOR, "[data-test-id='btn-clear-survey-question-filters']"
    abbreviation_dropdown = By.CSS_SELECTOR, "[data-test-id='text-abbreviation-survey-question-filters-label']"
    show_remove = By.CSS_SELECTOR, "[data-test-id='switch-survey-question-show-deleted']"

    # Selectors of preview question
    preview_button = By.CSS_SELECTOR, "[data-test-id='btn-open-preview-modal']"
    preview_cross_button = By.CSS_SELECTOR, "[data-test-id='btn-close-preview-survey']"
    preview_no_question_msg = By.CSS_SELECTOR, "[data-test-id='text-no-data-found-primary-message']"

    # Selectors of restore question
    restore_button = By.CSS_SELECTOR, "[data-test-id='btn-restore-question-row-2']"
    restore_popup_button = By.CSS_SELECTOR, "[data-test-id='btn-confirm-restore-survey-question']"
    source  = By.CSS_SELECTOR, "[data-test-id='drag-handle-row-2']"
    target  = By.CSS_SELECTOR, "[data-test-id='drag-handle-row-1']"


    # Selectors for create setting
    settings_page_btn = By.CSS_SELECTOR, "[data-test-id='tab-survey-version-settings']"
    create_setting_btn = By.CSS_SELECTOR, "[data-test-id='btn-open-survey-setting-create-dialog']"
    programs_dropdown = By.CSS_SELECTOR, "[data-test-id='select-survey-settings-program-display']"
    language_dropdown = By.CSS_SELECTOR, "[data-test-id='select-survey-settings-language']"
    organization_dropdown = By.CSS_SELECTOR, "[data-test-id='select-survey-settings-organization-display']"
    save_setting_btn = By.CSS_SELECTOR, "[data-test-id='btn-create-survey-setting']"
    cancel_setting_btn = By.CSS_SELECTOR, "[data-test-id='btn-cancel-create-survey-setting']"
    language_options = By.CSS_SELECTOR, "[data-test-id='dropdown-survey-settings-language-list'] li"
    change_language_dropdown = By.CSS_SELECTOR, "[data-test-id='select-survey-settings-language-display']"
    edit_save_setting_btn = By.CSS_SELECTOR, "[data-test-id='btn-edit-survey-setting']"
    organization_options = By.CSS_SELECTOR, "[data-test-id='dropdown-survey-settings-organization-list'] li"
    language_or_organization_text = By.CSS_SELECTOR, "[data-test-id='helper-text']"

    # Selectors for edit setting
    survey_setting_tab = By.CSS_SELECTOR, "[data-test-id='text-survey-setting-label']"
    activity_toggle = By.CSS_SELECTOR, "[data-test-id='switch-survey-setting-state']"
    search_input_field = By.CSS_SELECTOR, "[data-test-id='input-search-survey-settings-program']"
    filled_checkbox = By.CSS_SELECTOR, "[data-testid='CheckBoxIcon']"
    blank_checkbox = By.CSS_SELECTOR, "[data-testid='CheckBoxOutlineBlankIcon']"


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
        options = self.driver.find_elements(*self.select_language_option_field)
        if options:
           random.shuffle(options)  # Shuffle to make selection more random
           selected_option = options[0]
           print("Selecting language:", selected_option.text)
           selected_option.click()
        else:
            print("No options available in the dropdown.")


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
            random.shuffle(options)
            selected_option = options[0]
            selected_option.click()
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
        self.driver.find_element(*self.edit_question_save).click()
        time.sleep(2)
        self.driver.find_element(*self.save_question).click()
        time.sleep(2)
        self.driver.find_element(*self.save_edit_dilog_btn).click()
        time.sleep(1)


    # Method of Remove questions
    def click_on_remove_icon(self):
        self.driver.find_element(*self.remove_icon).click()
        self.driver.find_element(*self.inside_remove_icon).click()

    def click_on_save_delete_question(self):
        self.driver.find_element(*self.save_delete_question).click()
        self.driver.find_element(*self.save_dilog_delete_question).click()



    # Method of show remove question
    def handle_show_removed_functionality(self):
        self.driver.find_element(*self.show_remove).click()
        time.sleep(2)
        self.driver.find_element(*self.restore_button).click()
        time.sleep(2)
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
            # Click the search field
            search_field_element = self.driver.find_element(*self.search_field)
            search_field_element.click()

            # Extract question name from first row
            question_name_element = self.driver.find_element(
                By.CSS_SELECTOR, "[data-test-id='text-survey-question-1-name']"
            )
            question_name = question_name_element.text.strip()
            if not question_name:
                raise ValueError("No question name found in the first row.")

            # Enter question name into the search field
            search_field_element.send_keys(question_name)
            time.sleep(2)

            return question_name

    def clear_search(self):
            """Clicks the cross icon to clear the search field."""
            cross_icon_element = self.driver.find_element(*self.search_cross_icon)
            cross_icon_element.click()
            time.sleep(1)

    # Method for search type option functionality
    def select_random_type_option(self):
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

        # Assertions Method to get the text of an element
    def get_element_text(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            print(f"Element with locator {locator} not found within the specified time.")
            return None

        # Method to assert  text
    def is_setting_helper_text(self, expected_text):
        return self.get_element_text(self.language_or_organization_text) == expected_text


    def click_on_language_dropdown(self):
        self.driver.find_element(*self.language_dropdown).click()
        options = self.driver.find_elements(*self.language_options)
        if options:
            random.shuffle(options)  # Shuffle to make selection more random
            selected_option = options[0]
            print("Selecting language:", selected_option.text)
            selected_option.click()
        else:
            print("No options available in the dropdown.")

    def click_on_organization_dropdown(self):
        self.driver.find_element(*self.organization_dropdown).click()
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.organization_options)
        )
        if options:
            random.shuffle(options)  # Shuffle to make selection more random
            selected_option = options[0]
            print("Selecting organization:", selected_option.text)
            selected_option.click()
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
            self.driver.find_element(*self.edit_save_setting_btn).click()
            time.sleep(1)

    def click_on_activity_toggle(self):
        self.driver.find_element(*self.activity_toggle).click()

    def assertTrue(self, is_selected, param):
        pass
















