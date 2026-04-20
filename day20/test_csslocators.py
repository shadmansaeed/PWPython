'''

tag id -----  tag#id
tag class -----  tag.class
tag with any other attribute --- tag[attribute=value]
tag class attribute   ----- tag.class[attribute=value]


note: here tag is optional for all
'''
import time

import pytest
from playwright.sync_api import sync_playwright, Page, expect

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(ignore_https_errors=True)  # 🔥 SSL error ignore
        page = context.new_page()
        yield page
        browser.close()

def test_verify_css_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(2000)

    #tag id
    # page.locator("input#small-searchterms").fill("T-Shirts")
    # page.locator("#small-searchterms").fill("T-Shirts")
    # page.wait_for_timeout(2000)

    #or
    #tag class
    # page.locator("input.search-box-text").fill("T-Shirts")
    # page.locator(".search-box-text").fill("T-Shirts")
    # page.wait_for_timeout(3000)

    #or
    #tag attribute
    # page.locator("input[name=q]").fill("T-Shirts")
    # page.locator("[name=q]").fill("T-Shirts")
    # page.wait_for_timeout(3000)

    #or
    #tag class attribute
    page.locator("input.search-box-text[value='Search store']").fill("T-Shirts")
    # note: we cannot use double quatation within a double quatation, we need to use single quatation
    page.wait_for_timeout(3000)



