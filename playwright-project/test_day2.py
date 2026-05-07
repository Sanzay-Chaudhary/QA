from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")

    username = page.locator("#username")
    password = page.locator("#password")

    login_btn = page.locator("button[type='submit']")

    username.fill("tomsmith")
    password.fill("SuperSecretPassword!")
    login_btn.click()

    success_message = page.locator("#flash").inner_text()

    if "You logged into a secure area!" in success_message:
        print("Login successful!")
    else:
        print("Login failed!")

    page.wait_for_timeout(5000)

    browser.close()
