def test_secure_page(authenticated_page):

    authenticated_page.goto(
        "https://the-internet.herokuapp.com"
    )

    print("Authenticated session loaded")