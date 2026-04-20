import playwright
from playwright.sync_api import Page, expect


def test_xpath_locatiors(page:Page):
    # Launch the URL
    page.goto("https://demowebshop.tricentis.com/")

    #1. Absolute xpath(full xpath)
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()

    #2. Relative xpath : //tagname[@attribute='value']

    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(5000)

    #3. xpath with contains()

    products=page.locator("//h2//a[contains(@href,'computer')]")
    print("Products count:", products.count())  # counts from 1
    expect(products).to_have_count(products.count())

    print("First computer product:", products.first.text_content())

    print("Last computer product:", products.last.text_content())

    print("N-th computer product:", products.nth(2).text_content()) #nth method starts from 0


