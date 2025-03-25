import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright
