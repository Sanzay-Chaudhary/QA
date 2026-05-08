from playwright.sync_api import sync_playwright

def test_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        print("Opening login page...")

        page.goto(
            "https://the-internet.herokuapp.com/login",
            wait_until="domcontentloaded",
            timeout=60000
        )

        print("Current URL:", page.url)

        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator("button[type='submit']").click()

        assert "secure" in page.url

        flash_message = page.locator("#flash").inner_text()

        assert "You logged into a secure area!" in flash_message

        print("✅ Login test passed")

        browser.close()