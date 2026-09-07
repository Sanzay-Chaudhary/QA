import requests


def test_get_nonexistent_user():
    url = "https://jsonplaceholder.typicode.com/users/999999"

    response = requests.get(url)

    assert response.status_code == 404