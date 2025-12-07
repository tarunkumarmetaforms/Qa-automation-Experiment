"""
Screenshot Example
Demonstrates how to capture and save screenshots to files
"""

import asyncio
import os
from qa_browser import BrowserEnv, BrowseURLAction, browse


async def main():
    print("🌐 Initializing browser...")
    browser = BrowserEnv()

    # Get the current directory as workspace
    workspace_dir = os.getcwd()
    print(f"📁 Workspace directory: {workspace_dir}")
    print(f"📸 Screenshots will be saved to: {workspace_dir}/.browser_screenshots/")

    try:
        # Example 1: Navigate to Google.com and SAVE screenshot to file
        print("\n📍 Example 1: Taking screenshot of Google.com...")
        action = BrowseURLAction(url="https://www.metaforms.ai/")
        
        # Pass workspace_dir to save screenshot to file
        observation = await browse(action, browser, workspace_dir=workspace_dir)

        print(f"✅ Visited: {observation.url}")
        
        if observation.screenshot_path:
            print(f"💾 Screenshot SAVED to file: {observation.screenshot_path}")
        else:
            print(f"⚠️  Screenshot NOT saved (only in memory)")
        
        print(f"📊 Screenshot data size: {len(observation.screenshot)} characters (base64)")
        print(f"📄 Content preview: {observation.content[:150]}...")

        # Example 2: Navigate to Example.com and save screenshot
        print("\n📍 Example 2: Taking screenshot of Example.com...")
        action = BrowseURLAction(url="https://example.com")
        observation = await browse(action, browser, workspace_dir=workspace_dir)

        print(f"✅ Visited: {observation.url}")
        if observation.screenshot_path:
            print(f"💾 Screenshot SAVED to file: {observation.screenshot_path}")
        
        # Example 3: Navigate WITHOUT saving (no workspace_dir)
        print("\n📍 Example 3: Screenshot in memory only (not saved)...")
        action = BrowseURLAction(url="https://github.com")
        observation = await browse(action, browser)  # No workspace_dir parameter

        print(f"✅ Visited: {observation.url}")
        if observation.screenshot_path:
            print(f"💾 Screenshot saved to: {observation.screenshot_path}")
        else:
            print(f"ℹ️  Screenshot kept in memory only (not saved to file)")
            print(f"📊 Screenshot data available: {len(observation.screenshot)} characters")

        print("\n" + "="*60)
        print("✅ Summary:")
        print(f"   - Screenshots are saved to: {workspace_dir}/.browser_screenshots/")
        print(f"   - Check that folder to see your PNG files!")
        print("="*60)

    finally:
        print("\n🧹 Closing browser...")
        browser.close()
        print("✅ Done!")


if __name__ == "__main__":
    asyncio.run(main())
