from pages.base_page import BasePage

class StoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.heading = page.locator(".post-heading")