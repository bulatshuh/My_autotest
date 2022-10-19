from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_email_field(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), 'No email field presented'

    def should_not_be_search_field(self):
        assert self.is_not_element_present(*BasePageLocators.SEARCH_FIELD), 'Search field presented, but shouldn\'t be'

    def should_be_create_button(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_BUTTON), 'No FORGOT button'

    def switch_to_russian(self):
        list_of_lang_button = self.browser.find_element(*LoginPageLocators.LIST_OF_LANGUAGES)
        list_of_lang_button.click()
        russian_lang = self.browser.find_element(*LoginPageLocators.RUSSIAN_LANGUAGE)
        russian_lang.click()
