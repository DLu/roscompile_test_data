cmake_minimum_required(VERSION 2.8.3)
project(minimal_package)
find_package(catkin REQUIRED COMPONENTS actionlib_msgs diagnostic_msgs geometry_msgs nav_msgs roscpp sensor_msgs shape_msgs stereo_msgs)
catkin_package(
    CATKIN_DEPENDS actionlib_msgs diagnostic_msgs geometry_msgs nav_msgs roscpp sensor_msgs shape_msgs stereo_msgs
)
add_executable(node src/node.cpp)
