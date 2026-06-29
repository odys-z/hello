# About

Hello Slint.

# Setup

## Prerequisites

- Install Rust and Cargo

1. Download rust-init at [Rust](https://rustup.rs/)

1. (Optinal) setup Rust mirror

```
    export RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static
    export RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup
```

1. Install Rust

```
    ./rustup-init.exe
```

Close and restart VS Code.

1. Check Cargo

```
    $ rustc --version
    rustc 1.96.0 (ac68faa20 2026-05-25)

    $ cargo --version
    cargo 1.96.0 (30a34c682 2026-05-25)
```

## Setup CMake Project In Windows, using VS Code Bash Terminal


configure Cargo mirro

```
    code ~/.cargo/config.toml
```

File content:

```
    [source.crates-io]
    replace-with = 'ustc'

    [source.ustc]
    registry = "sparse+https://mirrors.ustc.edu.cn/crates.io-index/"
```

The project uses MinGW GCC 16.0.1

```
    $ export PATH="/c/Qt-6.10/Tools/CMake_64/bin:$PATH"
    $ export PATH="/c/Qt-6.10/mingw64-gcc16.1.0/bin:$PATH"
    $ rustup target add --toolchain stable-x86_64-pc-windows-msvc x86_64-pc-windows-gnu
    $ cmake -G "MinGW Makefiles" -B build
```


Debug with MinGW GCC 16.0.1 & GDB in VS Code.

Add a customer downloaded MingGW & GCC to system environment, start VS Code and in CMake, scan the kit and select it.

[debug](./debug.png)