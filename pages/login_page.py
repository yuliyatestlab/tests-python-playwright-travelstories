from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email = page.get_by_label("Email")
        self.password = page.get_by_label("Password")
        self.submit = page.get_by_role("button", name="LOG IN")
        self.error = page.locator(".error-message")

    def open(self):
        super().open("/login")

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.submit.click()

