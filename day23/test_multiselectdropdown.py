import time
import pytest
from playwright.sync_api import Page, expect


def test_multi_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple options from the dropdown - 3 ways

    #page.locator("#colors").select_option(["Red", "Blue", "Green"])   # by label
    page.locator("#colors").select_option(label=["Red", "Blue", "Green"])  # by label

    page.wait_for_timeout(4000)
