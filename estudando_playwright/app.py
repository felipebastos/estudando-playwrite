from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://google.com')

    parsed = BeautifulSoup(page.content(), 'html.parser')

    print(parsed.span)

    browser.close()