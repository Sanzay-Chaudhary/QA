import requests

def test_create_users():
    url = "https://jsonplaceholder.typicode.com/users"
    payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "abc@gmail.com",
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]