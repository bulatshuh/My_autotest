import pytest
from .pages.base_page import BasePage


@pytest.mark.new
def test_take_long_screenshot(headless_option_browser):
    url = 'https://www.youtube.com/'
    path = 'C:/Users/Bulatshuh/My_autotest/tmp/screen.png'

    page = BasePage(headless_option_browser, url)
    page.open()
    page.scroll_down_slowly_and_scrape(path)
