class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def get_url(self):
        return self.page.url

    def take_screenshot(self, file_name):
        self.page.screenshot(
            path=f"screenshots/{file_name}"
        )