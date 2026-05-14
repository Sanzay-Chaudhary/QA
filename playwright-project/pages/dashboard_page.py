from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.logout_button = (
            "a[href='/logout']"
        )

        self.flash_message = "#flash"

    def logout(self):

        self.click(self.logout_button)

    def get_flash_message(self):

        return self.get_text(self.flash_message)