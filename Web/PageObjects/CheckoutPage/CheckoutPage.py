from Web.BasePage import BasePage
from playwright.sync_api import Page
from Web.PageObjects.CheckoutPage.CheckoutLocators import CheckoutPageLocator

class CheckoutPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = CheckoutPageLocator()

    def fill_in_checkout_details(self, first_name: str, last_name: str, zip_code: str) -> None:
        self.send_keys(self.locators.first_name_input, first_name)
        self.send_keys(self.locators.last_name_input, last_name)
        self.send_keys(self.locators.zip_code_input, zip_code)

    def place_order(self):
        self.click_element(self.locators.continue_button)
        self.click_element(self.locators.finish_button)

    def is_order_confirmation_visible(self):
        return self.visibility_of_element_located(self.locators.success_order_message)
