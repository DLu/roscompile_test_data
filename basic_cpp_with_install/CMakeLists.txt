cmake_minimum_required(VERSION 3.8)
project(minimal_package)
find_package(ament_cmake REQUIRED)
add_executable(node src/node.cpp)
install(TARGETS node
        DESTINATION lib/${PROJECT_NAME}
)
ament_package()
