cmake_minimum_required(VERSION 3.8)
project(minimal_package)
find_package(ament_cmake REQUIRED)
install(FILES c3po.urdf core.launch
        DESTINATION share/${PROJECT_NAME}
)
install(FILES launch/test.launch
        DESTINATION share/${PROJECT_NAME}/launch
)
install(FILES urdf/r2d2.urdf
        DESTINATION share/${PROJECT_NAME}/urdf
)
ament_package()
