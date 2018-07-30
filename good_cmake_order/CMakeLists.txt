cmake_minimum_required(VERSION 2.8.3)
project(minimal_package)
set_directory_properties(PROPERTIES COMPILE_OPTIONS "-std=c++11;-Wall;-Werror")
find_package(catkin REQUIRED)
catkin_python_setup()
add_message_files()
add_service_files()
add_action_files()
generate_dynamic_reconfigure_options()
generate_messages()
catkin_package()

include_directories()

add_library(library src/library.cpp)
add_dependencies(library ${catkin_EXPORTED_TARGETS})
target_link_libraries(library ${catkin_LIBRARIES})

add_executable(node src/node.cpp)
add_dependencies(node ${catkin_EXPORTED_TARGETS})
target_link_libraries(node ${catkin_LIBRARIES})

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

install()
catkin_install_python()
