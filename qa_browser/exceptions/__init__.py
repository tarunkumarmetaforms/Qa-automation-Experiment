# QA Browser Exceptions

class BrowserError(Exception):
    """Base class for all browser exceptions."""
    pass


class BrowserInitException(BrowserError):
    """Raised when browser fails to initialize."""
    def __init__(self, message: str = 'Failed to initialize browser') -> None:
        super().__init__(message)


class BrowserUnavailableException(BrowserError):
    """Raised when browser is not available."""
    def __init__(self, message: str = 'Browser is not available') -> None:
        super().__init__(message)


class BrowserTimeoutException(BrowserError):
    """Raised when browser operation times out."""
    def __init__(self, message: str = 'Browser operation timed out') -> None:
        super().__init__(message)

