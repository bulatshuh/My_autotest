from .base_page import BasePage
from .locators import ExplorePageLocators


class ExplorePage(BasePage):
    def destination_bar_appeared(self):
        assert self.is_element_present(*ExplorePageLocators.DESTINATION_BAR), 'Bar don\'t appear'
