from dotenv import load_dotenv
import os
import requests

load_dotenv()

URL = "https://internet.lpu.in/24online/servlet/E24onlineHTTPClient"

USERNAME = os.getenv("LPU_USER")
PASSWORD = os.getenv("LPU_PASS")

payload = {
    "mode":"191", "isAccessDenied":"false", "url":"null", 

    "username": USERNAME,
    "password": PASSWORD,
}

headers = {
    "Origin": "https://internet.lpu.in",
    "Referer": "https://internet.lpu.in/24online/servlet/E24onlineHTTPClient",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/x-www-form-urlencoded",
}

s = requests.Session()

r = s.post(URL, data=payload, headers=headers, timeout=15, allow_redirects=True)

# crude success check
if r.status_code == 200 and "logout" in r.text.lower() or "welcome" in r.text.lower():
    print("Likely logged in")
else:
    # print short diagnostics
    print("Response code:", r.status_code)
    print("Response length:", len(r.text))
    # Optionally save the page to debug
    open("debug_login_response.html", "w", encoding="utf-8").write(r.text)
    print("Saved debug_login_response.html for inspection.")
