import os
import time
import pytest
from page_funcations.login_test import LoginTest
from page_funcations.survey_dashboard_test import SurveyDashboardTest
from page_funcations.survey_test import SurveyTest
from page_funcations.question_test import QuestionTest
from config.config import Config

class SurveyFixture:
    def __init__(self, survey, dashboard,questions):
        self.survey = survey
        self.dashboard = dashboard
        self.questions = questions

def test_setup_language():
    print(f"Running tests in language: {Config.language}")
    os.environ["TEST_LANGUAGE"] = Config.language

@pytest.fixture(scope="module")
def survey_test():
    login_test = LoginTest()
    login_test.setup_method()
    login_test.test_login_user()
    time.sleep(4)
    print("User logged in successfully.")

    # Create and share driver
    survey = SurveyTest()
    survey.driver = login_test.driver

    surveyDashboard = SurveyDashboardTest()
    surveyDashboard.driver = login_test.driver

    questions = QuestionTest()
    questions.driver = login_test.driver
    return SurveyFixture(survey, surveyDashboard,questions )


# # # Run survey functionality
def test_create_survey(survey_test):
    survey_test.survey.create_survey()
    print("Survey was successfully created with an empty template.")

def test_copy_survey_version(survey_test):
    survey_test.survey.create_survey_copy_from_another_version()
    print("Copy from another version created successfully.")

def test_open_version_and_edit_content(survey_test):
    survey_test.survey.open_version_and_edit_content()
    print("Version updated successfully")

def test_create_multiple_questions(survey_test):
    survey_test.survey.create_multiple_questions(count=2)
    print("Question created successfully")

def test_edit_question(survey_test):
    survey_test.survey.edit_question()
    print("Survey version questions updated successfully")

def test_remove_question(survey_test):
    survey_test.survey.remove_question()
    print("The question has been removed")

def test_handle_show_removed_questions(survey_test):
    survey_test.survey.handle_show_removed_questions()
    print("The question has been restored")

def test_add_questions(survey_test):
    survey_test.survey.add_questions()
    print("Survey version questions updated successfully")

def test_preview_question(survey_test):
    survey_test.survey.handle_preview_case()
    print("Question preview successfully")

def test_search_question_name(survey_test):
    survey_test.survey.test_search_question_name()
    print("question search successfully")

def test_create_settings(survey_test):
    survey_test.survey.create_settings()
    print("Configuration saved")

def test_edit_setting(survey_test):
    survey_test.survey.edit_setting()
    print("Configuration updated")

def test_already_exist_survey(survey_test):
    survey_test.survey.already_exist_survey()


# Run dashboard testcase
def test_search_survey_name(survey_test):
    survey_test.dashboard.search_survey_functionality()
    print("Survey search successfully")

def test_view_survey_information(survey_test):
    survey_test.dashboard.view_survey()
    print ("survey view successfully")

def test_edit_survey_basic_information(survey_test):
    survey_test.dashboard.edit_survey_basic_information()
    print("Survey updated successfully")

def test_dashboard_pagination(survey_test):
    survey_test.dashboard.test_pagination()
    print("Pagination is working successfully")


# Run Question page functionality
def test_create_questions(survey_test):
    survey_test.questions.create_question_page()
    print("Question create successfully.")

def test_edit_question_page(survey_test):
    survey_test.questions.edit_question_page()
    # print("Question updated successfully.")

def test_delete_question(survey_test):
    survey_test.questions.try_to_delete_question()
    print("Are you sure you want to delete this question?")

def test_search_questions(survey_test):
    survey_test.questions.search_question_functionality()

def test_question_pagination(survey_test):
    survey_test.questions.question_pagination()