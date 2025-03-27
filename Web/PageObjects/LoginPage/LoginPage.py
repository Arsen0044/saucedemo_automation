from Web.BasePage import BasePage
from playwright.sync_api import Page
from Web.Utilities.read_config import Constants
from Web.PageObjects.ProductPage.ProductPage import ProductPage
from Web.PageObjects.LoginPage.LoginPageLocators import LoginPageLocator


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = LoginPageLocator()

    def do_login(self, username: str, password: str) -> ProductPage:
        self.navigate(Constants.base_url)
        self.fill_in_username_field(username)
        self.fill_in_password_field(password)
        self.click_login_button()
        return ProductPage(self.page)

    def fill_in_username_field(self, username: str) -> None:
        self.send_keys(self.locators.username_input, username)

    def fill_in_password_field(self, password: str) -> None:
        self.send_keys(self.locators.password_input , password)

    def click_login_button(self) -> None:
        self.click_element(self.locators.login_button)

    def is_error_message_visible(self) -> bool:
        return self.visibility_of_element_located(self.locators.error_popup)

    def is_correct_error_message_text(self) -> bool:
        error_message = self.get_text(self.locators.error_popup)
        return error_message == "Epic sadface: Username and password do not match any user in this service"

    def is_password_masked(self) -> bool:
        password_field = self.find_element(self.locators.password_input)
        return True if password_field.get_attribute('type') == "password" else False


