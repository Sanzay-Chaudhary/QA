from api.api_client import APIClient

client = APIClient()

def test_get_users():
    response = client.get( "https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200