from playwright.sync_api import sync_playwright
import logging

def run_youtube_search():
    try:
        logging.info("📥 Performing YouTube search automation")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
            )
            page = context.new_page()

            logging.info("🌐 Navigating to YouTube...")
            page.goto("https://www.youtube.com", timeout=60000)
            page.wait_for_load_state("load")

            logging.info("🔍 Waiting for search input...")
            page.wait_for_selector("input[placeholder='Search']", timeout=15000)

            logging.info("💬 Typing and submitting...")
            page.fill("input[placeholder='Search']", "relaxing music")
            page.press("input[placeholder='Search']", "Enter")

            logging.info("⏳ Waiting for results...")
            page.wait_for_selector("ytd-video-renderer", timeout=15000)

            logging.info("▶️ Clicking first video...")
            page.click("ytd-video-renderer a#thumbnail")

            logging.info("✅ Relaxing music playing.")
            page.wait_for_timeout(10000)

    except Exception as e:
        logging.error(f"❌ YouTube automation failed: {e}")
if __name__ == "__main__":
    run_youtube_search()