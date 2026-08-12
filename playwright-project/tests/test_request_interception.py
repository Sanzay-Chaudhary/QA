def test_backend_failure(page):

    def handle_request(route):

        route.fulfill(
            status=503,
            content_type="application/json",
            body='{"error": "Service unavailable"}'
        )

    page.route(
        "**/users",
        handle_request
    )

    response = page.goto(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status == 503