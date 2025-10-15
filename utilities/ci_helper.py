from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import time
import os


class CIHelper:
    @staticmethod
    def setup_driver(headless=False):
        """Use webdriver-manager for automatic Firefox setup in CI/CD"""
        print("🏗️ CI/CD: Setting up Firefox with webdriver-manager...")

        firefox_options = Options()

        # Essential options for CI/CD
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--window-size=1920,1080")

        if headless:
            firefox_options.add_argument("--headless")

        try:
            # Let webdriver-manager handle everything automatically
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=firefox_options)
            driver.implicitly_wait(10)
            print("✅ CI/CD Firefox setup successful with webdriver-manager!")
            return driver
        except Exception as e:
            print(f"❌ CI/CD webdriver-manager failed: {e}")
            raise Exception(f"CI/CD Firefox setup failed: {e}")

    @staticmethod
    def take_screenshot(driver, name):
        """Take screenshot"""
        if not os.path.exists('reports'):
            os.makedirs('reports')
        filename = f"reports/screenshot_{name}_{int(time.time())}.png"
        driver.save_screenshot(filename)
        print(f"📸 Screenshot saved: {filename}")
        return filename

    @staticmethod
    def wait_for_element(driver, by, value, timeout=10):
        """Wait for element"""
        return WebDriverWait(driver, timeout).until(
            lambda driver: driver.find_element(by, value)
        )