from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_successful_login(page):

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    # URL validation
    expect(page).to_have_url(
        "https://the-internet.herokuapp.com/secure"
    )

    # Flash message validation
    expect(
        login_page.flash_message
    ).to_contain_text(
        "You logged into a secure area!"
    )

    print("✅ Login test passed")