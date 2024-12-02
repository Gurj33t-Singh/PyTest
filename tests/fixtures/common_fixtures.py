# Common fixtures (e.g., authentication tokens)

import pytest

@pytest.fixture(scope="session")
def get_auth_token(get_env_data):
    """Fixture to provide authentication token."""
    return get_env_data["auth_token"]

@pytest.fixture
def base_url(get_env_data):
    """Fixture to provide the base URL."""
    return get_env_data["base_url"]
