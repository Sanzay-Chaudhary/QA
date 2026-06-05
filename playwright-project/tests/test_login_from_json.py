import json
from pages.login_page import LoginPage

def test_login_from_json(page):
    with open('testdata/login_data.json') as file:
        data = json.load(file)

    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login(
        data['username'],
        data['password']
    )

    # page.wait_for_timeout(5000)
    assert "secure" in page.url