# A BaseTestMain class is created to handle browser setup and teardown for all the test classes.
#  This ensures that all tests can run on a fresh browser instance.


from selenium import webdriver
import pytest


class BaseTestMain:

    url = "https://ecommerce.artoftesting.com/"

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()
