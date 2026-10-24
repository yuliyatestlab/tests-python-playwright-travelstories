import uuid
from playwright.sync_api import Page, expect

def test_registration_smoke(page: Page, registration_page, base_url):
    registration_page.open()

    #  Check registration form is visible
    expect(registration_page.email).to_be_visible()
    expect(registration_page.password).to_be_visible()
    expect(registration_page.name).to_be_visible()
    expect(registration_page.profile_image).to_be_visible()

    #  Register with a unique email
    email = f"test_{uuid.uuid4().hex[:8]}@gmail.com"
    registration_page.register(email, "test1234", "Mary")

    #  Check successful redirect
    expect(page).to_have_url(f"{base_url}/")
    expect(page.locator("#logout")).to_be_visible()
