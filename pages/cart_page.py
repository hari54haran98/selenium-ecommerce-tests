from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        print("🛒 CartPage initialized")

    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_TITLE = (By.CLASS_NAME, "title")
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")

    def get_cart_items_count(self):
        """Get number of items in cart"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        print(f"📦 Cart has {len(items)} items")
        return len(items)

    def get_page_title(self):
        """Get cart page title"""
        title = self.driver.find_element(*self.CART_TITLE).text
        print(f"📄 Cart page title: {title}")
        return title

    def proceed_to_checkout(self):
        """Click checkout button"""
        print("💰 Proceeding to checkout...")
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return self

    def continue_shopping(self):
        """Click continue shopping button"""
        print("🛍️ Continuing shopping...")
        self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()
        return self

    def remove_first_item(self):
        """Remove first item from cart"""
        print("🗑️ Removing first item from cart...")
        self.driver.find_element(*self.REMOVE_BUTTON).click()
        return self

    def is_on_cart_page(self):
        """Check if we're on cart page"""
        return 'cart' in self.driver.current_url

    def get_cart_item_names(self):
        """Get names of all items in cart"""
        items = self.driver.find_elements(*self.CART_ITEMS)
        item_names = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            item_names.append(name)
        print(f"🛒 Cart contains: {item_names}")
        return item_names