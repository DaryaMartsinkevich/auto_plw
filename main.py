import re
import pytest
from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright


def run(playwright):
    ff = playwright.firefox     #создали браузер
    browser = ff.launch()       #создали браузер-контекст
    page: Page = browser.new_page()     #вкладка
    page.goto('https://demoqa.com/')

    print('Hello World')
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
