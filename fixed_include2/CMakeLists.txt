cmake_minimum_required(VERSION 3.8)
project(minimal_package)
find_package(ament_cmake REQUIRED)
add_executable(node src/node.cpp)
target_include_directories(node PUBLIC
  $<INSTALL_INTERFACE:include>
)
ament_package()
