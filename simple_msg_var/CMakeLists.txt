cmake_minimum_required(VERSION 2.8.3)
project(simple_msg_var)

find_package(catkin REQUIRED)

catkin_package()
add_library(the_library src/lib.cpp)
add_dependencies(the_library ${${PROJECT_NAME}_EXPORTED_TARGETS})
