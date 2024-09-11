import re

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope='function', autouse=True)
def open_page(page: Page):
    print("START")
    page.goto("https://playwright.dev/")
    yield
    print("FINISH")


def test_homepage_has_playwright_in_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    (expect(page).to_have_title(re.compile("Playwright")))
