cmake_minimum_required(VERSION 3.20)
project(MyGoogleTestExample LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# ── Download GoogleTest automatically (no manual install needed) ──
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
  # You can also use GIT_REPOSITORY https://github.com/google/googletest.git
  #    GIT_TAG        main   # or a specific release tag
)
# For Windows: prevent overriding parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# ── Our production code (can be static lib or just headers) ──
add_library(math_utils INTERFACE)
target_include_directories(math_utils INTERFACE src)

# ── The test executable ──
add_executable(tests
    tests/test_math_utils.cpp
)

target_link_libraries(tests
    PRIVATE
        math_utils
        gtest
        gtest_main          # ← provides main() automatically!
)

# Optional: make CMake discover all tests automatically
include(GoogleTest)
gtest_discover_tests(tests)