import allure

from Logs.Logger import Logger
from playwright.sync_api import Page

from Web.Utilities.read_config import Constants
from Web.PageObjects.LoginPage.LoginPage import LoginPage


@allure.suite("Login tests")
@allure.sub_suite("Login tests")
class TestLogin:

    @allure.title("Test login main flow")
    @allure.description("Open login page, do login, verify logged in")
    def test_first_login(self, page: Page):

        with allure.step("Open login page"):
            Logger.log.log("Open login form")
            page.goto("https://www.saucedemo.com/")
            login_page = LoginPage(page)

        with allure.step("Fill in username"):
            Logger.log.info("Fill in username field")
            login_page.fill_in_username_field(Constants.standard_user_name)

