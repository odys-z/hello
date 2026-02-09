cmake_minimum_required(VERSION 3.30)

# in my/github/vcpkg
# ./vcpkg install entt:x64-windows --x-install-root="../anclient/examples/example.qml/vcpkg_packages"
set(CMAKE_TOOLCHAIN_FILE "${CMAKE_SOURCE_DIR}/../vcpkg/scripts/buildsystems/vcpkg.cmake" CACHE STRING "")
set(VCPKG_INSTALLED_DIR "${CMAKE_SOURCE_DIR}/vcpkg_packages" CACHE PATH "vcpkg install dir")

project(anson.cmake LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_compile_options(/utf-8)

# I can't solve the MSVC mojibake problem. You might be better remove any MSVC kit's language packs other than English.
# add_compile_options("$<$<CXX_COMPILER_ID:MSVC>:/utf-8>")
# if(MSVC)
# This forces MSVC to report errors in a way that avoids some encoding issues
# add_compile_options(/source-charset:utf-8 /execution-charset:utf-8)
# endif()

# Generate compile_commands.json for clangd/IDE integration (single-config only)
if(NOT CMAKE_CONFIGURATION_TYPES)
  set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
endif()

find_package(EnTT CONFIG REQUIRED)
find_package(nlohmann_json CONFIG REQUIRED)

add_subdirectory(src)

option(ANSON_BUILD_TESTS "Build tests for Anson.cmake" ON)
if (ANSON_BUILD_TESTS)
  enable_testing()
  add_subdirectory(tests)
endif()
