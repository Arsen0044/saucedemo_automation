from playwright.sync_api import Page, TimeoutError
from Logs.Logger import Logger

class Wait:
    def __init__(self, page: Page):
        self.page = page
        self.identify_locator = ''

    def element_to_be_clickable(self, locator: str, timeout=5):
        self.identify_locator = locator
        try:
            self.page.locator(locator).wait_for(state="attached", timeout=timeout * 1000)
            self.page.locator(locator).wait_for(state="visible", timeout=timeout * 1000)
            return True
        except TimeoutError:
            Logger.log.debug(f'The locator {locator} is not clickable within {timeout} seconds.')
            return False

    def element_not_to_be_clickable(self, locator: str, timeout=5):
        self.identify_locator = locator
        try:
            self.page.locator(locator).wait_for(state="hidden", timeout=timeout * 1000)
            return True
        except TimeoutError:
            Logger.log.debug(f'The locator {locator} is still clickable within {timeout} seconds.')
            return False

    def presence_of_element_located(self, locator: str, timeout=5):
        self.identify_locator = locator
        try:
            self.page.locator(locator).wait_for(state="attached", timeout=timeout * 1000)
            return True
        except TimeoutError:
            Logger.log.debug(f'The locator {locator} is not present within {timeout} seconds.')
            return False

    def not_presence_of_element_located(self, locator: str, timeout=5):
        self.identify_locator = locator
        try:
            self.page.locator(locator).wait_for(state="detached", timeout=timeout * 1000)
            return True
        except TimeoutError:
            Logger.log.debug(f'The locator {locator} is still present within {timeout} seconds.')
            return False

    def visibility_of_element_located(self, locator: str, timeout=5):
        self.identify_locator = locator
        try:
            self.page.locator(locator).wait_for(state="visible", timeout=timeout * 1000)
            return True
        except TimeoutError:
            Logger.log.debug(f'The locator {locator} is not visible within {timeout} seconds.')
            return False

    def not_visibility_of_element_located(self, locator: str, timeout=5):
        self.identify_locator = locator
        try:
            self.page.locator(locator).wait_for(state="hidden", timeout=timeout * 1000)
            return True
        except TimeoutError:
            Logger.log.debug(f'The locator {locator} is still visible within {timeout} seconds.')
            return False