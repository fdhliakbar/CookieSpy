from .cli import main, fetch_cookies, validate_url

__all__ = ["main", "fetch_cookies", "validate_url"]
__version__ = "0.1.0"

def get_cookies(url: str):
    """Ambil cookies dari URL secara langsung."""
    return fetch_cookies(url)