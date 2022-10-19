import pytest
from .pages.explore_page import ExplorePage


@pytest.mark.smoke
def test_destination_bar_appears(browser):
    link = 'https://www.youtube.com/'
    page = ExplorePage(browser, link)
    page.open()
    page.go_to_explore_page()
    page.destination_bar_appeared()
