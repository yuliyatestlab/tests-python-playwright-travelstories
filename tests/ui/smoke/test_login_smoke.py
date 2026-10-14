def test_login_smoke(login_page):
    login_page.open()
    login_page.login("test@test.com", "test123")
    assert login_page.page.url.endswith("/")