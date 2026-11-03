from playwright.sync_api import expect

def test_story_list_visible(story_list_page):
    story_list_page.open()

    expect(story_list_page.stories.first).to_be_visible()
    assert story_list_page.stories.count() > 0, "No stories are displayed"

