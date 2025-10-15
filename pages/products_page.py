from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        print("🛍️ ProductsPage initialized")

    # Locators
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_page_title(self):
        """Get products page title"""
        title = self.driver.find_element(*self.PRODUCTS_TITLE).text
        print(f"📄 Page title: {title}")
        return title

    def add_backpack_to_cart(self):
        """Add backpack to cart"""
        print("🎒 Adding backpack to cart...")
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()
        return self

    def add_bike_light_to_cart(self):
        """Add bike light to cart"""
        print("🚲 Adding bike light to cart...")
        self.driver.find_element(*self.ADD_TO_CART_BIKE_LIGHT).click()
        return self

    def get_cart_count(self):
        """Get number of items in cart"""
        try:
            count = self.driver.find_element(*self.CART_BADGE).text
            print(f"🛒 Cart has {count} items")
            return count
        except:
            print("🛒 Cart is empty")
            return "0"

    def go_to_cart(self):
        """Click cart icon to go to cart page"""
        print("📦 Going to cart...")
        self.driver.find_element(*self.CART_ICON).click()
        return self