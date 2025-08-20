import argparse
from cookiespy.exporter import export_to_json, export_to_csv
from rich.console import Console
import requests
from urllib.parse import urlparse

console = Console()

def fetch_cookies(url):
    try:
        response = requests.get(url)
        cookies = response.cookies.get_dict()
        return cookies
    except Exception as e:
        console.print(f"[red][!] Error mengambil cookies: {e}[/red]")
        return {}

def main():
    parser = argparse.ArgumentParser(description="CookieSpy - Inspect and export cookies")
    parser.add_argument("url", help="Target URL to fetch cookies from")
    parser.add_argument("--export", choices=["json", "csv"], help="Export format")
    args = parser.parse_args()

    console.print(f"[bold green]Fetching cookies from:[/bold green] {args.url}")
    response = requests.get(args.url)

    cookies = response.cookies.get_dict()
    console.print(f"[cyan]Cookies found:[/cyan] {cookies}")

    if args.export == "json":
        export_to_json(cookies, "cookies.json")
        console.print("[yellow]Exported cookies to cookies.json[/yellow]")
    elif args.export == "csv":
        export_to_csv(cookies, "cookies.csv")
        console.print("[yellow]Exported cookies to cookies.csv[/yellow]")

# Ensure main is called when run as a script
if __name__ == "__main__":
    main()
