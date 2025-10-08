# Connect & Auto Login to closest LPU WiFi [Windows only]


<!-- BEGIN LATEST DOWNLOAD BUTTON -->
[![Download lpu-wifi-autologin.exe](https://custom-icon-badges.demolab.com/badge/-Download-orange?style=for-the-badge&logo=download&logoColor=white "Download lpu-wifi-autologin.exe")](https://github.com/friedavocadoes/lpu-wifi-autologin/releases/download/4/lpu-wifi-autologin.exe)
<!-- END LATEST DOWNLOAD BUTTON -->


A simple Python script to automate login to LPU WiFi networks like `LPU Hostels`, `LPUWIRELESS`, `LPU Block-34`, etc.

### I assure you there are no kinds of spyware or data stealers in this script, you may check the code yourself or use AI to verify safety.

## How to Use (Read the whole thing pls)

1. Download the lastest Release of `lpu-wifi-autologin.exe` from [Releases](https://github.com/friedavocadoes/lpu-wifi-autologin/releases).

2. Run the `lpu-wifi-autologin.exe` file. It will connect you to the closest LPU WiFi and log you in.

> [!CAUTION]
> Windows might display a warning when you try to run the exe file. This is because the file is not signed.
> You can safely ignore this warning.

3. Enter your LPU credentials when/if prompted.

> [!NOTE]
> You will only need to input credentials on the first login, after that everytime you run the exe, it will automatically log you in.

## For Contributors

`exer.py` is used to build the `.exe` file during packaging.

#### Commands to work with:

> [!TIP]
> I suggest you create a virtual environment to work with this project.

1. Install required packages: `pip install -r requirements.txt`
2. After build cleanup: `rm -rf build dist __pycache__ *.pyc`
3. Convert to exe: `pyinstaller --onefile exer.py`
4. Output available in: `dist/exer.exe`
