# Auto Login to LPU WiFi

A simple Python script to automate login to LPU WiFi network.

## How to Use

Download the lastest Release of `lpu-wifi-autologin.exe` from [Releases](https://github.com/friedavocadoes/lpu-wifi-autologin/releases)

> [!CAUTION]
> Windows might display a warning when you try to run the exe file. This is because the file is not signed. You can safely ignore this warning.

## For Contributors

1. Install required packages: `pip install -r requirements.txt`
2. After build cleanup: `rm -rf build dist __pycache__ *.pyc`
3. Convert to exe: `pyinstaller --onefile exer.py`
4. Output: `dist/exer.exe`
