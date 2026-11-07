import os
import pytest

pytestmark = pytest.mark.smoke

@pytest.mark.parametrize("path", ["/", "/about", "/contact", "/login", "/register"])
def test_public_pages_return_200(api, path):
    assert api.get(path).status_code == 200

def test_login_with_valid_credentials(api):
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")
    if not email or not password:
        pytest.skip("TEST_EMAIL / TEST_PASSWORD are not set")

    response = api.login(email, password)

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")