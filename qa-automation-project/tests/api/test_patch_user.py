import requests
def test_patch_user():
    url = "https://reqres.in/api/users/2"
    payload = {
        "job" : "Lead QA"
    }

    response = requests.patch(url, json= payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

    data = response.json()
    assert data["job"] == "Lead QA"
