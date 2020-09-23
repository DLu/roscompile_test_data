#include <ros/ros.h>
#include <actionlib_msgs/GoalStatus.h>
#include <diagnostic_msgs/KeyValue.h>
#include <geometry_msgs/Point.h>
#include <nav_msgs/Path.h>
#include <sensor_msgs/Joy.h>
#include <shape_msgs/Plane.h>
#include <stereo_msgs/DisparityImage.h>


int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  while (ros::ok())
  {
    ros::spinOnce();
  }

  return 0;
}
