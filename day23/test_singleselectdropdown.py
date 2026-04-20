import time
import pytest
from playwright.sync_api import Page, expect


def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways to select option from the dropdown
    #page.locator("#country").select_option("Brazil")  # by label  (both are same)
    page.locator("#country").select_option(label="Brazil")  # by label
    page.wait_for_timeout(4000)

    page.locator("#country").select_option("germany")  # by value (both are same)
    page.locator("#country").select_option(value="germany")  # by value
    page.wait_for_timeout(4000)

    page.locator("#country").select_option(index=4)  # index start from 0
    page.wait_for_timeout(4000)

    # check number of options in dropdown
    dropdown_options=page.locator("#country>option")

    expect(dropdown_options).to_have_count(10)
    options_text=[text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    # print countries using loop
    for option in options_text:
        print(option)

    page.wait_for_timeout(4000)







