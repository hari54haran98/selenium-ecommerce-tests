import os
import sys


def setup_driver(headless=False):
    """Universal driver setup - auto-detects working browser"""
    print("🔍 Detecting optimal browser for this environment...")

    # Try Chrome first (most stable in CI/CD)
    try:
        from utilities.chrome_helper import ChromeHelper
        print("🚀 Attempting Chrome...")
        return ChromeHelper.setup_driver(headless)
    except Exception as e:
        print(f"❌ Chrome failed: {e}")

    # Try Firefox as fallback
    try:
        from utilities.firefox_helper import FirefoxHelper
        print("🦊 Attempting Firefox...")
        return FirefoxHelper.setup_driver(headless)
    except Exception as e:
        print(f"❌ Firefox failed: {e}")

    raise Exception("No browser driver could be initialized")


def take_screenshot(driver, name):
    """Take screenshot - uses any available implementation"""
    try:
        from utilities.chrome_helper import ChromeHelper
        return ChromeHelper.take_screenshot(driver, name)
    except:
        from utilities.firefox_helper import FirefoxHelper
        return FirefoxHelper.take_screenshot(driver, name)


def wait_for_element(driver, by, value, timeout=10):
    """Wait for element - uses any available implementation"""
    try:
        from utilities.chrome_helper import ChromeHelper
        return ChromeHelper.wait_for_element(driver, by, value, timeout)
    except:
        from utilities.firefox_helper import FirefoxHelper
        return FirefoxHelper.wait_for_element(driver, by, value, timeout)


class Helper:
    setup_driver = staticmethod(setup_driver)
    take_screenshot = staticmethod(take_screenshot)
    wait_for_element = staticmethod(wait_for_element)