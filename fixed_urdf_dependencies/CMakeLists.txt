cmake_minimum_required(VERSION 2.8.3)
project(minimal_package)
find_package(catkin REQUIRED)
catkin_package()
install(FILES urdf/r2d2.urdf.xacro
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf
)
