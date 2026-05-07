from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")
    page.fill("#password", "Superssword!")
    page.click("button[type='submit']")

    success_message = page.locator("#flash").inner_text()

    if "You logged into a secure area!" in success_message:
        print("login successful!")
    
    else:
        print("Login failed!")
    
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the result

    page.goto("https://the-internet.herokuapp.com/checkboxes")

    page.click("text=Checkboxes")

    checkbox = page.locator("input[type='checkbox']").first
    checkbox.check()

    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the result

    browser.close()