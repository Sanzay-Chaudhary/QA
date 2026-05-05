from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    page.goto("https://ekantipur.com")

    page.wait_for_selector("h2")

    headlines = page.locator("h2").all_text_contents()

    for i, title in enumerate(headlines[:5]):
        print(f"{i+1}. {title}")

    browser.close()
