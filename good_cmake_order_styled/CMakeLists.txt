cmake_minimum_required(VERSION 2.8.3)
project(minimal_package)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()
set_directory_properties(PROPERTIES COMPILE_OPTIONS "-std=c++11;-Wall;-Werror")
add_compile_options(-Wall -Wextra -Wpedantic)
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(aim_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
rosidl_generate_interfaces()

add_library(library src/library.cpp)
ament_target_dependencies(library std_msgs)

add_executable(node src/node.cpp)

target_include_directories(node x)
ament_target_dependencies(node rclcpp)

install()
ament_python_install_module()
ament_python_install_package(${PROJECT_NAME})
ament_export_include_directories(include)
ament_export_dependencies(rosidl_default_runtime)
ament_export_targets(export_the_library)
pluginlib_export_plugin_description_file(polygon_base polygon_base_plugins.xml)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  find_package(rostest REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)

  add_executable(etest test/etest.cpp)
  target_link_libraries(etest ${GTEST_LIBRARIES})
  add_rostest(test/etest.launch)

  catkin_add_gtest(vtest test/vtest.cpp)

  ament_lint_auto_find_test_dependencies()
endif()
ament_package()
