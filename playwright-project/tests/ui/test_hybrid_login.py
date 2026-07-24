from playwright.sync_api import sync_playwright


def test_hybrid_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        context = browser.new_context()

        context.add_cookies([
            {
                "name": "session_token",
                "value": "fake_auth_token",
                "domain": "the-internet.herokuapp.com",
                "path": "/"
            }
        ])

        page = context.new_page()

        page.goto("https://the-internet.herokuapp.com")

        print("Page opened with simulated session")

        # Print cookies
        print(context.cookies())

        # Save auth state
        context.storage_state(path="auth.json")

        page.wait_for_timeout(5000)

        browser.close()