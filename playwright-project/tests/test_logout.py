from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_logout(page):

    # Create page objects
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Step 1: Open login page
    login_page.open_login_page()

    # Step 2: Login
    login_page.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    # Verify login success
    assert "secure" in page.url

    # Step 3: Logout
    dashboard_page.logout()

    # Step 4: Verify redirected to login page
    assert "login" in page.url

    print("✅ Logout test passed")