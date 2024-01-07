cmake_minimum_required(VERSION 3.8)
project(my_cpp_py_pkg)
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
add_executable(node src/node.cpp)
install(TARGETS node
        DESTINATION lib/${PROJECT_NAME}
)
install(FILES resource/my_cpp_py_pkg
        DESTINATION share/${PROJECT_NAME}/resource
)
install(PROGRAMS scripts/cursive scripts/pilot.py scripts/rex
        DESTINATION lib/${PROJECT_NAME}
)
ament_python_install_package(${PROJECT_NAME})
ament_package()
