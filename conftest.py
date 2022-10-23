import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope='function')
def browser(request):
    user_agent = UserAgent()
    browser_name = request.config.getoption('browser')
    browser = None
    if browser_name == 'chrome':
        print('\nOpening Chrome browser...')
        options = Options()
        options.add_argument(f'user-agent={user_agent.random}')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nOpening Firefox browser...')
        options = webdriver.FirefoxOptions()
        options.set_preference('general.useragent.override', user_agent.random)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')
    yield browser
    print('\nQuitting browser...')
    browser.quit()
