from playwright.sync_api import sync_playwright


def test_get_users():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        response = request_context.get(
            "https://jsonplaceholder.typicode.com/users"
        )

        print("Status:", response.status)

        data = response.json()

        print("First user:", data[0])

        assert response.status == 200

        print("Test passed")