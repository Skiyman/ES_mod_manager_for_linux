
<img src="src/assets/logo.png" alt="drawing" width="63"/> ESModManager
=====================
![release](https://img.shields.io/github/v/release/Skiyman/ES_mod_manager_for_linux)
![GitHub repo size](https://img.shields.io/github/repo-size/Skiyman/ES_mod_manager_for_linux)
![GitHub all releases](https://img.shields.io/github/downloads/Skiyman/ES_mod_manager_for_linux/total)


Настольное приложение для упрощения запуска визуальной новеллы "Бесконечное лето". Написанное для ОС на базе GNU/Linux

[💿 **Скачать deb пакет**](https://github.com/Skiyman/ES_mod_manager_for_linux/releases/download/v0.1/esmodmanager_0.1-1_amd64.deb)

### Проверенные дистрибутивы:
- [x] Debian 12 «Bookworm»
- [ ] Ubuntu 22.04
- [ ] ArchLinux
- [ ] Fedora

Установка:
-------------
**Debian, Ubuntu 22.04-23.04**:

Необходимо скачать [.deb пакет](https://github.com/Skiyman/ES_mod_manager_for_linux/releases/download/v0.1/esmodmanager_0.1-1_amd64.deb), открыть папку с пакетом в терминале и выполнить команду:
```shell
sudo apt install ./esmodmanager_0.1-1_amd64.deb 
```

Сборка из исходного кода:
-------------

**Установка зависимостей**:
Python3, Pip3, Git, gcc, make, Python3 aiohttp, Python3 beautifulsoup4, Python3 lxml, Python 3 psutil,
Python3 request, Python3 PyQt5

**Для Debian/Ubuntu**:
```bash
sudo apt install make git gcc upx-ucl python3 python3-pip python3-wheel \
  python3-aiohttp python3-bs4 python3-lxml python3-psutil\
  python3-requests python3-pyqt5
```

### Запуск из исходного кода:

`python3-venv`, `build-essentials` и вышеперечисленные библиотеки необходимы.
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/launcher.py
```

### Установка:
Скачайте исходники и запустите `make`:
```bash
git clone https://github.com/Skiyman/ES_mod_manager_for_linux
cd ES_mod_manager_for_linux
make
sudo make install # Установка
```