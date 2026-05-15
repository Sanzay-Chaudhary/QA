import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("tomsmith", "SuperSecretPassword!", "secure"),
        ("tomsmith", "wrongpass", "Your password is invalid!"),
        ("", "", "Your username is invalid!"),
    ]
)

def test_login_ddt(page, username, password, expected):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login(username, password)
    message = login_page.get_flash_message()
    assert expected in message