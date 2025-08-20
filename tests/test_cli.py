# tests/test_cli.py
import subprocess
import sys
import pytest
from cookiespy.cli import fetch_cookies, validate_url

def test_validate_url_valid():
    url = "https://youtube.com"
    assert validate_url(url) == url


def test_validate_url_invalid():
    with pytest.raises(ValueError):
        validate_url("invalid-url")


def test_fetch_cookies_real_site():
    """Tes ke situs nyata (YouTube). Bisa skip di CI untuk stabilitas."""
    cookies = fetch_cookies("https://www.youtube.com")
    assert isinstance(cookies, dict)


def test_cli_help():
    """Tes opsi --help"""
    result = subprocess.run(
        [sys.executable, "-m", "cookiespy.cli", "--help"],
        capture_output=True,
        text=True,
    )
    assert "CookieSpy" in result.stdout


def test_cli_with_export_json(tmp_path):
    """Tes export JSON"""
    output_file = tmp_path / "yt_cookies.json"
    result = subprocess.run(
        [sys.executable, "-m", "cookiespy.cli", "https://www.youtube.com", "--export", "json", "--output", str(output_file)],
        capture_output=True,
        text=True,
    )
    assert output_file.exists()
    assert "Exported cookies" in result.stdout


def test_cli_with_export_csv(tmp_path):
    """Tes export CSV"""
    output_file = tmp_path / "yt_cookies.csv"
    result = subprocess.run(
        [sys.executable, "-m", "cookiespy.cli", "https://www.youtube.com", "--export", "csv", "--output", str(output_file)],
        capture_output=True,
        text=True,
    )
    assert output_file.exists()
    assert "Exported cookies" in result.stdout
