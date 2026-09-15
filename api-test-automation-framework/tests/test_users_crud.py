import allure
import jsonschema
import pytest

from schemas.user_schema import LIST_USERS_SCHEMA, SINGLE_USER_SCHEMA


@allure.feature("Users API")
@allure.story("Read")
class TestGetUsers:
    def test_list_users_returns_200_and_valid_schema(self, api_client):
        response = api_client.get("/users", params={"page": 2})
        assert response.status_code == 200
        jsonschema.validate(response.json(), LIST_USERS_SCHEMA)

    def test_single_user_returns_200_and_valid_schema(self, api_client):
        response = api_client.get("/users/2")
        assert response.status_code == 200
        jsonschema.validate(response.json(), SINGLE_USER_SCHEMA)
        assert response.json()["data"]["id"] == 2

    def test_single_user_not_found_returns_404(self, api_client):
        response = api_client.get("/users/23")
        assert response.status_code == 404
        assert response.json() == {}


@allure.feature("Users API")
@allure.story("Create")
class TestCreateUser:
    def test_create_user_returns_201(self, api_client, new_user_payload):
        response = api_client.post("/users", json=new_user_payload)
        body = response.json()
        assert response.status_code == 201
        assert body["name"] == new_user_payload["name"]
        assert body["job"] == new_user_payload["job"]
        assert "id" in body and "createdAt" in body

    @pytest.mark.parametrize("payload", [
        {},                              # missing all fields
        {"name": "Jane"},                # missing job
        {"job": "QA Engineer"},          # missing name
        {"name": "", "job": ""},         # empty strings (boundary)
    ], ids=["empty_body", "missing_job", "missing_name", "empty_strings"])
    def test_create_user_with_incomplete_payload_still_succeeds_per_api_contract(self, api_client, payload):
        # reqres.in doesn't enforce required fields, so this documents actual
        # behavior. Against a real API, this is exactly where you'd assert
        # a 400 + validation error instead — update the assertions to match
        # your API's real contract.
        response = api_client.post("/users", json=payload)
        assert response.status_code == 201


@allure.feature("Users API")
@allure.story("Update")
class TestUpdateUser:
    def test_put_updates_all_fields(self, api_client):
        response = api_client.put("/users/2", json={"name": "Jane Updated", "job": "Lead QA"})
        assert response.status_code == 200
        assert response.json()["name"] == "Jane Updated"

    def test_patch_updates_partial_fields(self, api_client):
        response = api_client.patch("/users/2", json={"job": "Senior QA"})
        assert response.status_code == 200
        assert response.json()["job"] == "Senior QA"


@allure.feature("Users API")
@allure.story("Delete")
class TestDeleteUser:
    def test_delete_user_returns_204(self, api_client):
        response = api_client.delete("/users/2")
        assert response.status_code == 204
        assert response.text == ""
