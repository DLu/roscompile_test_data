cmake_minimum_required(VERSION 3.8)
project(minimal_package)
find_package(ament_cmake REQUIRED)

# This one should remove the /config
install(DIRECTORY config
        DESTINATION share/${PROJECT_NAME}
)

# This one should not change because of the trailing slash
install(DIRECTORY launch/
        DESTINATION share/${PROJECT_NAME}/launch
)
ament_package()
