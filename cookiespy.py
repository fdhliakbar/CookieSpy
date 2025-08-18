import requests
from urllib.parse import urlparse
from exporter import export_to_json, export_to_csv
from rich.console import Console

console = Console()

def fetch_cookies(url):
    try:
        response = requests.get(url)
        cookies = response.cookies.get_dict()
        return cookies
    except Exception as e:
        console.print(f"[red][!] Error mengambil cookies: {e}[/red]")
        return {}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="CookieSpy CLI")
    parser.add_argument("url", help="URL target")
    parser.add_argument("--export", choices=["json", "csv"], help="Export format")
    args = parser.parse_args()

    console.print("[cyan]🔍 Mengambil cookies...[/cyan]")
    cookies = fetch_cookies(args.url)

    if cookies:
        console.print(f"[green]✔ Cookies ditemukan:[/green] {cookies}")

        if args.export == "json":
            export_to_json(cookies)
        elif args.export == "csv":
            export_to_csv(cookies)
    else:
        console.print("[yellow][!] Tidak ada cookie ditemukan[/yellow]")
