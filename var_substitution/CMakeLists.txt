cmake_minimum_required(VERSION 2.8.3)
project(simple_msg)

find_package(catkin REQUIRED)

set(SOURCE_FILES src/lib.cpp)

catkin_package()
add_library(${PROJECT_NAME} ${SOURCE_FILES})
