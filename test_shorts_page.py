from .pages.shorts_page import ShortsPage
import pytest


@pytest.mark.smoke
def test_user_can_watch_reels(browser):
    link = 'https://www.youtube.com/'
    page = ShortsPage(browser, link)
    page.open()
    page.go_to_shorts_page()
    page.go_full_screen()
    page.reel_container_appear()
    page.email_field_not_appear()


@pytest.mark.new
@pytest.mark.flaky(reruns=5)
def test_switch_next_and_previous_reel(browser):
    link = 'https://www.youtube.com/'
    page = ShortsPage(browser, link)
    page.open()
    page.go_to_shorts_page()
    page.go_full_screen()
    page.switch_to_next_reel()
    page.email_field_not_appear()
    page.switch_to_previous_reel()
    page.email_field_not_appear()
