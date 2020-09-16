## About

This sub project is used for GLFW & OpenGl practicing.

## Quick Start (Ubuntu)

### 1. Install CMake

Reference [Install CMake on Ubuntu](https://askubuntu.com/questions/355565/how-do-i-install-the-latest-version-of-cmake-from-the-command-line)

Purge first:

~~~
    sudo apt remove --purge --auto-remove cmake
~~~

[download cmake-\*-Linux-x86_64.tar.gz](https://cmake.org/download/)

run bin/cmake-gui or use CLI:

~~~
	bin/cmake --version
~~~

### 2. install GLFW from source

According to [CMake doc: Compiling GLFW](https://www.glfw.org/docs/latest/compile.html),
install xorg-dev:

~~~
    sudo apt-get install xorg-dev
~~~

Then configure CMake:

~~~
    bin/ccmake .
~~~

and turn on BUILD_SHARED_LIBS.

And install GLFW:

~~~
	make # try again after ccmake . skipped first time
	sudo make install
~~~

Installation output:

~~~
	Install the project...
	-- Install configuration: ""
	-- Up-to-date: /usr/local/include/GLFW
	-- Up-to-date: /usr/local/include/GLFW/glfw3native.h
	-- Up-to-date: /usr/local/include/GLFW/glfw3.h
	-- Up-to-date: /usr/local/lib/cmake/glfw3/glfw3Config.cmake
	-- Up-to-date: /usr/local/lib/cmake/glfw3/glfw3ConfigVersion.cmake
	-- Old export file "/usr/local/lib/cmake/glfw3/glfw3Targets.cmake" will be replaced.
	Removing files [/usr/local/lib/cmake/glfw3/glfw3Targets-noconfig.cmake].
	-- Installing: /usr/local/lib/cmake/glfw3/glfw3Targets.cmake
	-- Installing: /usr/local/lib/cmake/glfw3/glfw3Targets-noconfig.cmake
	-- Installing: /usr/local/lib/pkgconfig/glfw3.pc
	-- Installing: /usr/local/lib/libglfw.so.3.3
	-- Installing: /usr/local/lib/libglfw.so.3
	-- Installing: /usr/local/lib/libglfw.so
~~~

Go test folder and make test:

~~~
    cd test
    make test
~~~

[Make sure Makefile use tabs not 4 space](https://stackoverflow.com/questions/16931770/makefile4-missing-separator-stop).

If everything ok, the window will show a ratating trangle.
