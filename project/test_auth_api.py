import pytest
import requests

BASE_URL = "https://dummyjson.com/auth"

@pytest.fixture(scope="session")
def auth_token():
    payload = {
        "username": "emilys",
        "password": "emilyspass"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

    assert response.status_code == 200
    assert "token" in response.json()

    return response.json()["token"]


def test_profile_with_token(auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.get(
        f"{BASE_URL}/me",
        headers=headers
    )

    assert response.status_code == 200
    assert "username" in response.json()
