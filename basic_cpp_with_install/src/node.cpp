#include <rclcpp/rclcpp.hpp>
#include "std_msgs/msg/string.hpp"
#include <tf2_ros/transform_listener.h>  // unused, but forces the dependency

int main(int argc, char **argv)
{
  using namespace std::chrono_literals;
  rclcpp::init(argc, argv);
  auto n = std::make_shared<rclcpp::Node>("roscompile");
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr chatter_pub = n->create_publisher<std_msgs::msg::String>("chatter", 1000);

  while (rclcpp::ok())
  {
    auto message = std_msgs::msg::String();
    message.data = "roscompile rules";
    chatter_pub->publish(message);
    rclcpp::spin_some(n);
    rclcpp::sleep_for(100ms);
  }

  return 0;
}
