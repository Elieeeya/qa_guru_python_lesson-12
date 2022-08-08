"""
С использованием indirect
"""

from confest import *

@pytest.mark.parametrize("browser_size", [(1100, 1200)], indirect=True)
def test_github_desktop(browser_size):
    browser.open('https://github.com/')
    s('//div[contains(@class, "HeaderMenu")]//a[contains(text(), "Sign up")]').click()


@pytest.mark.parametrize("browser_size", [(414, 896)], indirect=True)
def test_github_mobile(browser_size):
    s('[class="octicon octicon-three-bars"]').click()
    s('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()
