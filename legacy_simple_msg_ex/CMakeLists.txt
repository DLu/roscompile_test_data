cmake_minimum_required(VERSION 2.8.3)
project(legacy_simple_msg_ex)
find_package(catkin REQUIRED)
catkin_package()
add_executable(node src/node.cpp)
add_dependencies(node ${catkin_EXPORTED_TARGETS} ${PKG_NAME}_generate_messages_cpp)

add_executable(node2 src/node.cpp)
add_dependencies(node2 ${catkin_EXPORTED_TARGETS} ${PKG_NAME}_gencpp)

add_executable(node3 src/node.cpp)
add_dependencies(node3 ${catkin_EXPORTED_TARGETS} legacy_simple_msg_ex_generate_messages_cpp)

add_executable(node4 src/node.cpp)
add_dependencies(node4 ${catkin_EXPORTED_TARGETS} legacy_simple_msg_ex_gencpp)

add_executable(node5 src/node.cpp)
add_dependencies(node5 ${catkin_EXPORTED_TARGETS} ${PKG_NAME}_generate_messages_cpp ${simple_msg_ex_EXPORTED_TARGETS})
