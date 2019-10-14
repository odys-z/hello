# Execute ex1.4.py from Ubuntu

~~~
    sudo apt-get install python3-numpy
    sudo apt-get install python3-matplotlib
    pip3 install ipython

~~~

For error like

~~~
    Traceback (most recent call last):
      File "/usr/bin/pip3", line 9, in <module>
        from pip import main
    ImportError: cannot import name 'main'
~~~

Try update pip3

~~~
    sudo python3 -m pip uninstall pip && sudo apt install python3-pip --reinstall
~~~

If python complain about

~~~
    You are using pip version 8.1.1, however version 19.2.3 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.
~~~

Upgrade pip3

~~~
    pip3 install --upgrade pip
~~~

And if you are not lucky, the PLA looks like will trying endlessly without error
converged.

![001 ex1.4](imgs/001%20ex1.4.png)

![002 ex1.4](imgs/002%20ex1.4.png)
