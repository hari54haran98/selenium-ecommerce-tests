from utilities.firefox_helper import FirefoxHelper

# Use Firefox as the main browser
class Helper:
    setup_driver = FirefoxHelper.setup_driver
    take_screenshot = FirefoxHelper.take_screenshot
    wait_for_element = FirefoxHelper.wait_for_element