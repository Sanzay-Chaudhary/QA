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




# call the function
if __name__ ==  "__main__":
    test_get_users()