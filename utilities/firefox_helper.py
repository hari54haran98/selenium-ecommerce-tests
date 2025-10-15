from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import os


class FirefoxHelper:
    @staticmethod
    def setup_driver(headless=False):
        """Set up Firefox WebDriver - Optimized for CI/CD"""
        print("🦊 Setting up Firefox driver...")

        firefox_options = Options()

        # Critical options for CI/CD stability
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--window-size=1920,1080")

        # Firefox-specific optimizations
        firefox_options.set_preference("dom.ipc.processCount", 8)
        firefox_options.set_preference("dom.disable_beforeunload", True)
        firefox_options.set_preference("dom.popup_maximum", 0)

        if headless:
            firefox_options.add_argument("--headless")

        try:
            # Use system Firefox with direct service (no webdriver-manager)
            service = Service()
            driver = webdriver.Firefox(service=service, options=firefox_options)
            driver.implicitly_wait(10)
            print("✅ Firefox driver setup successful!")
            return driver
        except Exception as e:
            print(f"❌ Firefox setup failed: {e}")
            raise

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