from playwright.sync_api import sync_playwright

def handler(event, context):
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--disable-gpu", "--single-process", "--no-zygote"])
        page = browser.new_page()
        page.goto("https://example.com/")
        browser.close()
