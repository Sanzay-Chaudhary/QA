from api.api_client_helper import APIClient

client = APIClient()

def test_json_validation():
    response = client.get( "https://jsonplaceholder.typicode.com/users/1")

    client.validate_status_code(response, 200)

    data = client.get_json(response)
    print(data["name"])
    assert data["id"] == 1

    assert data["name"] == "Leanne Graham"

    assert data["username"] == "Bret"

    assert data["email"] == "Sincere@april.biz"

    assert "address" in data

    assert data["address"]["city"] == "Gwenborough"

    assert isinstance(data["id"], int)

    assert isinstance(data["name"], str)
