import requests
import sys

def check_cookies(url):
    try:
        session = requests.Session()
        response = session.get(url, allow_redirects=True)

        cookies = session.cookies

        if not cookies:
            print(f"[!] Tidak ada cookie ditemukan dari {url}")
            return

        print(f"\n🍪 Cookie Analysis for: {url}\n")
        print("{:<20} {:<10} {:<10} {:<15}".format("Cookie", "Secure", "HttpOnly", "SameSite"))
        print("-" * 60)

        for cookie in cookies:
            cookie_attrs = cookie.__dict__

            secure = "Yes" if cookie.secure else "No"
            httponly = "Yes" if "HttpOnly" in cookie_attrs.get("_rest", {}) else "No"
            samesite = cookie_attrs.get("samesite", "None")

            print("{:<20} {:<10} {:<10} {:<15}".format(cookie.name, secure, httponly, samesite))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cookiespy.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    check_cookies(url)
