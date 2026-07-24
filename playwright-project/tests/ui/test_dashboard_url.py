def test_dashboard_url(logged_in_page):
     assert "secure" in logged_in_page.url