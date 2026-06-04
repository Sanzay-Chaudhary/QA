from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger()

def test_valid_login(page):

    logger.info("Opening login page")

    login_page = LoginPage(page)

    login_page.open_login_page()

    logger.info("Entering credentials")

    login_page.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    logger.info("Login successful")