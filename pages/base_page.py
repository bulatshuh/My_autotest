from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, browser, link, timeout=5):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def go_full_screen(self):
        self.browser.maximize_window()

    def go_to_login_page(self):
        sign_in_button = self.browser.find_element(*BasePageLocators.SIGN_IN_BUTTON)
        sign_in_button.click()

    def go_to_explore_page(self):
        explore_button = self.browser.find_element(*BasePageLocators.EXPLORE_BUTTON)
        explore_button.click()

    def go_to_shorts_page(self):
        shorts_button = self.browser.find_element(*BasePageLocators.SHORTS_BUTTON)
        shorts_button.click()

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def switch_to_first_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[0])

    def open_new_tab(self):
        self.browser.execute_script("window.open('');")

    def close_current_tab(self):
        self.browser.close()

    def scroll_down_slowly_and_scrape(self, path_for_screenshot):
        original_size = self.browser.get_window_size()
        required_width = self.browser.execute_script('return document.body.parentNode.scrollWidth')
        required_height = self.browser.execute_script('return document.body.parentNode.scrollHeight')

        html = self.browser.find_element(*BasePageLocators.HTML)

        while original_size['height'] < required_height:
            html.send_keys(Keys.PAGE_DOWN)
            original_size['height'] += original_size['height']

        html.send_keys(Keys.HOME)
        self.browser.set_window_size(required_width, required_height)

        self.browser.save_screenshot(path_for_screenshot)
        self.browser.set_window_size(original_size['width'], original_size['height'])

    def quit(self):
        self.browser.quit()
