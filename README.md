# 🍪 CookieSpy

CookieSpy is a simple tool for retrieving, displaying, and exporting cookies from a URL.  
Supports colorized CLI display (via `rich`), export to JSON/CSV, and a simple web-based GUI (Flask).

---

## FLowchart

<div align="center">
<img src="./cookiespy-diagram.drawio.png" alt="diagram business for cookiespy" />
</div>

## Installation

With PyPI

```bash
pip install cookiespy
```

Or clone this repository(`recommended`)

```bash
https://github.com/fdhliakbar/CookieSpy.git
```

---

### Run with Docker 🐋

```bash
 docker build -t cookiespy:latest .
```

## CLI Usage

````bash
🔍 Mengambil cookies...

✔ Cookies ditemukan: {'_gh_sess':
'3TLOJqcMKU9Mi5JN8EkecauN9FsSaImjhCOiKu8YDXpalofmkZbBe1xYtVDBFYf6bmbNh6MTfg8IVY2wsq%2FVN46DF2ok51y2O%2FHGYnq1X8qXX3zLmRFtZzierEp1O%2BuPy9StY3jL11vTVDNmjvX2%2Bdfy99JZ0fZOc
Dle6ZmLE0%2F8kvP6oMMB%2FGhOb0jGTwRPpEuAfmy%2BFmoGfg%2FqUZTpNk6JvPifKDVLAFwVPH08JyFwuf2YxM1tRs1S2Rx7H%2B%2Blo8mLWUKKDpVeGaONLYeNbQ%3D%3D--2bPnIxmDdV4DSGDx--L5Zjb9nicw2HqWy
0LoVW%2BQ%3D%3D', '_octo': 'GH1.1.89567047.1755552745', 'logged_in': 'no'}
``` -->

### Install Packages

```bash
pip install dist/cookiespy-0.1.0-py3-none-any.whl

Installing collected packages: cookiespy
Successfully installed cookiespy-0.1.0
````

### Run Program with CLI(Command Line Interface)

```bash
# Export with JSON
cookiespy https://youtube.com/ --export json

# Export with CSV
cookiespy https://youtube.com/ --export csv

```

### Output JSON from Terminal

```bash
Fetching cookies from: https://facebook.com/
Cookies found: {'fr': '0qhvcEPszmVSmExBF..Boqw-r..AAA.0.0.Boqw-r.AWe5t84W9KkqFc6QoQPZqX7icCs', 'sb': 'qw-raOaLC5CvSSBM3qNhw0wf'}
[+] Cookies diexport ke cookies.json
Exported cookies to cookies.json
```

### Output CSV from Terminal

```bash
Fetching cookies from: https://facebook.com/
Cookies found: {'fr': '0o5AyAWMjYLU5Wf8G..Boqw_G..AAA.0.0.Boqw_G.AWejVulJjL0qf-r097kKCKBqM4k', 'sb': 'xg-raIpCTxgOpbwcUJfHj7bj'}
[+] Cookies diexport ke cookies.csv
Exported cookies to cookies.csv
```

### Example for User

```python
import cookiespy

url = "https://youtube.com"
cookies = cookiespy.get_cookies(url)
print(cookies)
```

```bash
python your_file.py
{'GPS': '1', 'YSC': 'ZURMJelC7BE', '__Secure-ROLLOUT_TOKEN': 'CLCs2Yu9lrzMIhD2lbW716OPAxj2lbW716OPAw%3D%3D', 'VISITOR_INFO1_LIVE': 'OF9aXStzneU', 'VISITOR_PRIVACY_METADATA': 'CgJJRBIEGgAgJQ%3D%3D'}
```

---

## Next feature development

1. `Support for Various Browsers`: Currently, CookieSpy uses requests, which do not run JavaScript. Many cookies, especially for analytics and tracking, are set via JavaScript.
2. `Session Management (Login)`: Distinguishing between session cookies and persistent cookies, as well as first-party and third-party cookies, and increasing export formats
3. `Increased Output`
4. `Interactive mode and GUI`

<p>If you have any questions or would like to contribute, you can make a pull request from my repository or contact me via email at <a href=
"mailto:fadhliakbar125@gmail.com?subject=Inquiry&body=Hi, I'm interested in your project on Cookiespy...">fadhliakbar125</a>.</p>
