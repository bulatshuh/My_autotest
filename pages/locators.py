from selenium.webdriver.common.by import By


class BasePageLocators:
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'ytd-button-renderer a #button[aria-label="Sign in"]')
    EXPLORE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Explore"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search-input #search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#search-icon-legacy.style-scope')
    BODY = (By.TAG_NAME, 'body')
    SHORTS_BUTTON = (By.CSS_SELECTOR, '#items .style-scope.ytd-mini-guide-renderer:nth-child(2)')


class LoginPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, '[aria-label="Email or phone"]')
    FORGOT_BUTTON = (By.CSS_SELECTOR, '[type="button"]')
    LIST_OF_LANGUAGES = (By.CSS_SELECTOR, '.VfPpkd-O1htCb .VfPpkd-TkwUic:nth-child(1)')
    RUSSIAN_LANGUAGE = (By.CSS_SELECTOR, '.MCs1Pd:nth-child(53)')


class ExplorePageLocators:
    DESTINATION_BAR = (By.CSS_SELECTOR, '#destination-buttons.style-scope')


class SearchPageLocators:
    SEARCH_RESULTS = (By.CSS_SELECTOR, '#container .style-scope.ytd-search')
    CHANNEL_LINK = (By.CSS_SELECTOR, '#info-section #main-link #info #channel-title')


class ShortsPageLocators:
    REEL_VIDEO_CONTAINER = (By.CSS_SELECTOR, '#shorts-container #shorts-inner-container'
                                             ' .reel-video-in-sequence:nth-child(2)')
    NEXT_REEL_BUTTON = (By.CSS_SELECTOR, '.navigation-button.style-scope.ytd-shorts:nth-child(4) '
                                         '.style-scope.ytd-shorts')
    PREVIOUS_REEL_BUTTON = (By.CSS_SELECTOR, '.navigation-button.style-scope.ytd-shorts:nth-child(1) '
                                            '.style-scope.ytd-shorts')
