cmake_minimum_required(VERSION 2.8.3)
project(simple_msg)

find_package(catkin REQUIRED)

catkin_package()
add_library(the_library src/lib.cpp)
