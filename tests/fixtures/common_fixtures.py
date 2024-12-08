# Common fixtures (e.g., authentication tokens)
import pytest
from urllib.parse import urljoin

from tests.utils import api_helpers

@pytest.fixture
def get_auth_token(get_env_data, get_endpoints):
    """Fixture to provide authentication token."""

    endpoint = get_endpoints["authToken"]["oauth"]

    url = urljoin(get_env_data["host"], endpoint)

    body = {
              "username": "SUPERUSER",
              "password": "eGov@123",
              "grant_type": "password",
              "scope": "read",
              "tenantId": "pg",
              "userType": "EMPLOYEE"
            }

    response = api_helpers.make_request("POST", url, payload=body, is_json=False)

    return response.json()["access_token"]
