cmake_minimum_required(VERSION 3.8)
project(my_cpp_py_pkg)
find_package(ament_cmake REQUIRED)
add_executable(node src/node.cpp)
ament_package()
