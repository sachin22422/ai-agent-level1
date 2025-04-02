# app/actions/amazon_action.py

from playwright.sync_api import sync_playwright
import logging

def run_amazon_search():
    try:
        logging.info("🔍 Starting Amazon search automation")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            print("🌐 Opening Amazon...")
            page.goto("https://www.amazon.in", timeout=60000)
            page.wait_for_timeout(3000)  # wait a moment for full page render

            print("🔎 Searching iPhone 15...")
            page.fill("input[name='field-keywords']", "iPhone 15")
            page.click("input[type='submit']")

            page.wait_for_selector("div.s-main-slot")
            print("✅ Search completed!")

            page.wait_for_timeout(5000)

    except Exception as e:
        logging.error(f"❌ Amazon automation failed: {e}")
if __name__ == "__main__":
    run_amazon_search()
