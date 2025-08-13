import pytest
from api.authentication_api import get_auth_cookie


@pytest.fixture(scope="module")
def auth_data():
    session, cookie = get_auth_cookie()
    return session, cookie