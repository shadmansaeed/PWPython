'''


'''
import time

from playwright.sync_api import Page, expect


#  page.get_by_alt_text()c
#  page.get_by_text()
#   page.getByRole
# 4. page.get_by_label
# 5. page.get_by_placeholder
# 6. page.get_by_title()
# 7. page.get_by_test_id()

def test_verify_pwlocators(page: Page):
    #page.goto("https://demo.nopcommerce.com/")
    # time.sleep(5) #
    #page.wait_for_timeout(4000)
    # 1 page.get_by_alt_text()
    #logo=page.get_by_alt_text("nopCommerce demo store")
    #expect(logo).to_be_visible()
    #page.close()
    #expect(page.get_by_alt_text("nopCommerce demo store")).to_be_visible()  -- this is single page assertion
    # 2 page.get_by_text()
    #expect(page.get_by_text("Welcome to our store")).to_be_visible() # full text

    # page.get_by_role()
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")

    page.wait_for_timeout(5000)
    #expect(page.get_by_role("heading", name="Register")).to_be_visible()

    # 4. page.get_by_label()
    page.get_by_label("First name:").fill("shadman")
    page.get_by_label("Last name:").fill("saeed")
    page.get_by_label("Email:").fill("nrbc.qa@gmail.com")
    page.wait_for_timeout(3000)

    # 5. page.get_by_placeholder()
    page.get_by_placeholder("Search store").fill("Apple MacBook")
    page.wait_for_timeout(5000)

    # 6. page.get_by_title()

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    page.wait_for_timeout(5000)

    # 7. page.get_by_test_id()

    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")

    



