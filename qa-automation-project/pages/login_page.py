from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_id = "username"
    password_id = "password"
    login_btn_css = "button[type= 'submit']"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_btn_css).click()