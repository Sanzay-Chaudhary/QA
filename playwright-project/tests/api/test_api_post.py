from playwright.sync_api import sync_playwright


def test_create_user():

    with sync_playwright() as p:

        request_context = p.request.new_context()

        payload = {
            "name": "Sanjay",
            "job": "QA Engineer"
        }

        response = request_context.post(
            "https://jsonplaceholder.typicode.com/users",
            data=payload
        )

        print("Status:", response.status)

        response_body = response.json()

        print("Response:", response_body)

        assert response.status in [200, 201]

        print("Name:", response_body.get("name"))

        print("✅ POST API test passed")