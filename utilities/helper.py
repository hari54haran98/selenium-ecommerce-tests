import os
import time
from selenium.webdriver.support.ui import WebDriverWait


def setup_driver(headless=False):
    """Universal driver setup - detects environment and uses appropriate browser"""
    print("🔍 Detecting environment and optimal browser...")

    # Check if we're in CI/CD environment
    is_ci = os.getenv('GITHUB_ACTIONS') or os.getenv('CI')

    if is_ci:
        print("🏗️ CI/CD environment detected - using CI-specific setup")
        from utilities.ci_helper import CIHelper
        return CIHelper.setup_driver(headless)
    else:
        print("💻 Local environment - using universal browser detection")
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
    """Take screenshot and save in reports folder - PROPER IMPLEMENTATION"""
    # Ensure reports directory exists
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
        print(f"📁 Created directory: {reports_dir}")

    # Create filename with timestamp
    filename = f"{reports_dir}/screenshot_{name}_{int(time.time())}.png"

    try:
        # Take screenshot using the driver directly
        driver.save_screenshot(filename)
        print(f"📸 Screenshot saved: {filename}")

        # Verify file was created
        if os.path.exists(filename):
            file_size = os.path.getsize(filename)
            print(f"✅ File verified: {filename} ({file_size} bytes)")
            return filename
        else:
            print(f"❌ File not found after save: {filename}")
            return None

    except Exception as e:
        print(f"❌ Screenshot failed: {e}")
        return None


def wait_for_element(driver, by, value, timeout=10):
    """Wait for element to be present"""
    return WebDriverWait(driver, timeout).until(
        lambda driver: driver.find_element(by, value)
    )


# Create the Helper class with static methods
class Helper:
    setup_driver = staticmethod(setup_driver)
    take_screenshot = staticmethod(take_screenshot)
    wait_for_element = staticmethod(wait_for_element)


