def test_checkbox(page):

    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkbox = page.locator(
        "input[type='checkbox']"
    ).first

    checkbox.check()

    assert checkbox.is_checked()

    checkbox.uncheck()

    assert not checkbox.is_checked()