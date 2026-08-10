import json


def test_intercept_request(page):

    def handle_request(route):

        print("Request intercepted")

        route.continue_()

    page.route(
        "**/users/1",
        handle_request
    )

    page.goto(
        "https://jsonplaceholder.typicode.com/users/1"
    )


def test_block_request(page):

    def handle_request(route):

        print("Request blocked")

        route.abort()

    page.route(
        "**/users/2",
        handle_request
    )

    page.goto(
        "https://jsonplaceholder.typicode.com/users/2"
    )


def test_mock_response(page):

    mock_response = {
        "id": 999,
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }

    def handle_request(route):

        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(mock_response)
        )

    page.route(
        "**/users/3",
        handle_request
    )

    page.goto(
        "https://jsonplaceholder.typicode.com/users/3"
    )