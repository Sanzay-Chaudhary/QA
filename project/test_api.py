import requests

# --Get Request Test--

def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

# check status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

# check first user has id and name
    data = response.json()
    assert "id" in data[0], "fisrt user has no 'id'"
    assert "name" in data[0], "first user has no 'name'"
    print("Get test passed ✅")


# create user test
def test_create_user():
    url = "https://jsonplaceholder.typicode.com/users"
    payload = {
        "name": "Sanjay",
        "job": "QA Engineer"
    }

    response = requests.post(url, json=payload)

#check status code 
    assert response.status_code in [200, 201], f"Expected 200/201, got {response.status_code}"

# response should contain the name
    data = response.json()
    assert data.get("name") == "Sanjay", f"Expected 'Sanjay', got {data.get('name')}"
    print("POST test passed ✅")


# call the function
if __name__ ==  "__main__":
    test_get_users()
    test_create_user()