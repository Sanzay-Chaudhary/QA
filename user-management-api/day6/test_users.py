import requests
url = "https://jsonplaceholder.typicode.com"

def test_get_users():
    
    response = requests.get(f"{url}/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]
    assert "username" in data[0]
    assert "email" in data[0]


def test_get_single_user():
    response = requests.get(f"{url}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data
    assert "username" in data
    assert "email" in data


def test_get_nonexistent_user():
    response = requests.get(f"{url}/users/9999")
    assert response.status_code == 404
   
def test_create_user():
    payload = {
        "name": "Sanjay",
        "username": "sanjay123",
        "email": "abc@example.com"
    }
    response = requests.post(f"{url}/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
    assert "id" in data  # The response should include an ID for the new user

def test_update_user():

    payload = {
        "name": "Updated Sanjay",
        "username": "updated123",
        "email": "updated@example.com"
    }

    response = requests.put(
        f"{url}/users/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]

def test_patch_user():

    payload = {
        "name": "Patched Name"
    }

    response = requests.patch(
        f"{url}/users/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == payload["name"]


def test_delete_user():

    response = requests.delete(
        f"{url}/users/1"
    )

    assert response.status_code == 200