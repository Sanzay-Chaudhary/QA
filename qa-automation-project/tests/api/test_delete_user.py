import requests
def test_delete_user():
    url = "https://reqres.in/api/users/2"
    response = requests.delete(url)
    print(response.status_code)
    assert response.status_code == 204