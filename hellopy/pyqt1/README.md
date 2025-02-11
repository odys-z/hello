# About

Helloworld of PyQt6, created by QT Creator.

To build installer exe file:

    $ pyinstaller widget.py --onefile --windowed --paths "venv/Lib/site-packages" --hidden-import PySide6 --icon="favicon.ico" --add-data="favicon.ico;."


# Issue

Can't change app window icon.

[see also](https://stackoverflow.com/questions/24363719/pyinstaller-cant-change-the-shortcut-icon)
- none of these is working