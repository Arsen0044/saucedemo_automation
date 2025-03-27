import pytest
from Logs.Logger import Logger
from Web.Utilities.read_config import Constants
from playwright.sync_api import sync_playwright
from Web.PageObjects.LoginPage.LoginPage import LoginPage


@pytest.fixture(scope="class")
def browser():
    Logger.log.debug("Start Playwright browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )
        yield browser
        browser.close()
        Logger.log.debug("Close browser")

@pytest.fixture(scope="function")
def page(browser):
    Logger.log.debug("Create new page")
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    Logger.log.debug("Close page")

@pytest.fixture(scope="function")
def login_with_standard_user(page):
    Logger.log.info('Do log in to dashboard')
    login_page = LoginPage(page)
    product_page = login_page.do_login(Constants.standard_user_name, Constants.standard_user_password)
    product_page.wait_for_page_load()
    yield product_page
    Logger.log.info('FIXTURE teardown get_dashboard_with_login')

