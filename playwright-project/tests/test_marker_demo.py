import pytest


@pytest.mark.smoke
@pytest.mark.ui
def test_login():
    print("Smoke Login")
    assert True


@pytest.mark.regression
@pytest.mark.ui
def test_dashboard():
    print("Regression Dashboard")
    assert True


@pytest.mark.api
def test_get_users():
    print("API Test")
    assert True


@pytest.mark.database
def test_database():
    print("Database Test")
    assert True


@pytest.mark.slow
def test_report_generation():
    print("Slow Report")
    assert True