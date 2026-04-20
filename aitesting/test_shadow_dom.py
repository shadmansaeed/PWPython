import time

from playwright.sync_api import Page, expect


def test_example(page: Page):
    page.goto("https://books-pwakit.appspot.com/")

    # await page.locator('#input')
    # page.locator("#input")
    # page.locator()
    page.locator("#input").fill("Welcome to the Team")
    # expect(page.get_by_role("button", name="Menu")).to_be_visible()
    time.sleep(5)
