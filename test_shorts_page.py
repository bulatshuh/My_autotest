from .pages.shorts_page import ShortsPage
import pytest


@pytest.mark.new
def test_user_can_watch_reels(browser):
    link = 'https://www.youtube.com/'
    page = ShortsPage(browser, link)
    page.open()
    page.go_to_shorts_page()
    page.go_full_screen()
    page.reel_container_appear()
    page.email_field_not_appear()
