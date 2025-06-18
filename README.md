![App Screenshot](screenshots/shot1.png)

# Hello World PyQt6 Debian Package

This project is a simple "Hello World" desktop application built with Python and PyQt6, packaged as a `.deb` file for easy installation on Debian-based systems.

## Installing the Application

### Option 1: Graphical Installation (Recommended)
1. **Install gdebi** (if not already installed):
   ```bash
   sudo apt install gdebi
   ```

2. **Right-click** the downloaded `hello-world-pyqt_1.0.0-1_all.deb` file and select "Open with GDebi Package Installer"
   - Or double-click the .deb file if your system is configured to use gdebi by default
   - Click "Install Package" in the gdebi window
   - Enter your password when prompted

### Option 2: Command Line Installation
1. **Download the .deb file** (`hello-world-pyqt_1.0.0-1_all.deb`)

2. **Install PyQt6** (required for Ubuntu 22.04):
   ```bash
   sudo apt update
   sudo apt install -y python3-pip
   sudo pip3 install PyQt6
   ```

3. **Install the package:**
   ```bash
   sudo apt install ./hello-world-pyqt_1.0.0-1_all.deb
   ```
   This will automatically install all required dependencies.

## Running the Application
After installation, you can run the app:
- From your application menu (look for "Hello World PyQt")
- Or from the terminal:
  ```bash
  hello-world-pyqt
  ```

## Troubleshooting

### Ubuntu 22.04 Users
If you see an error about `python3-pyqt6` not being installable:
1. Install PyQt6 using pip as shown in the installation steps above
2. Then try installing the .deb package again

## Modifying the Application

- The main application code is in `hello_world.py`.
- To change the window title, message, or appearance, edit this file as needed.
- After making changes, rebuild the package to apply them.

## Building the .deb Package

1. **Install build dependencies:**
   ```bash
   sudo apt-get update
   sudo apt-get install -y devscripts debhelper python3-all python3-setuptools dh-python python3-pyqt6 qt6-gtk-platformtheme qt6-qpa-plugins
   ```

2. **Build the package:**
   ```bash
   dpkg-buildpackage -us -uc
   ```
   This will create a file like `../hello-world-pyqt_1.0.0-1_all.deb`.

## Installing on Another Debian Machine

1. **Copy the .deb file** to the other machine (e.g., using USB, scp, or email):
   ```bash
   scp ../hello-world-pyqt_1.0.0-1_all.deb user@other-machine:/path/to/
   ```

2. **On the other machine, install the package:**
   ```bash
   sudo apt update
   sudo apt install ./hello-world-pyqt_1.0.0-1_all.deb
   ```
   This will automatically install all required dependencies.

3. **Run the app:**
   - From the application menu, or
   - In the terminal:
     ```bash
     hello-world-pyqt
     ```

---

If you make changes to the app, repeat the build and install steps to update the package on your system(s). 