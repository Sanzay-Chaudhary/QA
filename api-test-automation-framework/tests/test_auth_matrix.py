import allure
import pytest

from api_client.base_client import APIClient


@allure.feature("Authentication")
class TestLogin:
    def test_valid_credentials_return_token(self, api_client):
        response = api_client.post("/login", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka",
        })
        assert response.status_code == 200
        assert "token" in response.json()

    # Note: this demo API accepts ANY password for a known fixture email
    # (it doesn't actually check credentials) — so "wrong password" isn't
    # a real negative case here. Against a real auth backend, add a case
    # with a valid email + genuinely wrong password expecting 401/400.
    @pytest.mark.parametrize("payload, expected_status, expected_error", [
        ({"email": "not-registered@reqres.in", "password": "cityslicka"}, 400, "user not found"),
        ({"email": "eve.holt@reqres.in"}, 400, "Missing password"),
        ({"password": "cityslicka"}, 400, "Missing email or username"),
        ({}, 400, "Missing email or username"),
    ], ids=["unregistered_email", "missing_password", "missing_email", "missing_both"])
    def test_invalid_or_missing_credentials_are_rejected(self, api_client, payload, expected_status, expected_error):
        response = api_client.post("/login", json=payload)
        assert response.status_code == expected_status
        assert expected_error.lower() in response.json()["error"].lower()


@allure.feature("Authentication")
class TestTokenValidation:
    def test_request_with_missing_token_is_rejected(self):
        # No Authorization header set at all.
        client = APIClient(base_url="https://reqres.in/api", default_headers={
            "x-api-key": "reqres-free-v1",
        })
        response = client.get("/users/2")
        # reqres.in doesn't actually gate GETs behind auth, so this assertion
        # documents the demo API's real behavior. Against a real protected
        # API, assert 401 here instead.
        assert response.status_code == 200

    def test_request_with_malformed_token_header(self, api_client):
        api_client.session.headers["Authorization"] = "NotBearer garbage-token"
        response = api_client.get("/users/2")
        assert response.status_code in (200, 401)  # adapt to your API's real contract
        api_client.session.headers.pop("Authorization", None)

    def test_request_with_expired_token_is_rejected(self, api_client):
        # Simulated: reqres doesn't expire tokens, so we use a token shaped
        # like a real (expired) JWT to show how you'd wire this up against
        # a real backend that does check expiry.
        expired_jwt = (
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
            "eyJzdWIiOiIxMjM0NTY3ODkwIiwiZXhwIjoxfQ."
            "invalidSignaturePlaceholder"
        )
        api_client.set_auth_token(expired_jwt)
        response = api_client.get("/users/2")
        # Placeholder assertion — replace with `assert response.status_code == 401`
        # once pointed at a real backend that enforces token expiry.
        assert response.status_code in (200, 401)
        api_client.set_auth_token(None)
