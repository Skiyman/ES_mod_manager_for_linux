
<img src="src/assets/logo.png" alt="drawing" width="63"/> ESModManager
=====================
![release](https://img.shields.io/github/v/release/Skiyman/ES_mod_manager_for_linux)
![GitHub repo size](https://img.shields.io/github/repo-size/Skiyman/ES_mod_manager_for_linux)
![GitHub all releases](https://img.shields.io/github/downloads/Skiyman/ES_mod_manager_for_linux/total)


Desktop application for easier launch visual novel "Everlasting summer". Built for OS based on GNU/Linux

[💿 **Download deb package**](https://github.com/Skiyman/ES_mod_manager_for_linux/releases/download/v0.1.1/esmodmanager_0.1.1-2_amd64.deb)

### Verified distributive:
- [x] Debian 12 «Bookworm»
- [x] ArchLinux
- [ ] Ubuntu 22.04
- [ ] Fedora

Installation:
-------------
**Debian, Ubuntu 22.04-23.04**:

Need to download [.deb package](https://github.com/Skiyman/ES_mod_manager_for_linux/releases/download/v0.1.1/esmodmanager_0.1.1-2_amd64.deb), open the folder where the package is located in the terminal and run the command:
```shell
sudo apt install ./esmodmanager_0.1-1_amd64.deb 
```

Build from source code:
-------------

**Install dependencies**:
Python3, Pip3, Git, gcc, make, Python3 aiohttp, Python3 beautifulsoup4, Python3 lxml, Python 3 psutil,
Python3 request, Python3 PyQt5

**For Debian/Ubuntu**:
```bash
sudo apt install make git gcc python3 python3-pip python3-wheel \
  python3-aiohttp python3-bs4 python3-lxml python3-psutil\
  python3-requests python3-pyqt5
```

**For Arch**:
```bash
sudo pacman -S make git gcc python python-pip python-wheel \
python-aiohttp python-beautifulsoup4 python-lxml python-psutil \
python-requests python-pyqt5 
```

### Run from source code:

`python3-venv`, `build-essentials` and the above libraries are required.
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/launcher.py
```

### Install:
Download source and run `make`:
```bash
git clone https://github.com/Skiyman/ES_mod_manager_for_linux
cd ES_mod_manager_for_linux
make
sudo make install # Install
```
