#include <ros/ros.h>
#include "std_msgs/String.h"
#include <tf/tf.h> // unused, but forces the dependency
#include <basic_cpp_with_include/its_a_header.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);

  ros::Rate loop_rate(10);
  while (ros::ok())
  {
    std_msgs::String msg;
    msg.data = "roscompile rules";
    chatter_pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}
