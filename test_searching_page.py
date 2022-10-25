import pytest
from .pages.searching_page import SearchPage


@pytest.mark.smoke
def test_search(browser):
    link = 'https://www.youtube.com/'
    page = SearchPage(browser, link)
    page.open()
    page.search_request()


@pytest.mark.new
@pytest.mark.flaky(reruns=5)
def test_search_and_open_channel(browser):
    link = 'https://www.youtube.com/'
    page = SearchPage(browser, link)
    page.open()
    page.search_request()
    page.open_channel()
