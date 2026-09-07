import requests

url = "https://jsonplaceholder.typicode.com/users/1"

payload = {
    "name": "Updated User",
    "username": "updateduser",
    "email": "updated@example.com"
}

response = requests.put(
    url,
    json=payload
)

assert response.status_code == 200

data = response.json()
assert data["name"] == "Updated User"
assert data["username"] == "updateduser"
assert data["email"] == "updated@example.com"
