from pages.base_page import BasePage

class StoryListPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.stories = page.locator(".post-preview")

    def open(self):
        super().open("/")

