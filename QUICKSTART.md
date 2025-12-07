# QA Browser - Quick Start Guide 🚀

Get up and running in 5 minutes!

## Prerequisites

- Python 3.12+
- pip or poetry

## Installation

```bash
# 1. Navigate to the module directory
cd qa_browser_module

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
playwright install chromium
```

## Hello World - Your First Test

Create `my_first_test.py`:

```python
import asyncio
from qa_browser import BrowserEnv, BrowseURLAction, browse

async def main():
    # Initialize browser
    browser = BrowserEnv()

    try:
        # Visit a website
        action = BrowseURLAction(url="https://example.com")
        observation = await browse(action, browser)

        # Check results
        print(f"✅ Visited: {observation.url}")
        print(f"📸 Screenshot: {observation.screenshot_path}")

        if not observation.error:
            print("🎉 Success!")
        else:
            print(f"❌ Error: {observation.last_browser_action_error}")

    finally:
        browser.close()

if __name__ == "__main__":
    asyncio.run(main())
```

Run it:
```bash
python my_first_test.py
```

## Next Steps

### 1. Interactive Actions

```python
from qa_browser import BrowseInteractiveAction

# Click, fill forms, scroll, etc.
action = BrowseInteractiveAction(
    browser_actions='''
goto("https://google.com")
fill("q", "")
press("q", "Enter")
'''
)
observation = await browse(action, browser)
```

### 2. Real-time Updates

Start the WebSocket server:

```bash
python -m examples.websocket_demo
```

Then connect from your frontend or use `wscat`:
```bash
npm install -g wscat
wscat -c ws://localhost:8000/ws/my-test-123
```

### 3. Build Your QA Agent

See `examples/qa_agent.py` for a complete AI-powered QA agent example!

## Common Issues & Solutions

### Issue: "Browser failed to start"
```bash
# Re-install Playwright browsers
playwright install chromium --force
```

### Issue: "Module 'qa_browser' not found"
```bash
# Install in development mode
pip install -e .
```

### Issue: "Permission denied" on screenshots
```bash
# Create screenshots directory
mkdir -p .browser_screenshots
chmod 755 .browser_screenshots
```

## Resources



## What's Next?

1. ✅ Run basic browser test
2. ⬜ Add WebSocket real-time updates
3. ⬜ Build React frontend
4. ⬜ Create AI QA agent
5. ⬜ Deploy to production

**Happy Testing!** 🎉

