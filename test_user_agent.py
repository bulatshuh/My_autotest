import pytest
from .pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


@pytest.mark.new
def test_check_user_agent(browser):
    link = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
    page = BasePage(browser, link)
    page.open()
    page.go_full_screen()
