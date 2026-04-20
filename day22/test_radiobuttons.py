import time

import pytest
from playwright.sync_api import Page, expect


def test_inputbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    male_radio = page.locator("#male")

    # visibility of the element and enable or not
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    # male radio button should not be checked (default)
    expect(male_radio).not_to_be_checked()

    # select/check radio button
    male_radio.check()
    time.sleep(3)

    # male radio button should be checked
    expect(male_radio).to_be_checked()

