from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        print("💳 CheckoutPage initialized")

    # Locators
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    CHECKOUT_TITLE = (By.CLASS_NAME, "title")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, first_name):
        """Enter first name"""
        print(f"👤 Entering first name: {first_name}")
        self.driver.find_element(*self.FIRST_NAME_FIELD).clear()
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        """Enter last name"""
        print(f"👤 Entering last name: {last_name}")
        self.driver.find_element(*self.LAST_NAME_FIELD).clear()
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code):
        """Enter postal code"""
        print(f"📮 Entering postal code: {postal_code}")
        self.driver.find_element(*self.POSTAL_CODE_FIELD).clear()
        self.driver.find_element(*self.POSTAL_CODE_FIELD).send_keys(postal_code)
        return self

    def enter_shipping_info(self, first_name, last_name, postal_code):
        """Enter all shipping information"""
        print("📝 Entering shipping information...")
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        return self

    def continue_to_overview(self):
        """Click continue button"""
        print("➡️ Continuing to overview...")
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self

    def complete_purchase(self):
        """Click finish button to complete purchase"""
        print("✅ Completing purchase...")
        self.driver.find_element(*self.FINISH_BUTTON).click()
        return self

    def cancel_checkout(self):
        """Click cancel button"""
        print("❌ Cancelling checkout...")
        self.driver.find_element(*self.CANCEL_BUTTON).click()
        return self

    def get_success_message(self):
        """Get order success message"""
        message = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text
        print(f"🎉 Order success: {message}")
        return message

    def get_error_message(self):
        """Get error message if any"""
        try:
            error_text = self.driver.find_element(*self.ERROR_MESSAGE).text
            print(f"❌ Checkout error: {error_text}")
            return error_text
        except:
            return "No error message"

    def get_page_title(self):
        """Get checkout page title"""
        return self.driver.find_element(*self.CHECKOUT_TITLE).text

    def get_order_summary(self):
        """Get order summary details"""
        try:
            item_total = self.driver.find_element(*self.ITEM_TOTAL).text
            tax = self.driver.find_element(*self.TAX).text
            total = self.driver.find_element(*self.TOTAL).text
            summary = {
                'item_total': item_total,
                'tax': tax,
                'total': total
            }
            print(f"💰 Order summary: {summary}")
            return summary
        except:
            return "No summary available"

    def is_checkout_complete(self):
        """Check if checkout is successfully completed"""
        return "checkout-complete" in self.driver.current_url