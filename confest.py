import pytest
from selene import by, be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


# test_fixtures and test_skip
@pytest.fixture(scope='function')
def browser_desktop():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1200
    browser.config._window_height = 800
    browser.open('https://github.com/')


@pytest.fixture(scope='function')
def browser_mobile():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 310
    browser.config._window_height = 516
    browser.open('https://github.com/')


# test_parametrize
chrome = pytest.fixture(params=[(1000, 900), (1500, 1200), (900, 500)])


@chrome
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def browser_config(browser_size):
    width = browser_size.param[0]
    height = browser_size.param[1]

    browser.config.window_width = width
    browser.config.window_height = height
    browser.open('https://github.com/')


