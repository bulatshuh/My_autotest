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

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def switch_to_first_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[0])

    def open_new_tab(self):
        self.browser.execute_script("window.open('');")

    def close_current_tab(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()
