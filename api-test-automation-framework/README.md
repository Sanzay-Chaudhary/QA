# API Test Automation Framework

An end-to-end API automation framework built with **Python, Pytest, and Requests**, designed to practice real-world QA engineering — not just "does the endpoint respond," but does it behave correctly under valid, invalid, and edge-case conditions.

Tests run against [reqres.in](https://reqres.in), a free mock REST API, so the project runs immediately with no backend setup required.

## What this demonstrates

- **Reusable API client architecture** (`api_client/base_client.py`) — a single wrapper around `requests` supporting GET/POST/PUT/PATCH/DELETE, so auth, headers, and base-URL logic live in one place instead of being duplicated across tests.
- **Data-driven testing** via Pytest fixtures and `@pytest.mark.parametrize` for positive, negative, and boundary cases (empty payloads, invalid pagination, oversized requests).
- **Authentication test matrix** covering valid, invalid, missing, and expired credentials.
- **Response validation beyond status codes** — JSON schema validation (`schemas/`), header checks, and business-logic assertions (e.g., uniqueness of created resource IDs).
- **CI/CD integration** — GitHub Actions runs the full suite on every push and pull request.
- **Allure reporting** for readable, shareable HTML test reports (published to GitHub Pages via CI).

## Project structure

```
api-test-automation-framework/
├── api_client/
│   └── base_client.py       # Reusable HTTP client
├── schemas/
│   └── user_schema.py       # JSON schemas for response validation
├── tests/
│   ├── conftest.py          # Shared fixtures (client, auth, test data)
│   ├── test_users_crud.py   # GET/POST/PUT/PATCH/DELETE coverage
│   ├── test_auth_matrix.py  # Valid/invalid/missing/expired credential tests
│   └── test_negative_boundary.py
├── .github/workflows/ci.yml # CI pipeline
├── pytest.ini
└── requirements.txt
```

## Getting started

```bash
git clone https://github.com/<your-username>/api-test-automation-framework.git
cd api-test-automation-framework
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run the suite:

```bash
pytest
```

Run in parallel:

```bash
pytest -n auto
```

Generate an Allure report (requires the [Allure commandline](https://allurereport.org/docs/gettingstarted-installation/)):

```bash
allure serve allure-results
```

## Tech stack

Python · Pytest · Requests · Postman · GitHub Actions · Allure · jsonschema

## Notes on the demo API

Some tests include comments where reqres.in's actual behavior (e.g., not rejecting incomplete payloads) differs from what a real production API would typically enforce. Those tests document the real contract of the API under test — swap the base URL and adjust the assertions to point this framework at your own API.

## Possible extensions

- Contract testing with a real backend
- Load testing hooks (Locust/k6) reusing the same client
- Mutation testing to validate test suite strength
