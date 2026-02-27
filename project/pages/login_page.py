from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    # ===== Locators =====
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    flash_message = (By.ID, "flash")

    # ===== Constructor =====
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===== Actions =====
    def enter_username(self, username):

        self.wait.until(EC.visibility_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_input))
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        # self.driver.find_element(*self.login_button).click()
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def get_flash_message(self):
        # return self.driver.find_element(*self.flash_message).text
        return self.wait.until(EC.visibility_of_element_located(self.flash_message)).text