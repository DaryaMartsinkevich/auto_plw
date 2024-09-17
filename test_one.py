import re

import allure
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

    @allure.step("Open page demoqa.com")
    def open_page(self):
        self.page.goto('https://demoqa.com/')

    @allure.step("Assert that logo is visible")
    def assert_that_logo_is_visible(self):
        self.logo.screenshot(path='scrn.png')
        expect(self.logo).to_be_visible()
        allure.attach.file(
            "scrn.png",
            name="scrn",
            attachment_type=allure.attachment_type.PNG
        )


@allure.feature("MAIN feature")
@allure.title("MAIN TITLE")
def test_run(page: Page):
    demo_qa = DemoQA(page)
    demo_qa.open_page()
    demo_qa.assert_that_logo_is_visible()