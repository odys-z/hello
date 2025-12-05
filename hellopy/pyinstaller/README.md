```
    pip install pyintaller
    cp -r $HOME/github/semantics-jserv/synode.py synode.py3
    cd synode.py3
    pyinstaller --onefile src/synodepy3/__main__.py3
    # modefiy .spec, name = 'synode-gui'
    pyinstaller __main.spec
    dist/synode-gui.exe
```