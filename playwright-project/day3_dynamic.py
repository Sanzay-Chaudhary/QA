from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

    page.locator("text=Start").click()

    page.wait_for_selector("#finish")

    text = page.locator("#finish").inner_text()

    assert "Hello World!" in text

    print("Dynamic loading handled successfully!")

    page.wait_for_timeout(5000)

    browser.close()