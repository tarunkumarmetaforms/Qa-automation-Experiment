# QA Browser Module 

```
qa-browser-agent/
├── pyproject.toml              # Dependencies
├── requirements.txt            # Alternative dependency file
├── setup.py                    # Setup file
│
├── qa_browser/
│   ├── __init__.py
│   │
│   ├── core/                   # Core types and schemas
│   │   ├── __init__.py
│   │   ├── schema.py           # ActionType, ObservationType enums
│   │   ├── exceptions.py       # Custom exceptions
│   │   └── event.py            # Base Event class
│   │
│   ├── events/                 # Event definitions
│   │   ├── __init__.py
│   │   ├── action.py           # Action base class
│   │   ├── observation.py      # Observation base class
│   │   ├── browse_action.py    # Browser-specific actions
│   │   └── browse_observation.py  # Browser observations
│   │
│   ├── browser/                # Browser runtime
│   │   ├── __init__.py
│   │   ├── browser_env.py      # Core browser management
│   │   ├── utils.py            # Browser utilities
│   │   └── base64_utils.py     # Screenshot encoding/decoding
│   │
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   ├── async_utils.py      # Async helpers
│   │   ├── shutdown_listener.py
│   │   └── logger.py           # Logging setup
│   │
│   └── server/                 # WebSocket server (optional)
│       ├── __init__.py
│       ├── websocket_server.py # Real-time event streaming
│       └── session.py          # Session management
│
```
