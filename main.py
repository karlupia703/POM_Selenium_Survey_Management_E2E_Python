import os
import time
from Page_Funcations.login_test import LoginTest
from Config.config import Config
class MainDriverClass:
    driver = None

    @classmethod
    def setup_language(cls):
        print(f"Running tests in language: {Config.language}")
        os.environ["TEST_LANGUAGE"] = Config.language

    @classmethod
    def run(cls):
        # Main method to execute tests.
        print("Starting main method...")
        # Initialize and execute login test
        login_test = LoginTest()
        login_test.setup_method()
        cls.driver = login_test.driver
        login_test.test_login_user()
        time.sleep(4)
        print("User logged in successfully.")
        time.sleep(6)

        if cls.driver is None:
            print("Error: WebDriver is not initialized. Exiting...")
            return

if __name__ == "__main__":
    MainDriverClass.setup_language()
    MainDriverClass.run()