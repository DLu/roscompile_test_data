cmake_minimum_required(VERSION 2.8.3)
project(minimal_package)
find_package(catkin REQUIRED)
catkin_package()
add_executable(node src/node.cpp)
install(TARGETS node
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
