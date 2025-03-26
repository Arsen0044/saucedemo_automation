from Web.BasePage import BasePage
from playwright.sync_api import Page
from Web.PageObjects.LoginPage.LoginPageLocators import LoginPageLocator

class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = LoginPageLocator()

    def fill_in_username_field(self, username: str) -> None:
        self.fill(self.locators.username_input, username)