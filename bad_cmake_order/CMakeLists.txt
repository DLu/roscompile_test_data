cmake_minimum_required(VERSION 2.8.3)
project(minimal_package)
add_service_files()

install()
set_directory_properties(PROPERTIES COMPILE_OPTIONS "-std=c++11;-Wall;-Werror")
catkin_python_setup()
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()
add_action_files()
some_bizzare_command()
generate_dynamic_reconfigure_options()
catkin_package()

add_library(library src/library.cpp)

add_executable(node src/node.cpp)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
add_dependencies(node ${catkin_EXPORTED_TARGETS})
add_dependencies(library ${catkin_EXPORTED_TARGETS})
target_link_libraries(library ${catkin_LIBRARIES})
target_link_libraries(node ${catkin_LIBRARIES})

include_directories()
generate_messages()

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)

  add_executable(etest test/etest.cpp)
  find_package(catkin REQUIRED COMPONENTS roslint)
  add_rostest(test/etest.launch)
  target_link_libraries(etest ${GTEST_LIBRARIES})

  roslint_cpp()
  roslint_add_test()

  catkin_add_gtest(vtest test/vtest.cpp)
endif()
add_message_files()
find_package(catkin REQUIRED)
catkin_install_python()
