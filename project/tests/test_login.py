from pages.login_page import LoginPage

def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)
    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()
    
    assert "secure" in driver.current_url

def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)
    login.enter_username("tomsmith")
    login.enter_password("WrongPassword!")
    login.click_login()

    assert "invalid" in driver.page_source