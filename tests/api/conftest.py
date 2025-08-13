import logging
import pytest
from api.authentication_api import get_auth_cookie


def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

@pytest.fixture(scope="session")
def auth_data():
    session, cian_cookie = get_auth_cookie()
    session.cookies.set("_CIAN_GK", cian_cookie)
    return session