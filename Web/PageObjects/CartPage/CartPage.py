from Web.BasePage import BasePage
from playwright.sync_api import Page
from Web.PageObjects.CheckoutPage.CheckoutPage import CheckoutPage
from Web.PageObjects.CartPage.CartPageLocators import CartPageLocator

class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CartPageLocator()

    def proceed_to_checkout(self) -> CheckoutPage:
        self.click_element(self.locators.checkout_button)
        return CheckoutPage(self.page)

    def is_correct_product_in_cart_by_name(self, name_to_verify: str) -> bool:
        product_name = self.get_text(self.locators.product_name)
        return product_name == name_to_verify
