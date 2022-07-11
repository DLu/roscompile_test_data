cmake_minimum_required(VERSION 2.8.3)
project(minimal_package)
find_package(catkin REQUIRED COMPONENTS geometry_msgs rospy)
catkin_package(CATKIN_DEPENDS geometry_msgs rospy)
catkin_install_python(PROGRAMS scripts/node.py
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
