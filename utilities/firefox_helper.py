from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time
import os


class FirefoxHelper:
    @staticmethod
    def setup_driver(headless=False):
        """Set up and return Firefox WebDriver - Compatible with Linux CI/CD"""
        print("🦊 Setting up Firefox driver...")

        firefox_options = Options()

        # Essential options for CI/CD compatibility
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")

        if headless:
            firefox_options.add_argument("--headless")

        try:
            # Use webdriver-manager to handle GeckoDriver automatically
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=firefox_options)
            driver.implicitly_wait(10)
            print("✅ Firefox driver setup successful!")
            return driver
        except Exception as e:
            print(f"❌ Firefox setup failed: {e}")
            print("🔄 Trying alternative setup...")
            # Fallback: Use system GeckoDriver
            service = Service('/usr/local/bin/geckodriver')
            driver = webdriver.Firefox(service=service, options=firefox_options)
            return driver

    @staticmethod
    def take_screenshot(driver, name):
        """Take screenshot and save in reports folder"""
        if not os.path.exists('reports'):
            os.makedirs('reports')
        filename = f"reports/screenshot_{name}_{int(time.time())}.png"
        driver.save_screenshot(filename)
        print(f"📸 Screenshot saved: {filename}")
        return filename

    @staticmethod
    def wait_for_element(driver, by, value, timeout=10):
        """Wait for element to be present"""
        return WebDriverWait(driver, timeout).until(
            lambda driver: driver.find_element(by, value)
        )