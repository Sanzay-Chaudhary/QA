import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        yield page

        browser.close()


@pytest.fixture
def logged_in_page(page):

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    yield page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")
    
            print(
                f"\nScreenshot saved: screenshots/{item.name}.png"
            )

            print(
                f"Failed URL: {page.url}"
            )



def pytest_html_report_title(report):
    report.title = "Playwright Automation Report"


# Adding custom command-line option for environment selection
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment Name"
    )


