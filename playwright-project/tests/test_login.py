from pages.login_page import LoginPage 

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "Secure" in page.url

    assert "You logged into a secure area!" in login_page.get_flash_message()
