class DashboardPage:

    def __init__(self, page):

        self.page = page

        self.logout_button = page.locator("a.button")

    def logout(self):

        self.logout_button.click()