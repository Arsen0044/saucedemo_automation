from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def fill(self, locator: str, value: str) -> None:
        self.page.fill(locator, value)
