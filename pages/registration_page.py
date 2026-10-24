from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email = page.locator("#email")
        self.password = page.locator("#password")
        self.name = page.locator("#name")
        self.profile_image = page.get_by_role("button", name="Profile Image")
        self.submit = page.locator("#submit")

    def open(self):
        super().open("/register")

    def register(self, email, password, name):
        self.email.fill(email)
        self.password.fill(password)
        self.name.fill(name)
        self.submit.click()