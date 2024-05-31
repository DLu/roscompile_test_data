#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped


def main(args=None):
    rclpy.init(args=args)
    node = Node('asdf')
    node.create_publisher(PointStamped, '/plam', 1)
    rclpy.spin(node)


if __name__ == '__main__':
    main()
