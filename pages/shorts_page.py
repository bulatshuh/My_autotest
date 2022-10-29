from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ShortsPageLocators


class ShortsPage(BasePage):
    def reel_container_appear(self):
        assert self.is_element_present(*ShortsPageLocators.REEL_VIDEO_CONTAINER), 'Reels doesn\'t appear'

    def email_field_not_appear(self):
        assert self.is_not_element_present(*LoginPageLocators.EMAIL_FIELD), 'Email field appears'
