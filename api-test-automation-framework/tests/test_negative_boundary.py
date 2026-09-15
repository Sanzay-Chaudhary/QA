import allure
import pytest


@allure.feature("Negative & Boundary Testing")
class TestPagination:
    @pytest.mark.parametrize("page", [1, 2, 100, -1, 0])
    def test_pagination_boundary_values(self, api_client, page):
        response = api_client.get("/users", params={"page": page})
        assert response.status_code == 200
        body = response.json()
        if page in (100, -1, 0):
            # Out-of-range / invalid pages should return an empty data set,
            # not an error and not stale data from another page.
            assert body["data"] == []
        else:
            assert len(body["data"]) > 0

    def test_per_page_upper_boundary(self, api_client):
        response = api_client.get("/users", params={"per_page": 10000})
        assert response.status_code == 200
        # API should cap results rather than choke on a huge request.
        assert response.json()["total_pages"] >= 1


@allure.feature("Negative & Boundary Testing")
class TestHeadersAndBusinessLogic:
    def test_response_content_type_is_json(self, api_client):
        response = api_client.get("/users/2")
        assert "application/json" in response.headers["Content-Type"]

    def test_nonexistent_endpoint_returns_404(self, api_client):
        response = api_client.get("/this-endpoint-does-not-exist")
        assert response.status_code == 404

    def test_delayed_response_still_completes_within_timeout(self, api_client):
        # reqres.in supports ?delay=N to simulate slow backends.
        response = api_client.get("/users", params={"delay": 2})
        assert response.status_code == 200

    def test_created_resource_id_is_unique_per_request(self, api_client, new_user_payload):
        first = api_client.post("/users", json=new_user_payload).json()
        second = api_client.post("/users", json=new_user_payload).json()
        # Business rule: two independently created resources must not
        # collide on ID even with identical payloads.
        assert first["id"] != second["id"]
