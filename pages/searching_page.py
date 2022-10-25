from .base_page import BasePage
from .locators import BasePageLocators
from .locators import SearchPageLocators


class SearchPage(BasePage):
    def search_request(self):
        search_field = self.browser.find_element(*BasePageLocators.SEARCH_FIELD)
        search_field.send_keys('qwerty')
        search_button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON)
        search_button.click()
        assert self.browser.find_element(*SearchPageLocators.SEARCH_RESULTS), 'Search results not presented'

    def open_channel(self):
        channel_link = self.browser.find_element(*SearchPageLocators.CHANNEL_LINK)
        channel_link.click()
