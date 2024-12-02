# Common fixtures (e.g., authentication tokens)
import pytest
from urllib.parse import urljoin

from tests.utils import api_helpers

@pytest.fixture
def get_auth_token(get_env_data):
    """Fixture to provide authentication token."""

    endpoint = "/user/oauth/token"
    url = urljoin(get_env_data["host"], endpoint)

    headers = {
        "authorization": "Basic ZWdvdi11c2VyLWNsaWVudDo="
    }

    api_helpers.make_request("POST", url, headers, 
                             payload="", is_json=False)
    return get_env_data["auth_token"]

@pytest.fixture
def base_url(get_env_data):
    """Fixture to provide the base URL."""
    return get_env_data["base_url"]
