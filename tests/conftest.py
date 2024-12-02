import pytest
import json
from tests.utils.api_helpers import get_json

@pytest.fixture(scope="session", autouse=True)
def get_env_data():
    """Load environment configuration data."""
    with open("tests/config/env_config.json") as f:
        env_config = json.load(f)
    return env_config
