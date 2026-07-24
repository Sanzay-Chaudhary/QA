import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password, expected",
    [
        (
            "tomsmith",
            "SuperSecretPassword!",
            "You logged into a secure area!"
        ),
        (
            "wronguser",
            "wrongpass",
            "Your username is invalid!"
        )
    ]
)
def test_login_ddt(
    page,
    username,
    password,
    expected
):

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(username, password)

    flash_message = login_page.get_flash_message()

    print("\nMessage:", flash_message)

    assert expected in flash_message