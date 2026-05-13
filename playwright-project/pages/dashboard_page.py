class DashboardPage:
    def __init__(self, page):
        self.page = page

    # Locators for the dashboard page elements
        self.logout_button = page.locator("text= Logout")

    # Actions
    def logout(self):
        self.logout_button.click()