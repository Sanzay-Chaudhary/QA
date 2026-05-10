from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.on("dialog", lambda dialog:dialog.accept())
    page.click("text=Click for JS Alert")
    result = page.locator("#result").inner_text()

    assert "You successfully clicked an alert" in result
    
    browser.close()
