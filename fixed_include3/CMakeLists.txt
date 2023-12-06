cmake_minimum_required(VERSION 3.8)
project(basic_cpp_with_include)
find_package(ament_cmake REQUIRED)
add_executable(node src/node.cpp)
target_include_directories(node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)
ament_package()
