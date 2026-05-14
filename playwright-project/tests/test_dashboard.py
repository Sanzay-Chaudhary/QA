from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_dashboard_logout(page):

    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Step 1: Login first
    login_page.open_login_page()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "secure" in page.url

    # Step 2: Logout
    dashboard_page.logout()

    # Step 3: Validate logout
    assert "login" in page.url

    flash_message = page.locator("#flash").inner_text()

    assert "You logged out of the secure area!" in flash_message
    