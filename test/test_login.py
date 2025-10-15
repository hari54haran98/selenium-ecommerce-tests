import pytest
import allure
from utilities.helper import Helper
from pages.login_page import LoginPage


@allure.feature("Login Tests")
@allure.story("User Authentication")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup before each test"""
        self.driver = Helper.setup_driver()
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.quit()

    @allure.title("Successful Login with Valid Credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self):
        """Test that users can login with valid credentials"""
        with allure.step("Navigate to login page"):
            self.login_page.navigate_to_login()
            Helper.take_screenshot(self.driver, "login_page_loaded")

        with allure.step("Enter valid credentials"):
            self.login_page.login("standard_user", "secret_sauce")

        with allure.step("Verify login successful and redirected to products"):
            assert self.login_page.is_login_successful()
            Helper.take_screenshot(self.driver, "login_successful")

        # Attach screenshot to Allure report
        allure.attach.file(
            Helper.take_screenshot(self.driver, "final_success"),
            name="login_success",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.title("Failed Login with Invalid Credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_failed_login_invalid_credentials(self):
        """Test that login fails with invalid credentials and shows error"""
        with allure.step("Navigate to login page"):
            self.login_page.navigate_to_login()

        with allure.step("Enter invalid credentials"):
            self.login_page.login("invalid_user", "wrong_password")

        with allure.step("Verify error message is displayed"):
            error_message = self.login_page.get_error_message()
            assert "username and password do not match" in error_message.lower()
            Helper.take_screenshot(self.driver, "login_error_displayed")
