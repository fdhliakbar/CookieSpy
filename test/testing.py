import pytest
from cookiespy.cli import fetch_cookies


def test_fetch_cookies_google():
    cookies = fetch_cookies("https://google.com/")
    assert isinstance(cookies, dict)
    assert len(cookies) > 0
