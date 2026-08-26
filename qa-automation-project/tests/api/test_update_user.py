import requests
def test_update_user():
    url = "https://reqres.in/api/users/2"
    payload = {
        "name": "Sanzay Chaudhary",
        "job": "Senior QA"
    }
    response = requests.put(url, json= payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Sanzay Chaudhary"
    assert data["job"] == "Senior QA"
