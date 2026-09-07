import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


# GET
def get_users():
    response = requests.get(f"{BASE_URL}/users")

    print("Status:", response.status_code)
    print("Headers:", response.headers)
    print("Response time:", response.elapsed.total_seconds())
    print("Body:", response.json())


# GET by ID
def get_user():
    response = requests.get(f"{BASE_URL}/users/1")

    print("Status:", response.status_code)
    print("Body:", response.json())


# POST
def create_user():
    payload = {
        "name": "Sanjay",
        "username": "sanjay123",
        "email": "sanjay@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload
    )

    print("Status:", response.status_code)
    print("Body:", response.json())


# PUT
def update_user():
    payload = {
        "name": "Updated Sanjay",
        "username": "updated123",
        "email": "updated@example.com"
    }

    response = requests.put(
        f"{BASE_URL}/users/1",
        json=payload
    )

    print("Status:", response.status_code)
    print("Body:", response.json())


# PATCH
def patch_user():
    payload = {
        "name": "Partially Updated"
    }

    response = requests.patch(
        f"{BASE_URL}/users/1",
        json=payload
    )

    print("Status:", response.status_code)
    print("Body:", response.json())


# DELETE
def delete_user():
    response = requests.delete(
        f"{BASE_URL}/users/1"
    )

    print("Status:", response.status_code)
    print("Body:", response.text)


get_users()
get_user()
create_user()
update_user()
patch_user()
delete_user()