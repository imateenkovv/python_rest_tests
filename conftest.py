import pytest
from core.api_client import ApiClient


@pytest.fixture(scope='session')
def api_client():
    return ApiClient()
