import pytest

from pages.login_page import LoginPage
from utils.csv_reader import read_csv


test_data = read_csv(
    "testdata/login_data.csv"
)


@pytest.mark.parametrize(
    "username,password",
    test_data
)

def test_login_csv(page, username, password):

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        username,
        password
    )

    print(
        f"\nTesting: {username} / {password}"
    )

    print(
        login_page.get_flash_message()
    )