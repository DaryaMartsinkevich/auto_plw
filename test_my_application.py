import re
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope='function', autouse=True)
def open_page(page: Page):
    print("START")
    page.goto("https://demoqa.com/dynamic-properties")
    yield
    print("FINISH")


def test_homepage_has_playwright_in_title(page: Page):
    # скриншот локатора
    page.locator('[src="/images/Toolsqa.jpg"]').screenshot(path="locator_screenshot.png")
    # скриншот всей страницы
    page.screenshot(path="PAGE_FULL_screenshot.png", full_page=True)
    # скриншот видимой области
    page.screenshot(path="screenshot.png")
