import pytest
from .pages.searching_page import SearchPage


@pytest.mark.new
def test_search(browser):
    link = 'https://www.youtube.com/'
    page = SearchPage(browser, link)
    page.open()
    page.search_request()
