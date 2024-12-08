# Individual API tests (optional)

import pytest
from tests.utils.api_helpers import make_request
from tests.utils.validations import validate_response_status
from tests.fixtures.common_fixtures import get_auth_token

def test_individual_api(get_auth_token):
    
    print(get_auth_token)