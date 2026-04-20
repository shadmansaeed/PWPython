import pytest
from playwright.sync_api import Page, expect


def test_inputbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    text_box = page.locator("#name")

    # visibility of the element and enable or not
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()

    # check the attribute of the elements
    expect(text_box).to_have_attribute("maxlength", "15")

    # get an attribute of the element
    maxlength = text_box.get_attribute("maxlength")
    print("maximum length of inputbox:", maxlength)

    # fill the text
    text_box.fill("john kenedy")

    # get the input value from inputbox
    enterdvalue= text_box.input_value()
    print("value entered is:", enterdvalue)
    page.wait_for_timeout(5000)
