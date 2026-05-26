class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
    
    def open_login_page(self):

        self.page.goto(
            "https://the-internet.herokuapp.com/login"
        )


    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def get_flash_message(self):

        return self.flash_message.text_content()