# pre-requisite for asynchronous edecution
# install pytest-asyncio
# command: pip install pytest-asyncio
import pytest
from playwright.async_api import Page, expect, async_playwright


@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        mypage = await browser.new_page()
        await mypage.goto("http://www.automationpractice.pl/index.php")
        await expect(mypage).to_have_url("http://www.automationpractice.pl/index.php")  # expected url

    # page.goto("http://www.automationpractice.pl/index.php")  # passing url
    # myurl= page.url
