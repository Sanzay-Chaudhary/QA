import requests
url = "https://jsonplaceholder.typicode.com/users/1"

payload = {
    "name": "New Name"
}

response = requests.patch(
    url,
    json=payload
)

assert response.status_code == 200

data = response.json()

assert data["name"] == "New Name"