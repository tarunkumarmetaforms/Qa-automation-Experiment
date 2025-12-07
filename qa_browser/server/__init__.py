"""QA Browser Server - WebSocket server for real-time browser updates"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict, Set
import json
import asyncio
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class QABrowserServer:
    """Real-time WebSocket server for QA browser events"""

    def __init__(self):
        self.app = FastAPI(title="QA Browser Server")
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        self.setup_routes()

    def setup_routes(self):
        """Setup WebSocket and HTTP routes"""

        @self.app.websocket("/ws/{test_id}")
        async def websocket_endpoint(websocket: WebSocket, test_id: str):
            await self.connect(websocket, test_id)
            try:
                while True:
                    # Keep connection alive and receive messages
                    data = await websocket.receive_text()
                    logger.debug(f"Received message from {test_id}: {data}")
            except WebSocketDisconnect:
                await self.disconnect(websocket, test_id)

        @self.app.get("/health")
        async def health_check():
            return {"status": "healthy", "active_tests": len(self.active_connections)}

    async def connect(self, websocket: WebSocket, test_id: str):
        """Connect a new WebSocket client"""
        await websocket.accept()

        if test_id not in self.active_connections:
            self.active_connections[test_id] = set()

        self.active_connections[test_id].add(websocket)
        logger.info(f"Client connected to test {test_id}")

        # Send connection confirmation
        await self.send_event(test_id, {
            "type": "connection",
            "status": "connected",
            "test_id": test_id,
            "timestamp": datetime.now().isoformat()
        })

    async def disconnect(self, websocket: WebSocket, test_id: str):
        """Disconnect a WebSocket client"""
        if test_id in self.active_connections:
            self.active_connections[test_id].discard(websocket)

            if not self.active_connections[test_id]:
                del self.active_connections[test_id]

        logger.info(f"Client disconnected from test {test_id}")

    async def send_event(self, test_id: str, event: dict):
        """Send an event to all connected clients for a test"""
        if test_id not in self.active_connections:
            logger.warning(f"No clients connected for test {test_id}")
            return

        # Add timestamp if not present
        if "timestamp" not in event:
            event["timestamp"] = datetime.now().isoformat()

        message = json.dumps(event)

        # Send to all connected clients
        dead_connections = set()
        for connection in self.active_connections[test_id]:
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"Error sending to client: {e}")
                dead_connections.add(connection)

        # Clean up dead connections
        for conn in dead_connections:
            self.active_connections[test_id].discard(conn)

    async def broadcast_browser_observation(
        self,
        test_id: str,
        url: str,
        screenshot: str | None = None,
        action: str = '',
        error: bool = False,
        error_message: str = ''
    ):
        """Broadcast a browser observation to connected clients"""
        event = {
            "type": "browser_observation",
            "url": url,
            "screenshot": screenshot,
            "action": action,
            "error": error,
            "error_message": error_message,
        }
        await self.send_event(test_id, event)

    async def broadcast_test_status(
        self,
        test_id: str,
        status: str,
        message: str = ''
    ):
        """Broadcast test status update"""
        event = {
            "type": "test_status",
            "status": status,
            "message": message,
        }
        await self.send_event(test_id, event)


__all__ = ['QABrowserServer']

