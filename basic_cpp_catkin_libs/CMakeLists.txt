cmake_minimum_required(VERSION 3.8)
project(minimal_package)
find_package(ament_cmake REQUIRED)
add_executable(node src/node.cpp)
ament_target_dependencies(node
  rclcpp
  std_msgs
  tf2_ros
)
ament_package()
