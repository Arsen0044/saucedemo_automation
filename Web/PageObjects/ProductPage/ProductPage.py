from Web.BasePage import BasePage
from playwright.sync_api import Page
from Web.PageObjects.CartPage.CartPage import CartPage
from Web.PageObjects.ProductPage.ProductPageLocators import ProductPageLocator

class ProductPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = ProductPageLocator()

    def is_product_page_loaded(self) -> bool:
        return self.visibility_of_element_located(self.locators.products_list)

    def add_product_to_cart_by_name(self, product_name: str) -> None:
        locator_type_product_name = product_name.replace(" ", "-").lower()
        locator = self.locators.add_cart_button.format(locator_type_product_name)
        self.click_element(locator)

    def navigate_to_cart(self):
        self.click_element(self.locators.cart_button)
        return CartPage(self.page)
