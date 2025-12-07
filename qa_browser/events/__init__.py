"""Event system for QA Browser - Actions and Observations"""

from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, ClassVar


# ============================================
# Event Types
# ============================================

class ActionType(str, Enum):
    """Types of actions that can be performed"""
    BROWSE = 'browse'
    BROWSE_INTERACTIVE = 'browse_interactive'


class ObservationType(str, Enum):
    """Types of observations from the environment"""
    BROWSE = 'browse'
    BROWSE_INTERACTIVE = 'browse_interactive'


class EventSource(str, Enum):
    """Source of an event"""
    AGENT = 'agent'
    USER = 'user'
    ENVIRONMENT = 'environment'


class ActionSecurityRisk(int, Enum):
    """Security risk level of an action"""
    UNKNOWN = -1
    LOW = 0
    MEDIUM = 1
    HIGH = 2


# ============================================
# Base Event Classes
# ============================================

@dataclass
class Event:
    """Base class for all events"""
    INVALID_ID = -1

    _id: int = field(default=INVALID_ID, init=False)
    _timestamp: str = field(default_factory=lambda: datetime.now().isoformat(), init=False)
    _source: str = field(default=EventSource.ENVIRONMENT.value, init=False)

    @property
    def id(self) -> int:
        return self._id

    @property
    def timestamp(self) -> str:
        return self._timestamp

    @property
    def source(self) -> EventSource:
        return EventSource(self._source)

    @property
    def message(self) -> str:
        return ''


@dataclass
class Action(Event):
    """Base class for actions"""
    runnable: ClassVar[bool] = False
    action: str = ''
    security_risk: ActionSecurityRisk = ActionSecurityRisk.UNKNOWN


@dataclass
class Observation(Event):
    """Base class for observations"""
    content: str = ''
    observation: str = ''


# ============================================
# Browser Actions
# ============================================

@dataclass
class BrowseURLAction(Action):
    """Action to browse to a URL"""
    url: str = ''
    thought: str = ''
    action: str = ActionType.BROWSE.value
    runnable: ClassVar[bool] = True
    security_risk: ActionSecurityRisk = ActionSecurityRisk.UNKNOWN
    return_axtree: bool = False

    @property
    def message(self) -> str:
        return f'Browsing to URL: {self.url}'

    def __str__(self) -> str:
        ret = '**BrowseURLAction**\n'
        if self.thought:
            ret += f'THOUGHT: {self.thought}\n'
        ret += f'URL: {self.url}'
        return ret


@dataclass
class BrowseInteractiveAction(Action):
    """Action to interact with the browser"""
    browser_actions: str = ''
    thought: str = ''
    browsergym_send_msg_to_user: str = ''
    action: str = ActionType.BROWSE_INTERACTIVE.value
    runnable: ClassVar[bool] = True
    security_risk: ActionSecurityRisk = ActionSecurityRisk.UNKNOWN
    return_axtree: bool = False

    @property
    def message(self) -> str:
        return f'Interacting with browser:\n```\n{self.browser_actions}\n```'

    def __str__(self) -> str:
        ret = '**BrowseInteractiveAction**\n'
        if self.thought:
            ret += f'THOUGHT: {self.thought}\n'
        ret += f'BROWSER_ACTIONS: {self.browser_actions}'
        return ret


# ============================================
# Browser Observations
# ============================================

@dataclass
class BrowserOutputObservation(Observation):
    """Observation from browser output"""
    url: str = ''
    trigger_by_action: str = ''
    screenshot: str = field(repr=False, default='')
    screenshot_path: str | None = None
    set_of_marks: str = field(default='', repr=False)
    error: bool = False
    observation: str = ObservationType.BROWSE.value
    goal_image_urls: list[str] = field(default_factory=list)
    open_pages_urls: list[str] = field(default_factory=list)
    active_page_index: int = -1
    dom_object: dict[str, Any] = field(default_factory=dict, repr=False)
    axtree_object: dict[str, Any] = field(default_factory=dict, repr=False)
    extra_element_properties: dict[str, Any] = field(default_factory=dict, repr=False)
    last_browser_action: str = ''
    last_browser_action_error: str = ''
    focused_element_bid: str = ''
    filter_visible_only: bool = False

    @property
    def message(self) -> str:
        return f'Visited {self.url}'

    def __str__(self) -> str:
        ret = (
            '**BrowserOutputObservation**\n'
            f'URL: {self.url}\n'
            f'Error: {self.error}\n'
            f'Open pages: {self.open_pages_urls}\n'
            f'Active page index: {self.active_page_index}\n'
            f'Last browser action: {self.last_browser_action}\n'
            f'Last browser action error: {self.last_browser_action_error}\n'
            f'Focused element bid: {self.focused_element_bid}\n'
        )
        if self.screenshot_path:
            ret += f'Screenshot saved to: {self.screenshot_path}\n'
        ret += '--- Agent Observation ---\n'
        ret += self.content
        return ret


__all__ = [
    'ActionType',
    'ObservationType',
    'EventSource',
    'ActionSecurityRisk',
    'Event',
    'Action',
    'Observation',
    'BrowseURLAction',
    'BrowseInteractiveAction',
    'BrowserOutputObservation',
]

