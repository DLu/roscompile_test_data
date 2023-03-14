cmake_minimum_required(VERSION 3.8)
project(minimal_package)
find_package(ament_cmake REQUIRED)
add_library(the_library src/my_plugin.cpp)
install(TARGETS the_library
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        RUNTIME DESTINATION bin
        EXPORT export_the_library
)
ament_export_targets(export_the_library)
ament_package()
