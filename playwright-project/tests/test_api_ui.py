def test_api_ui(page):
    # Test API request
    response = page.request.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status == 200
    user = response.json()
    expected_name = user["name"]
    print("Expected name:", expected_name)

    # Test UI
    page.goto("https://the-internet.herokuapp.com/login")
    assert page.url.endswith("/login")