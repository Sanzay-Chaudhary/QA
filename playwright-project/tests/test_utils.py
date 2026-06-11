from utils.helpers import (print_current_url,generate_random_email, take_screenshot, current_timestamp)

def test_example(page):
    page.goto("https://www.google.com")
    print_current_url(page)

    email = generate_random_email()
    print(email)

    

    timestamp =current_timestamp()
    print(timestamp)

    take_screenshot(page, f"test-run-{timestamp}")

    assert True

