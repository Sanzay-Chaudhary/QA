import pytest

from utils.excel_reader import read_excel

from pages.login_page import LoginPage


test_data = read_excel(
    "testdata/login_data.xlsx",
    "LoginData"
)


@pytest.mark.parametrize(
    "username,password",
    test_data
)

def test_login_excel(page, username, password):

    login = LoginPage(page)

    login.open_login_page()

    login.login(username, password)
    page.screenshot(path="screenshots/login_success.png")

    print(
        f"Testing {username} / {password}"
    )
    