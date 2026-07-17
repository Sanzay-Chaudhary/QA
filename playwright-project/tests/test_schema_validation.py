from api.api_client_helper import APIClient
from jsonschema import validate
from schemas.user_schema import USER_SCHEMA

client = APIClient()

def test_schema_validation():
    response = client.get("https://jsonplaceholder.typicode.com/users/1")
    data = client.get_json(response)
    print(data["name"])
    print(data["username"])

    validate(
        instance = data,
        schema = USER_SCHEMA
    )