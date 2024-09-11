import re
import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright


class DemoQA:
    def __init__(self, page):
        self.page: Page = page
        self.logo = self.page.locator('[src="/images/Toolsqa.jpg"]')
        self.logo = self.page.locator('css=[src="/images/Toolsqa.jpg"]')
        self.logo = self.page.locator('xpath=//*[@src="/images/Toolsqa.jpg"]')
        self.submit = self.page.get_by_role("button", name="Submit")     #локатор который отвечате по роле того что можем сделать на странице
        self.text = self.page.get_by_text("Student Registration Form")
        self.text = self.page.locator("text=Student Registration Form")
        self.label = self.page.get_by_label("Name")
        self.placeholder = self.page.get_by_placeholder("First Name")
        self.alt = self.page.get_by_alt_text("Build PlayWright tests with AI")
        self.data_testid = self.page.get_by_test_id("123456")

    def open_page(self):
        self.page.goto('https://demoqa.com/')

    def assert_that_logo_is_visible(self):
        expect(self.logo).to_be_visible()


def test_run(page: Page):
    demo_qa = DemoQA(page)
    demo_qa.open_page()
    demo_qa.assert_that_logo_is_visible()
