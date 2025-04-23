import os
import time
import pytest
from Page_Funcations.login_test import LoginTest
from Page_Funcations.survey_test import SurveyTest
from Config.config import Config

def test_setup_language():
        print(f"Running tests in language: {Config.language}")
        os.environ["TEST_LANGUAGE"] = Config.language

@pytest.fixture(scope="module")
def survey_test():
        print("Setting up login and survey test instance...")
        login_test = LoginTest()
        login_test.setup_method()
        login_test.test_login_user()
        time.sleep(4)
        print("User logged in successfully.")

        survey = SurveyTest()
        survey.driver = login_test.driver
        return survey

def test_create_survey(survey_test):
    survey_test.create_survey()
    print("Survey was successfully created with an empty template.")

def test_copy_survey_version(survey_test):
    survey_test.create_survey_copy_from_another_version()
    print("Copy from another version created successfully.")

def test_edit_survey_basic_information(survey_test):
    survey_test.edit_survey_basic_information()
    print("Survey updated successfully")

def test_open_version_and_edit_content(survey_test):
    survey_test.open_version_and_edit_content()
    print("Version updated successfully")

def test_create_multiple_questions(survey_test):
    survey_test.create_multiple_questions(count=2)
    print("Question created successfully")

def test_edit_question(survey_test):
    survey_test.edit_question()
    print("Survey version questions updated successfully")

def test_remove_question(survey_test):
    survey_test.remove_question()
    print("The question has been removed")

def test_handle_show_removed_questions(survey_test):
    survey_test.handle_show_removed_questions()
    print("The question has been restored")

def test_add_questions(survey_test):
    survey_test.add_questions()
    print("Survey version questions updated successfully")

def test_search_question_name(survey_test):
        survey_test.test_search_question_name()
        print("question search successfully")

def test_create_settings(survey_test):
        survey_test.create_settings()
        print("Configuration saved")

def test_edit_setting(survey_test):
        survey_test.edit_setting()
        print("Configuration updated")

def test_already_exist_survey(survey_test):
        survey_test.already_exist_survey()


print("All testcases are run successfully.")

