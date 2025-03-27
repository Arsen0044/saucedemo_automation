import allure

from Logs.Logger import Logger
from playwright.sync_api import Page

from Web.Utilities.read_config import Constants
from Web.PageObjects.LoginPage.LoginPage import LoginPage
from Web.PageObjects.ProductPage.ProductPage import ProductPage


@allure.suite("Login tests")
@allure.sub_suite("Login tests")
class TestLogin:

    @allure.title("Test successful login with valid credentials")
    @allure.description("Login with valid credentials, verify redirection to product page")
    def test_successful_login(self, page: Page):
        with allure.step("Open login page"):
            Logger.log.info("Open login form")
            page.goto(Constants.base_url)
            login_page = LoginPage(page)

        with allure.step("Fill in valid username and password"):
            Logger.log.info("Fill in username")
            login_page.fill_in_username_field(Constants.standard_user_name)

            Logger.log.info("Fill in password")
            login_page.fill_in_password_field(Constants.standard_user_password)

        with allure.step("Click on login button"):
            Logger.log.info("Click login button")
            login_page.click_login_button()

        with allure.step("Verify successful login"):
            Logger.log.info("Verify user is redirected to the product page")
            product_page = ProductPage(page)
            assert product_page.is_product_page_loaded(), "Product page is not loaded after login"

    @allure.title("Test invalid login with wrong credentials")
    @allure.description("Login with invalid credentials, verify error message is shown")
    def test_invalid_login(self, page: Page):
        with allure.step("Open login page"):
            Logger.log.info("Open login form")
            page.goto(Constants.base_url)
            login_page = LoginPage(page)

        with allure.step("Fill in invalid username and password"):
            Logger.log.info("Fill in invalid username")
            login_page.fill_in_username_field("invalid_user")

            Logger.log.info("Fill in password")
            login_page.fill_in_password_field("invalid_password")

        with allure.step("Click on login button"):
            Logger.log.info("Click login button")
            login_page.click_login_button()

        with allure.step("Verify error message is shown with correct text"):
            Logger.log.info("Check if error message is displayed for invalid login")
            assert login_page.is_error_message_visible(), "Error message is not displayed"

            Logger.log.info("Check if correct text in error")
            assert login_page.is_correct_error_message_text()

    @allure.title("Test password input masking")
    @allure.description("Ensure password input is masked with •")
    def test_password_masking(self, page: Page):
        with allure.step("Open login page"):
            Logger.log.info("Open login form")
            page.goto(Constants.base_url)
            login_page = LoginPage(page)

        with allure.step("Fill in password field"):
            Logger.log.info("Fill in password field")
            login_page.fill_in_password_field(Constants.standard_user_password)

        with allure.step("Verify password field has masking symbol"):
            Logger.log.info("Check if password field is masked")
            assert login_page.is_password_masked(), "Password is not masked correctly"
