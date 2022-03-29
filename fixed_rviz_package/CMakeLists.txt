cmake_minimum_required(VERSION 2.8.3)
project(minimal_package)
find_package(catkin REQUIRED)
catkin_package()
install(FILES config/basic.rviz config/everything.rviz
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
)
