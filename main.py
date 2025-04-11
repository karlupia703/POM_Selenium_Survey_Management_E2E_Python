import os
import time
from Page_Funcations.login_test import LoginTest
from Page_Funcations.survey_test import SurveyTest
from Config.config import Config
class MainDriverClass:
    driver = None

    @classmethod
    def setup_language(cls):
        print(f"Running tests in language: {Config.language}")
        os.environ["TEST_LANGUAGE"] = Config.language

    @classmethod
    def run(cls):
        print("Starting main method...")
        # Initialize and execute login test
        login_test = LoginTest()
        login_test.setup_method()
        cls.driver = login_test.driver
        login_test.test_login_user()
        time.sleep(4)
        print("User logged in successfully.")
        time.sleep(4)
        if cls.driver is None:
            print("Error: WebDriver is not initialized. Exiting...")
            return

        # Initialize survey testcase
        survey_test = SurveyTest()
        # Run survey management tests
        survey_test.create_survey()
        survey_test.create_survey_copy_from_another_version()
        survey_test.edit_survey_basic_information()
        survey_test.open_version_and_edit_content()
        survey_test.create_settings()
        survey_test.edit_setting()
        survey_test.already_exist_survey()
        print("All testcases are run successfully.")

if __name__ == "__main__":
    MainDriverClass.setup_language()
    MainDriverClass.run()