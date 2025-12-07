"""
Basic Browser Example
Demonstrates simple browser automation with QA Browser
"""

import asyncio
from qa_browser import BrowserEnv, BrowseURLAction, BrowseInteractiveAction, browse


async def main():
    print("🌐 Initializing browser...")
    browser = BrowserEnv()

    try:
        # Example 1: Navigate to Google.com and take a screenshot
        print("\n📍 Example 1: Navigating to Google.com...")
        action = BrowseURLAction(url="https://www.google.com")
        observation = await browse(action, browser)

        print(f"✅ Visited: {observation.url}")
        print(f"📸 Screenshot: {observation.screenshot[:100]}...")  # Show first 100 chars of base64
        print(f"📄 Content preview: {observation.content[:200]}...")
        
        if observation.error:
            print(f"❌ Error: {observation.last_browser_action_error}")
        else:
            print("✅ Screenshot captured successfully!")

        # Example 2: Navigate to another website
        print("\n📍 Example 2: Navigating to Example.com...")
        action = BrowseURLAction(url="https://example.com")
        observation = await browse(action, browser)

        print(f"✅ Visited: {observation.url}")
        print(f"📸 Screenshot: {observation.screenshot[:100]}...")
        print(f"📄 Content preview: {observation.content[:200]}...")

        # Example 3: Get page information
        print("\n📊 Example 3: Page information...")
        print(f"Open pages: {observation.open_pages_urls}")
        print(f"Active page index: {observation.active_page_index}")
        print(f"Last action: {observation.last_browser_action}")

        if observation.error:
            print(f"❌ Error: {observation.last_browser_action_error}")

    finally:
        print("\n🧹 Closing browser...")
        browser.close()
        print("✅ Done!")


if __name__ == "__main__":
    asyncio.run(main())

