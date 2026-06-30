cmake_minimum_required(VERSION 3.21)
project(surrealtree LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(${PROJECT_NAME} src/main.cpp)

# find_package(Slint REQUIRED)
include(FetchContent)
FetchContent_Declare(
    Slint
    GIT_REPOSITORY https://github.com/slint-ui/slint.git
    GIT_TAG release/1
    SOURCE_SUBDIR api/cpp
)
FetchContent_MakeAvailable(Slint)

get_filename_component(SURREALISM_UI_DIR 
    "${CMAKE_CURRENT_SOURCE_DIR}/../surrealism-ui-nightly" 
    ABSOLUTE
)

FetchContent_Declare(
    webview
    GIT_REPOSITORY https://github.com/webview/webview
    GIT_TAG 0.12.0
    )
FetchContent_MakeAvailable(webview)

message(STATUS "=========================================== CMAKE_CURRENT_SOURCE_DIR = ${CMAKE_CURRENT_SOURCE_DIR}")
message(STATUS "=========================================== SURREALISM_UI_DIR = ${SURREALISM_UI_DIR}")
message(STATUS "=========================================== webview_SOURCE_DIR = ${webview_SOURCE_DIR}")


target_include_directories(${PROJECT_NAME} PRIVATE 
    ${webview_SOURCE_DIR}
)

target_link_libraries(${PROJECT_NAME} PRIVATE
    webview::core # V0.12.0 Not webview::webview or webview. don't trust Gemini too much.
    Slint::Slint
)

slint_target_sources(${PROJECT_NAME}
    ui/app-window.slint
    LIBRARY_PATHS "surrealism=${SURREALISM_UI_DIR}"
)

# On Windows, copy the Slint DLL next to the application binary so that it's found.
if (WIN32)
    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_RUNTIME_DLLS:${PROJECT_NAME}> $<TARGET_FILE_DIR:${PROJECT_NAME}> COMMAND_EXPAND_LISTS)
endif()
