from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ShortsPageLocators


class ShortsPage(BasePage):
    def reel_container_appear(self):
        assert self.is_element_present(*ShortsPageLocators.REEL_VIDEO_CONTAINER), 'Reels doesn\'t appear'

    def email_field_not_appear(self):
        assert self.is_not_element_present(*LoginPageLocators.EMAIL_FIELD), 'Email field appears'

    def switch_to_next_reel(self):
        next_reel_button = self.browser.find_element(*ShortsPageLocators.NEXT_REEL_BUTTON)
        next_reel_button.click()

    def switch_to_previous_reel(self):
        previous_reel_button = self.browser.find_element(*ShortsPageLocators.PREVIOUS_REEL_BUTTON)
        previous_reel_button.click()
