import requests
def test_create_user():

    url = "https://reqres.in/api/users"
    payload = {
        "name" : "Sanzay",
        "job" : "QA"
    }
    
    response = requests.post(url, json=payload)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == "Sanzay"
    assert data["job"] == "QA"
