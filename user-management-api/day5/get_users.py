import requests
def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
    assert "name" in data[0]
    assert "id" in data[0]
    assert "email" in data[0]
    assert "application/json" in response.headers["Content-Type"]
    print(response.headers["Content-Type"])
    print(response.elapsed)
    print(response.elapsed.total_seconds())