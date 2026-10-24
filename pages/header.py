from playwright.sync_api import Page

class Header:
    def __init__(self, page: Page):
        self.page = page
        self.logout_button = page.locator("#logout")
        self.login_link = page.locator("#login")

    def logout(self):
        self.logout_button.click()