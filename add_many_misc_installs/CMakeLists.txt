cmake_minimum_required(VERSION 3.8)
project(minimal_package)
find_package(ament_cmake REQUIRED)
install(FILES launch/core.launch
        DESTINATION share/${PROJECT_NAME}/launch
)
ament_package()
