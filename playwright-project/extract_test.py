from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    page.goto("https://ekantipur.com")

    page.wait_for_selector("h2")

    headlines = page.locator("h2").all_text_contents()

    cleaned_headlines = []
    for title in headlines:
        if title.strip() and len(title) > 20:
            cleaned_headlines.append(title.strip())

    top_headlines = cleaned_headlines[:5]

    data = []


    for i, title in enumerate(top_headlines):
        data.append({"id": i+1, "headline": title})

    with open("headlines.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    browser.close()
