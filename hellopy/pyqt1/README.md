# About

Helloworld of PyQt6, created by QT Creator.

To build installer exe file:

    $ pyinstaller widget.py --onefile --windowed --paths "venv/Lib/site-packages" --hidden-import PySide6 --icon="favicon.ico" --add-data="favicon.ico;."

# Tips

* Activate virtualenv

in 

    cd .qtcreator/Python_#_#.#venv/bin

or

    cd venv

run

    soruce activate

* install module in virtualenv

In activate venv,

    pip install <module>

To check current virtualenv

    pip -V

# Issue

* [solved] ModuleNotFoundError: No module named 'PySide6'

This happens when loaded an existing project. To solve the error, install PySide6.

* Can't change app window icon.

[see also questions here](https://stackoverflow.com/questions/24363719/pyinstaller-cant-change-the-shortcut-icon) - none of these is working