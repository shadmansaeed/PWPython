import time
import pytest
from playwright.sync_api import Page, expect


def test_multi_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple options from the dropdown - 3 ways

    # page.locator("#colors").select_option(["Red", "Blue", "Green"])   # by label
    # page.locator("#colors").select_option(label=["Red", "Blue", "Green"])  # by label

    # page.locator("#colors").select_option(value=["red", "white", "green"])  # by value

    #page.locator("#colors").select_option(index=[2, 4])   # by index

    dropdown_options=page.locator("#colors>option")
    expect(dropdown_options).to_have_count(7 )

    options_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    # print countries using loop
    for option in options_text:
        print(option)

    page.wait_for_timeout(4000)

