from api.api_client_helper import APIClient

client = APIClient()

def test_get_users():
    response = client.get( "https://jsonplaceholder.typicode.com/users/1")

    client.validate_status_code(response, 200)

    data = client.get_json(response)
    print(data["name"])
    assert data["name"] == "Leanne Graham"
