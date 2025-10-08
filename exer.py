import os
import sys
import requests
from pathlib import Path

URL = "https://internet.lpu.in/24online/servlet/E24onlineHTTPClient"
CONFIG_FILE = Path.home() / ".lpu_login.txt"  # gets saved as C:\Users\<you>\.lpu_login.txt on Windows

def read_creds():
    if not CONFIG_FILE.exists():
        return None, None
    try:
        lines = CONFIG_FILE.read_text(encoding="utf-8").splitlines()
        if len(lines) < 2:
            return None, None
        username, password = lines[0].strip(), lines[1].strip()
        return username, password
    except Exception:
        return None, None

def write_creds(username, password):
    CONFIG_FILE.write_text(f"{username}\n{password}", encoding="utf-8")

def ask_creds():
    username = input("Enter LPU username: ").strip()
    password = input("Enter LPU password: ").strip()
    write_creds(username, password)
    print("Credentials saved to", CONFIG_FILE)
    return username, password

def attempt_login(username, password):
    payload = {
        "mode": "191",
        "isAccessDenied": "false",
        "url": "null",
        "username": username,
        "password": password,
    }

    headers = {
        "Origin": "https://internet.lpu.in",
        "Referer": "https://internet.lpu.in/24online/servlet/E24onlineHTTPClient",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    try:
        r = requests.post(URL, data=payload, headers=headers, timeout=15)
        text = r.text.lower()
        if r.status_code == 200 and ("logout" in text or "welcome" in text or "you are connected" in text):
            print("[+] Logged in successfully.")
        else:
            print("[-] Login might have failed (check credentials or network).")
            print("Response code:", r.status_code)
    except Exception as e:
        print("[-] Error:", e)

def main():
    username, password = read_creds()
    if not username or not password:
        print("No saved credentials found.")
        username, password = ask_creds()
    attempt_login(username, password)

if __name__ == "__main__":
    main()
