from playwright.sync_api import expect

def test_view_story_page_loads(story_list_page, story_page):
    story_list_page.open()
    expect(story_list_page.stories.first).to_be_visible()

    story_list_page.open_first_story()

    expect(story_page.heading).to_be_visible()