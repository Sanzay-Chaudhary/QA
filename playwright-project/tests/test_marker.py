import pytest

@pytest.mark.smoke
def test_login():
    print("Running smoke test: test_login")
    assert True

@pytest.mark.regression
def test_dashboard():
    print("Running regression test: test_dashboard")
    assert True


@pytest.mark.api
def test_get_users():
    print("Running API test: test_get_users")
    assert True