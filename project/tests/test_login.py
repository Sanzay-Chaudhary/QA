
from pages.login_page import LoginPage
def test_valid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)

    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()

    assert "You logged into a secure area!" in login_page.get_flash_message()