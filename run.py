from dotenv import load_dotenv
import os
import requests

load_dotenv()

URL = "https://internet.lpu.in/24online/servlet/E24onlineHTTPClient"

# safer: set these in env vars instead of editing this file
USERNAME = os.getenv("LPU_USER")
PASSWORD = os.getenv("LPU_PASS")

payload = {
    "mode":"191","isAccessDenied":"false","url":"null","message":"","regusingpinid":"",
    "checkClose":"1","sessionTimeout":"-1","guestmsgreq":"false","logintype":"2",
    "orgSessionTimeout":"-1","chrome":"-1","alerttime":"null","timeout":"-1","popupalert":"0",
    "dtold":"0","mac":"f8%3Ac1%3A16%3A45%3Ab6%3A80","servername":"172.20.0.66","temptype":"",
    "selfregpageid":"","leave":"no","macaddress":"f8%3Ac1%3A16%3A45%3Ab6%3A80","ipaddress":"10.34.129.133",
    "username": USERNAME, "password": PASSWORD, "saveinfo":"saveinfo",
    "loginotp":"false","logincaptcha":"false","registeruserotp":"false","registercaptcha":"false"
}

headers = {
    "Origin": "https://internet.lpu.in",
    "Referer": "https://internet.lpu.in/24online/servlet/E24onlineHTTPClient",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/x-www-form-urlencoded",
}

s = requests.Session()
# optional: initialize cookies by hitting the page first
s.get("https://internet.lpu.in/24online/servlet/E24onlineHTTPClient", headers=headers, timeout=10)

r = s.post(URL, data=payload, headers=headers, timeout=15, allow_redirects=True)

# crude success check — tweak to something that indicates a logged-in page for you
if r.status_code == 200 and "logout" in r.text.lower() or "welcome" in r.text.lower():
    print("Likely logged in ✅")
else:
    # print short diagnostics
    print("Response code:", r.status_code)
    print("Response length:", len(r.text))
    # Optionally save the page to debug
    open("debug_login_response.html", "w", encoding="utf-8").write(r.text)
    print("Saved debug_login_response.html for inspection.")
