import requests

class APIClient:
    def get(self, url):
        return requests.get(url)
    
    def post(self, url, payload):
        return requests.post(url, json=payload)
    
    def validate_status_code(self, response, expected):
        assert response.status_code == expected

    def get_json(self, response):
        return response.json()