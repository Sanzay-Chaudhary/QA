from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= False)
        page = browser.new_page()

        yield page
        browser.close()