def test_valid_login(page):

    page.goto("https://the-internet.herokuapp.com/login")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")

    page.locator("button[type='submit']").click()

    assert "secure" in page.url

    flash_message = page.locator("#flash").inner_text()

    assert "You logged into a secure area!" in flash_message