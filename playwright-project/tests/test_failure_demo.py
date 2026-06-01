def test_failure_demo(page):

    page.goto(
        "https://the-internet.herokuapp.com/login"
    )

    assert False