cmake_minimum_required(VERSION 2.8.3)
project(simple_msg)

find_package(catkin REQUIRED COMPONENTS actionlib_msgs geometry_msgs message_generation)

catkin_package(CATKIN_DEPENDS actionlib_msgs geometry_msgs message_runtime)
add_service_files(FILES Simple.srv)
add_action_files(FILES ActionJackson.action)
generate_messages(DEPENDENCIES actionlib_msgs geometry_msgs)
