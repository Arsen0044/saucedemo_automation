from Web.Wait import Wait
from Logs.Logger import Logger
from playwright.sync_api import Page


class BasePage(Wait):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def send_keys(self, locator: str, value: str) -> None:
        self.page.fill(locator, value)

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def find_element(self, selector: str):
        return self.page.query_selector(selector)

    def click_element(self, selector: str) -> None:
        self.page.click(selector)

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)

    def wait_for_page_load(self) -> None:
        self.page.wait_for_load_state("load")

    def sleep_with_debug(self, timeout: int) -> None:
        Logger.log.info(f"Sleep with debug for {timeout} sec")
        self.page.wait_for_timeout(timeout)
