from playwright.sync_api import Page, expect

def test_logout_smoke(page: Page, login_page, header, base_url):
    login_page.open()
    login_page.login("test@test.com", "test123")

    # Logout
    header.logout()

    #  Check successful redirect
    expect(page).to_have_url(f"{base_url}/")
    expect(header.login_link).to_be_visible()