# Build & Install RTTR

Download from the [download page](https://www.rttr.org/doc/master/building_install_page.html).

Open the *x64 Native Tools Command Prompt for VS", 

```
    cmake --build . --config Release
    dir lib\Release
    rttr-0.9.6\lib\Release 的目录
    01/19/2026  11:46 PM    <DIR>          .
    01/19/2026  11:46 PM    <DIR>          ..
    01/19/2026  11:46 PM           312,952 rttr_core.exp
    01/19/2026  11:46 PM           519,660 rttr_core.lib

    cmake --install .
```

Set this project's environment as

```
    RTTR_DIR = .../rttr/install/cmake
```

the path where the rttr-config.cmake exists.

# References

1. [rttorg/RTTR @ Github](https://github.com/rttrorg/rttr)

```
    struct MyStruct { MyStruct() {}; void func(double) {}; int data; };

    RTTR_REGISTRATION
    {
        registration::class_<MyStruct>("MyStruct")
            .constructor<>()
            .property("data", &MyStruct::data)
            .method("func", &MyStruct::func);
    }
```

1. [RTTR Building & Installation](https://www.rttr.org/doc/master/building_install_page.html) RTTR Home page

```
    # Failed
    find_package(RTTR CONFIG REQUIRED Core)

    # looks downloading...
    FetchContent_Declare(
        rttr
        GIT_REPOSITORY  https://github.com/rttrorg/rttr.git
        GIT_TAG v0.9.6
    )

    FetchContent_MakeAvailable(rttr)

```

1. [nlohmann/json](https://github.com/nlohmann/json)

1. [JSON for Modern C++ version 3.12.0, nlohmann/json Issue #190](https://github.com/rttrorg/rttr/issues/190)

1. [JSON for Moden C++, SAX Interface](https://json.nlohmann.me/features/parsing/sax_interface/), nlohmann/json documents

1. [getml/reflect-cpp](https://github.com/getml/reflect-cpp/tree/main)

1. [ShumWengSang Reflection-Json-Serializer](https://github.com/ShumWengSang/Reflection-Json-Serializer)
   
   Only the serialization.

1. [JSONify All Things, Extending the nlohmann/json Library](https://www.kdab.com/jsonify-with-nlohmann-json/#:~:text=7%20comments,extending%20the%20library%20a%20bit.),
Nicolas Arnaud-Cormos, 14 April 2022

1. []