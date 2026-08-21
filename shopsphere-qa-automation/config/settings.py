import os

from dotenv import load_dotenv

from config.environments import ENVIRONMENTS

load_dotenv()

ENV = os.getenv("ENV", "qa")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"

if ENV not in ENVIRONMENTS:
    raise ValueError(
        f"Invalid environment '{ENV}'. "
        f"Supported environments: {list(ENVIRONMENTS.keys())}"
    )

BASE_URL = ENVIRONMENTS[ENV]["base_url"]
API_BASE_URL = ENVIRONMENTS[ENV]["api_base_url"]