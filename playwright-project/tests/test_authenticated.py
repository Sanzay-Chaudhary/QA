def test_secure_page(logged_in_page):

    logged_in_page.goto(
        "https://the-internet.herokuapp.com"
    )

    print("Authenticated session loaded")