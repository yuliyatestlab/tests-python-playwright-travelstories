import pytest
from pages.login_page import LoginPage
from pages.header import Header
from pages.registration_page import RegistrationPage
from pages.story_list_page import StoryListPage
from pages.story_page import StoryPage
from api.client import ApiClient

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def header(page):
    return Header(page)

@pytest.fixture
def registration_page(page):
    return RegistrationPage(page)

@pytest.fixture
def story_list_page(page):
    return StoryListPage(page)

@pytest.fixture
def story_page(page):
    return StoryPage(page)

@pytest.fixture
def api(base_url):
    return ApiClient(base_url)


