import pytest
from pages.login_page import LoginPage
from pages.header import Header

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def header(page):
    return Header(page)
