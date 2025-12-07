"""
WebSocket Demo
Demonstrates real-time browser updates via WebSocket server
"""

import asyncio
import uvicorn
from qa_browser import BrowserEnv, BrowseURLAction, browse
from qa_browser.server import QABrowserServer


async def run_test_with_websocket(server: QABrowserServer, test_id: str):
    """Run a test and broadcast updates via WebSocket"""

    # Notify test started
    await server.broadcast_test_status(test_id, "starting", "Initializing browser...")

    browser = BrowserEnv()

    try:
        # Test 1: Visit homepage
        await server.broadcast_test_status(test_id, "running", "Visiting homepage...")

        action = BrowseURLAction(url="https://example.com")
        observation = await browse(action, browser)

        await server.broadcast_browser_observation(
            test_id=test_id,
            url=observation.url,
            screenshot=observation.screenshot,
            action="Navigate to homepage",
            error=observation.error,
            error_message=observation.last_browser_action_error
        )

        await asyncio.sleep(2)  # Pause for visibility

        # Test 2: Interact with page
        await server.broadcast_test_status(test_id, "running", "Clicking link...")

        # This is just an example - adjust based on actual page structure
        from qa_browser import BrowseInteractiveAction
        action = BrowseInteractiveAction(
            browser_actions='click("more-information")'
        )
        observation = await browse(action, browser, workspace_dir='.')

        await server.broadcast_browser_observation(
            test_id=test_id,
            url=observation.url,
            screenshot=observation.screenshot,
            action="Click more information link",
            error=observation.error,
            error_message=observation.last_browser_action_error
        )

        # Test completed
        await server.broadcast_test_status(test_id, "completed", "All tests passed!")

    except Exception as e:
        await server.broadcast_test_status(test_id, "failed", f"Test failed: {str(e)}")

    finally:
        browser.close()


async def start_server_and_test():
    """Start WebSocket server and run a test"""

    # Create server
    server = QABrowserServer()

    print("🚀 Starting WebSocket server on http://localhost:8000")
    print("📡 WebSocket endpoint: ws://localhost:8000/ws/{test_id}")
    print("💚 Health check: http://localhost:8000/health")
    print("\n🔌 Connect a WebSocket client to see real-time updates!")
    print("   Example: wscat -c ws://localhost:8000/ws/demo-test-123\n")

    # Start server in background
    config = uvicorn.Config(server.app, host="0.0.0.0", port=8000, log_level="info")
    server_instance = uvicorn.Server(config)

    # Run server in background task
    server_task = asyncio.create_task(server_instance.serve())

    # Wait a bit for server to start
    await asyncio.sleep(2)

    # Run a test (this will broadcast to any connected clients)
    print("🧪 Running demo test...\n")
    await run_test_with_websocket(server, "demo-test-123")

    print("\n✅ Demo test completed!")
    print("📊 Server is still running. Press Ctrl+C to stop.")

    # Keep server running
    try:
        await server_task
    except asyncio.CancelledError:
        print("\n🛑 Server stopped")


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════╗
║          QA Browser - WebSocket Demo                    ║
║                                                          ║
║  This demo starts a WebSocket server and runs a test    ║
║  that broadcasts real-time browser updates.              ║
║                                                          ║
║  Connect with: wscat -c ws://localhost:8000/ws/test-123 ║
║  Or use the provided React frontend component           ║
╚══════════════════════════════════════════════════════════╝
""")

    try:
        asyncio.run(start_server_and_test())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

