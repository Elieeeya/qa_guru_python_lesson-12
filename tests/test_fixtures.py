"""
Разные фикстуры для каждого теста
"""


from confest import *


def test_github_desktop(browser_desktop):
    browser.open('https://github.com/')
    s('//div[contains(@class, "HeaderMenu")]//a[contains(text(), "Sign up")]').click()


def test_github_mobile(browser_mobile):
    s('[class="octicon octicon-three-bars"]').click()
    s('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()
