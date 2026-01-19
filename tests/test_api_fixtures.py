import pytest
import requests

# ---------- FIXTURE ----------
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


# ---------- GET TEST ----------
def test_get_users(base_url):
    response = requests.get(f"{base_url}/users")

    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]


# ---------- POST TEST ----------
def test_create_user(base_url):
    payload = {
        "name": "Sanjay",
        "job": "QA Engineer"
    }

    response = requests.post(f"{base_url}/users", json=payload)

    assert response.status_code in [200, 201]

    data = response.json()
    assert data["name"] == "Sanjay"

#this code is needed when running the script directly
# if __name__ == "__main__":
#     pytest.main()
