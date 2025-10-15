from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        print("🔐 LoginPage initialized")

    # Locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def navigate_to_login(self):
        """Navigate to login page"""
        print("🌐 Navigating to login page...")
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        """Complete login flow"""
        print(f"🚀 Attempting login with {username}")
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def get_error_message(self):
        """Get error message text"""
        try:
            error_text = self.driver.find_element(*self.ERROR_MESSAGE).text
            print(f"❌ Login error: {error_text}")
            return error_text
        except:
            return "No error message found"

    def is_login_successful(self):
        """Check if login was successful"""
        return "inventory" in self.driver.current_url