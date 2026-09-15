"""
Reusable API client used across all tests.

Wrapping `requests` in a single class means every test hits the API the same
way (same headers, same timeout, same base URL handling), and if the API's
base URL or auth scheme changes, you fix it in one place instead of in every
test file.
"""
from __future__ import annotations

import requests


class APIClient:
    def __init__(self, base_url: str, default_headers: dict | None = None, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.timeout = timeout
        self.session.headers.update(default_headers or {"Content-Type": "application/json"})

    def _url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def set_auth_token(self, token: str | None):
        """Attach or remove a bearer token for subsequent requests."""
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"
        else:
            self.session.headers.pop("Authorization", None)

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.get(self._url(endpoint), timeout=self.timeout, **kwargs)

    def post(self, endpoint: str, json: dict | None = None, **kwargs) -> requests.Response:
        return self.session.post(self._url(endpoint), json=json, timeout=self.timeout, **kwargs)

    def put(self, endpoint: str, json: dict | None = None, **kwargs) -> requests.Response:
        return self.session.put(self._url(endpoint), json=json, timeout=self.timeout, **kwargs)

    def patch(self, endpoint: str, json: dict | None = None, **kwargs) -> requests.Response:
        return self.session.patch(self._url(endpoint), json=json, timeout=self.timeout, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.delete(self._url(endpoint), timeout=self.timeout, **kwargs)
