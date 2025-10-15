from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time
import os


class ChromeHelper:
    @staticmethod
    def setup_driver(headless=False):
        """Set up and return Chrome WebDriver - Optimized for CI/CD"""
        print("🚀 Setting up Chrome driver...")

        chrome_options = Options()

        # Essential options for CI/CD compatibility
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-software-rasterizer")

        if headless:
            chrome_options.add_argument("--headless=new")

        try:
            # Use webdriver-manager for Chrome
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.implicitly_wait(10)
            print("✅ Chrome driver setup successful!")
            return driver
        except Exception as e:
            print(f"❌ Chrome setup failed: {e}")
            raise Exception(f"Chrome driver setup failed: {e}")

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