import pytest
import allure
from utilities.helper import Helper
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@allure.feature("Products Tests")
@allure.story("Shopping Cart Management")
class TestProducts:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup before each test"""
        self.driver = Helper.setup_driver()
        self.login_page = LoginPage(self.driver)
        self.products_page = ProductsPage(self.driver)

        # Login before each test
        self.login_page.navigate_to_login().login("standard_user", "secret_sauce")
        yield
        self.driver.quit()

    @allure.title("Add Single Item to Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_single_item_to_cart(self):
        """Test adding a single item to shopping cart"""
        with allure.step("Add backpack to cart"):
            self.products_page.add_backpack_to_cart()

        with allure.step("Verify cart count updates to 1"):
            cart_count = self.products_page.get_cart_count()
            assert cart_count == "1"
            Helper.take_screenshot(self.driver, "single_item_cart")

    @allure.title("Add Multiple Items to Cart")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_multiple_items_to_cart(self):
        """Test adding multiple items to shopping cart"""
        with allure.step("Add backpack to cart"):
            self.products_page.add_backpack_to_cart()

        with allure.step("Add bike light to cart"):
            self.products_page.add_bike_light_to_cart()

        with allure.step("Verify cart count shows 2 items"):
            cart_count = self.products_page.get_cart_count()
            assert cart_count == "2"
            Helper.take_screenshot(self.driver, "multiple_items_cart")