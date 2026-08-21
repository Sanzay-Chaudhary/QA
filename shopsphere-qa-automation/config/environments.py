import os

ENVIRONMENTS = {
    "dev": {
        "base_url": os.getenv("DEV_BASE_URL", "https://example.com"),
        "api_base_url": os.getenv(
            "DEV_API_BASE_URL",
            "https://api.example.com"
        ),
    },
    "qa": {
        "base_url": os.getenv("QA_BASE_URL", "https://example.com"),
        "api_base_url": os.getenv(
            "QA_API_BASE_URL",
            "https://api.example.com"
        ),
    },
    "staging": {
        "base_url": os.getenv(
            "STAGING_BASE_URL",
            "https://example.com"
        ),
        "api_base_url": os.getenv(
            "STAGING_API_BASE_URL",
            "https://api.example.com"
        ),
    },
}