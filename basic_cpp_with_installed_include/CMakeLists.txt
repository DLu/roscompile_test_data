cmake_minimum_required(VERSION 3.8)
project(basic_cpp_with_include)
find_package(ament_cmake REQUIRED)
add_executable(node src/node.cpp)
install(TARGETS node
        DESTINATION lib/${PROJECT_NAME}
)
install(DIRECTORY include/
        DESTINATION include
)
ament_export_include_directories(include)
ament_package()
