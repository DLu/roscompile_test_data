#!/usr/bin/python

import rospy
from geometry_msgs.msg import PointStamped

rospy.init_node('asdf')
pub = rospy.Publisher('/plam', PointStamped, queue_size=1)
rospy.spin()
