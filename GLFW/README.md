
https://askubuntu.com/questions/355565/how-do-i-install-the-latest-version-of-cmake-from-the-command-line

sudo apt remove --purge --auto-remove cmake

[download cmake-\*-Linux-x86_64.tar.gz](https://cmake.org/download/)

run bin/cmake-gui or

~~~
	bin/cmake --version
~~~

According to [Compiling GLFW](https://www.glfw.org/docs/latest/compile.html),
install xorg-dev.

~~~
    sudo apt-get install xorg-dev
~~~

~~~
    bin/ccmake .
~~~

and turn on BUILD_SHARED_LIBS

~~~
	make # try again after ccmake . skipped first time
	sudo make install
~~~

Installing output:

~~~
	Install the project...
	-- Install configuration: ""
	-- Up-to-date: /usr/local/include/GLFW
	-- Up-to-date: /usr/local/include/GLFW/glfw3native.h
	-- Up-to-date: /usr/local/include/GLFW/glfw3.h
	-- Up-to-date: /usr/local/lib/cmake/glfw3/glfw3Config.cmake
	-- Up-to-date: /usr/local/lib/cmake/glfw3/glfw3ConfigVersion.cmake
	-- Old export file "/usr/local/lib/cmake/glfw3/glfw3Targets.cmake" will be replaced.  Removing files [/usr/local/lib/cmake/glfw3/glfw3Targets-noconfig.cmake].
	-- Installing: /usr/local/lib/cmake/glfw3/glfw3Targets.cmake
	-- Installing: /usr/local/lib/cmake/glfw3/glfw3Targets-noconfig.cmake
	-- Installing: /usr/local/lib/pkgconfig/glfw3.pc
	-- Installing: /usr/local/lib/libglfw.so.3.3
	-- Installing: /usr/local/lib/libglfw.so.3
	-- Installing: /usr/local/lib/libglfw.so
~~~

Go test and make test.

[Make sure makefile use tabs not 4 space](https://stackoverflow.com/questions/16931770/makefile4-missing-separator-stop)

To export lib path in Ubuntu:

~~~
    export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
~~~
