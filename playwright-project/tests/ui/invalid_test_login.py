from pages.login_page import LoginPage


def test_invalid_login(page):

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        "tomsmith",
        "wrongpassword"
    )

    assert (
        "Your password is invalid!"
        in login_page.get_flash_message()
    )