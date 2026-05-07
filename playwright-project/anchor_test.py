from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://ekantipur.com")

    page.wait_for_selector("h2 a")

    elements = page.locator("h2 a")

    data = []

    # get the count once to avoid calling count() repeatedly
    count = elements.count()
    for i in range(min(5, count)):
        title = elements.nth(i).text_content()
        title = title.strip() if title else ""

        parent = elements.nth(i).locator("xpath=..")
        link = parent.get_attribute("href")

        # Convert relative URL to full URL
        if link and link.startswith("/"):
            link = "https://ekantipur.com" + link

        data.append({
            "id": i + 1,
            "headline": title,
            "link": link
        })

    # Save JSON
    with open("anchor.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("✅ Headlines with links saved!")

    browser.close()