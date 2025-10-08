import os
import sys
import threading
import time
import requests
from pathlib import Path

URL = "https://internet.lpu.in/24online/servlet/E24onlineHTTPClient"
CONFIG_FILE = Path.home() / ".lpu_login.txt"  # gets saved as C:\Users\<you>\.lpu_login.txt on Windows

def spinner(stop_event):
    while not stop_event.is_set():
        for c in "|/-\\":
            print(f"\rLogging in... {c}", end="", flush=True)
            time.sleep(0.1)
    print("\r", end="", flush=True)  

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
    username = input("Enter your Registration Number (eg. 1222332): ").strip()
    password = input("Enter your WiFi password: ").strip()
    username = username + "@lpu.com"
    print(username)
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

    stop_event = threading.Event()
    t = threading.Thread(target=spinner, args=(stop_event,))
    t.start()


    try:
        r = requests.post(URL, data=payload, headers=headers, timeout=15)
        stop_event.set()
        t.join()
        text = r.text.lower()
        if r.status_code == 200 and ("successfully logged in" in text):
            print("[+] Logged in successfully.")
        else:
            print("[-] Login might have failed (check credentials or network).")
            print("Response code:", r.status_code)
    except Exception as e:
        stop_event.set()
        t.join()
        print("[-] Error:", e)

def main():
    username, password = read_creds()
    if not username or not password:
        print("No saved credentials found.")
        username, password = ask_creds()
    attempt_login(username, password)

if __name__ == "__main__":
    main()
