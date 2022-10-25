import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser')
    browser = None
    if browser_name == 'chrome':
        print('\nOpening Chrome browser...')
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('\nOpening Firefox browser...')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')
    yield browser
    print('\nQuitting browser...')
    browser.quit()
