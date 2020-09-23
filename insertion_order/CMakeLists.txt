cmake_minimum_required(VERSION 2.8.3)
project(minimal_package)
find_package(catkin REQUIRED COMPONENTS diagnostic_msgs nav_msgs shape_msgs)
catkin_package(
    CATKIN_DEPENDS diagnostic_msgs nav_msgs shape_msgs
)
add_executable(node src/node.cpp)
