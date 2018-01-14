cmake_minimum_required(VERSION 2.8.3)
project(minimal_package)
add_service_files()

install()
set_directory_properties(PROPERTIES COMPILE_OPTIONS "-std=c++11;-Wall;-Werror")
catkin_python_setup()
add_action_files()
generate_dynamic_reconfigure_options()
catkin_package()

add_library(library src/library.cpp)

add_executable(node src/node.cpp)
add_dependencies(node ${catkin_EXPORTED_TARGETS})
add_dependencies(library ${catkin_EXPORTED_TARGETS})
target_link_libraries(library ${catkin_LIBRARIES})
target_link_libraries(node ${catkin_LIBRARIES})

include_directories()
catkin_install_python()
generate_messages()

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  find_package(catkin REQUIRED COMPONENTS roslint)

  add_executable(etest test/etest.cpp)
  target_link_libraries(etest ${GTEST_LIBRARIES})
  add_rostest(test/etest.launch)

  roslint_cpp()
  roslint_add_test()

  catkin_add_gtest(vtest test/vtest.cpp)
endif()
add_message_files()
find_package(catkin REQUIRED)
