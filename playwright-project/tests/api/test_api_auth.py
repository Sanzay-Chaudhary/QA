from playwright.sync_api import sync_playwright


def test_fake_auth():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        # Simulated token
        token = "fake_token_123"

        headers = {
            "Authorization": f"Bearer {token}"
        }

        print("Generated Token:", token)

        print("Headers:", headers)

        assert "Bearer" in headers["Authorization"]

        print("✅ Authentication test passed")