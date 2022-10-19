import pytest
from .pages.login_page import LoginPage


@pytest.mark.smoke
class TestLoginForm:
    def test_email_field_appears(self, browser):
        link = 'https://www.youtube.com/'
        page = LoginPage(browser, link)
        page.open()
        page.go_full_screen()
        page.go_to_login_page()
        page.should_be_email_field()
        page.should_not_be_search_field()

    def test_create_account_button_exist(self, browser):
        link = 'https://www.youtube.com/'
        page = LoginPage(browser, link)
        page.open()
        page.go_full_screen()
        page.go_to_login_page()
        page.should_be_create_button()


@pytest.mark.new
@pytest.mark.flaky(reruns=5)
def test_change_language(browser):
    link = 'https://www.youtube.com/'
    page = LoginPage(browser, link)
    page.open()
    page.go_full_screen()
    page.go_to_login_page()
    page.scroll_down()
    page.switch_to_russian()
