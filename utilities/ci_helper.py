from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
import time
import os


class CIHelper:
    @staticmethod
    def setup_driver(headless=False):
        """Set up Firefox WebDriver specifically for CI/CD environments"""
        print("🏗️ Setting up Firefox for CI/CD...")

        firefox_options = Options()

        # CI/CD optimized options
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--window-size=1920,1080")

        if headless:
            firefox_options.add_argument("--headless")

        try:
            # Method 1: Use system Firefox with explicit binary path
            service = Service()
            driver = webdriver.Firefox(service=service, options=firefox_options)
            driver.implicitly_wait(10)
            print("✅ CI/CD Firefox setup successful!")
            return driver
        except Exception as e:
            print(f"❌ Method 1 failed: {e}")

            try:
                # Method 2: Try with explicit Firefox binary
                firefox_binary = FirefoxBinary('/usr/bin/firefox')
                driver = webdriver.Firefox(firefox_binary=firefox_binary, options=firefox_options)
                driver.implicitly_wait(10)
                print("✅ CI/CD Firefox setup successful (method 2)!")
                return driver
            except Exception as e2:
                print(f"❌ Method 2 failed: {e2}")
                raise Exception(f"All CI/CD Firefox methods failed: {e2}")

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