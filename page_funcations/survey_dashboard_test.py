import string
import time
from page_funcations.driver_manager import DriverManager
from page_object.survey_dashboard_page import SurveyDashboardPage
from faker import Faker

class SurveyDashboardTest:
    def __init__(self):
        self.faker = Faker()
        self.driver = DriverManager.get_driver()
        self.survey_dashboard_page = SurveyDashboardPage(self.driver)

    def search_survey_functionality(self):
        """Execute the test for search survey."""
        self.survey_dashboard_page.search_survey_name()
        time.sleep(2)
        self.survey_dashboard_page.clear_survey_name()
        time.sleep(1)
        self.survey_dashboard_page.select_random_category_option()
        time.sleep(1)

    def view_survey(self):
        """Execute the test of view survey information"""
        self.survey_dashboard_page.click_on_survey_view()
        self.survey_dashboard_page.click_on_view_cancel_button()

    def edit_survey_basic_information(self):
        """Execute the test of edit basic information"""
        self.survey_dashboard_page.click_on_survey_name_field()
        time.sleep(2)
        self.survey_dashboard_page.change_language()
        time.sleep(2)
        self.survey_dashboard_page.select_of_survey_language()
        time.sleep(2)
        self.survey_dashboard_page.click_on_save_button()
        time.sleep(2)
        self.survey_dashboard_page.click_on_save_survey_dilog_box()
        time.sleep(2)

    def test_pagination(self):
        dashboard_page = SurveyDashboardPage(self.driver)
        self.survey_dashboard_page.click_on_survey_tab()
        time.sleep(2)
        if dashboard_page.is_right_arrow_available():
            if dashboard_page.is_right_arrow_enabled():
                print("Right pagination arrow is enabled.")
                dashboard_page.click_right_arrow()
                time.sleep(3)
            else:
                print("Right pagination arrow is disabled.")
        else:
            print("Right pagination arrow is not available.")

        if dashboard_page.is_left_arrow_available():
            if dashboard_page.is_left_arrow_enabled():
                print("Left pagination arrow is enabled.")
                dashboard_page.click_left_arrow()
                time.sleep(3)
            else:
                print("Left pagination arrow is disabled.")
        else:
            print("Left pagination arrow is not available.")