"""
Пропуск тестов
"""

from confest import *


def test_github_desktop(browser_config):
    if browser.config.window_width < 1100:
        pytest.skip('mobile version')
    s('//div[contains(@class, "HeaderMenu")]//a[contains(text(), "Sign up")]').click()


def test_github_mobile(browser_config):
    if browser.config.window_height > 1100:
        pytest.skip('browser version')
    s('[class="octicon octicon-three-bars"]').click()
    s('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()
