#include <rclcpp/rclcpp.hpp>
#include <actionlib_msgs/GoalStatus.h>
#include <diagnostic_msgs/KeyValue.h>
#include <geometry_msgs/Point.h>
#include <nav_msgs/Path.h>
#include <sensor_msgs/Joy.h>
#include <shape_msgs/Plane.h>
#include <stereo_msgs/DisparityImage.h>


int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto n = std::make_shared<rclcpp::Node>("roscompile");

  while (rclcpp::ok())
  {
    rclcpp::spin_some(n);
  }

  return 0;
}
