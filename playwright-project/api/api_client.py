import requests

class APIClient:
    def get(self, url):
        return requests.get(url)
    
    def post(self, url, payload):
        return requests.post(url, json=payload)
    
    