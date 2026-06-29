# Custom MinGW + GCC 16.1.0 Quick Start


```
    export PATH="/c/Qt-6.10/Tools/CMake_64/bin:$PATH"
    export PATH="/c/Qt-6.10/mingw64-gcc16.1.0/bin:$PATH"
    rustup target add --toolchain stable-x86_64-pc-windows-msvc x86_64-pc-windows-gnu
    cmake -G "MinGW Makefiles" -B build -DFETCHCONTENT_BASE_DIR="C:/CMakeCache" -DFETCHCONTENT_FULLY_DISCONNECTED=ON
    cmake --build build
    build/my_application.exe
`
```