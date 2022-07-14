cmake_minimum_required(VERSION 3.8)
project(minimal_package)
find_package(ament_cmake REQUIRED)
install(FILES config/basic.rviz config/everything.rviz
        DESTINATION share/${PROJECT_NAME}/config
)
ament_package()
