import time

from playwright.sync_api import Page, expect

def test_opencart(page: Page):
    page.goto("http://localhost/opencart/upload/")
    time.sleep(3)
    page.locator("span:has-text('My Account')").click()
    time.sleep(2)
    page.get_by_role("link", name="Register").click()
    time.sleep(2)
    page.get_by_role("textbox", name="First Name").fill("shadman")
    page.get_by_role("textbox", name="Last Name").fill("saeed")
    time.sleep(2)
    page.get_by_role("textbox", name="E-Mail").fill("nrbc.qa@gmail.com")
    time.sleep(2)
    page.get_by_role("textbox", name="Password").fill("Ur@123456")
    time.sleep(3)


