# Auto Login to LPU WiFi

A simple Python script to automate login to LPU WiFi network.

## How to Use (Read the whole thing T-T)

1. Download the lastest Release of `lpu-wifi-autologin.exe` from [Releases](https://github.com/friedavocadoes/lpu-wifi-autologin/releases).

2. Run the `lpu-wifi-autologin.exe` file.

> [!CAUTION]
> Windows might display a warning when you try to run the exe file. This is because the file is not signed.
> You can safely ignore this warning.

3. Enter your LPU credentials when prompted.

> [!NOTE]
> You will only need to input credentials on the first login, after that everytime you run the exe, it will automatically log you in.

## For Contributors

<!-- prettier-ignore -->
> [!NOTE]
> `exer.py` is used to build the `.exe` file during packaging. Use `run.py` to raw run using python and check out logic.

### Commands to work with:

> [!TIP]
> I suggest you create a virtual environment to work with this project.

1. Install required packages: `pip install -r requirements.txt`
2. After build cleanup: `rm -rf build dist __pycache__ *.pyc`
3. Convert to exe: `pyinstaller --onefile exer.py`
4. Output available in: `dist/exer.exe`
