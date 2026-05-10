from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page =browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login", wait_until="domcontentloaded")

    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()

    assert "secure" in page.url

    login_message = page.locator("#flash").inner_text()

    assert "You logged into a secure area!" in login_message

    print("Login test passed successfully")
    page.wait_for_timeout(3000)

    print("\n===== CHECKBOX TEST =====")
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox =page.locator("input[type='checkbox']").first
    checkbox.check()
    assert checkbox.is_checked()
    print("chekbox is checked")

    checkbox.uncheck()
    assert not checkbox.is_checked()
    print("checkbox is unchecked")
    page.wait_for_timeout(3000)


    print("\n===== DROPDOWN TEST =====")
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")
    dropdown.select_option("2")
    selected_value = dropdown.input_value()
    assert selected_value == "2"
    print("Dropdown option 2 selected successfully")
    page.wait_for_timeout(3000)
    

    print("\n===== ALERT TEST =====")
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("text=Click for JS Alert").click()
    result_text = page.locator("#result").inner_text()
    assert "You successfully clicked an alert" in result_text
    print("Alert test passed successfully")
    page.wait_for_timeout(3000)
    browser.close()