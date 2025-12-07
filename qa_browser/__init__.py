"""
QA Browser - Standalone Browser Automation Module
"""

__version__ = '0.1.0'

from qa_browser.browser import (
    BrowserEnv,
    browse,
    get_agent_obs_text,
    get_axtree_str,
    image_to_png_base64_url,
    png_base64_url_to_image,
)

from qa_browser.events import (
    ActionType,
    ObservationType,
    EventSource,
    ActionSecurityRisk,
    BrowseURLAction,
    BrowseInteractiveAction,
    BrowserOutputObservation,
)

from qa_browser.exceptions import (
    BrowserError,
    BrowserInitException,
    BrowserUnavailableException,
    BrowserTimeoutException,
)

from qa_browser.server import QABrowserServer

__all__ = [
    # Browser
    'BrowserEnv',
    'browse',
    'get_agent_obs_text',
    'get_axtree_str',
    'image_to_png_base64_url',
    'png_base64_url_to_image',
    # Events
    'ActionType',
    'ObservationType',
    'EventSource',
    'ActionSecurityRisk',
    'BrowseURLAction',
    'BrowseInteractiveAction',
    'BrowserOutputObservation',
    # Exceptions
    'BrowserError',
    'BrowserInitException',
    'BrowserUnavailableException',
    'BrowserTimeoutException',
    # Server
    'QABrowserServer',
]

