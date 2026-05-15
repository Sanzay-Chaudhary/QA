import pytest

@pytest.mark.parametrize(
    "state",
    [True, False]
)
def test_checkbox_ddt(page, state):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox = page.locator("input[type= 'checkbox']").first

    if state:
        checkbox.check()
        assert checkbox.is_checked()
    else:
        checkbox.uncheck()
        assert not checkbox.is_checked()
