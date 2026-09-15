import pytest

from api_client.base_client import APIClient

# reqres.in is a free mock REST API that fully simulates CRUD + auth
# responses (2xx, 4xx) without needing a real backend, so it's ideal
# for demonstrating a testing framework end-to-end.
BASE_URL = "https://reqres.in/api"


@pytest.fixture(scope="session")
def api_client() -> APIClient:
    """A shared, unauthenticated client for the whole test session."""
    # The public /api/users, /api/login etc. demo endpoints require no
    # authentication at all — only reqres's persistent /api/collections/*
    # endpoints (a separate, paid-tier feature) need an x-api-key.
    return APIClient(base_url=BASE_URL, default_headers={
        "Content-Type": "application/json",
    })


@pytest.fixture()
def authenticated_client(api_client) -> APIClient:
    """A client pre-loaded with a valid bearer token."""
    response = api_client.post("/login", json={
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    })
    token = response.json()["token"]
    api_client.set_auth_token(token)
    yield api_client
    api_client.set_auth_token(None)


@pytest.fixture()
def new_user_payload():
    """A valid payload for creating a user, reused by several tests."""
    return {"name": "Jane Doe", "job": "QA Engineer"}
