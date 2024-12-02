# Individual API tests (optional)

import pytest
from tests.utils.api_helpers import make_request
from tests.utils.validations import validate_response_status

def test_individual_api(base_url, get_auth_token):
    headers = {"Authorization": f"Bearer {get_auth_token}"}
    url = f"{base_url}/endpoint1"
    payload = {"key": "value"}
    response = make_request("POST", url, headers=headers, payload=payload)
    validate_response_status(response)
