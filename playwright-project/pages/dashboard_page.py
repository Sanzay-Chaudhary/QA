class DashboardPage:

    def __init__(self, page):
        self.page = page

        # ✅ More specific locator
        self.logout_button = page.locator("a[href='/logout']")

        self.flash_message = page.locator("#flash")

    def logout(self):
        self.logout_button.click()

    def get_flash_message(self):
        return self.flash_message.inner_text()