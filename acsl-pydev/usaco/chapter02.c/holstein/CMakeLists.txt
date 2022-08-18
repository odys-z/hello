cmake_minimum_required(VERSION 3.5)

project(holstein LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(holstein main.cpp)

add_definitions(-std=c++11)
