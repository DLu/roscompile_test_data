cmake_minimum_required(VERSION 2.8.3)
project(basic_cpp_with_include)
find_package(catkin REQUIRED)
catkin_package()
add_executable(node src/node.cpp)
install(TARGETS node
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
install(DIRECTORY include/${PROJECT_NAME}/
        DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)
