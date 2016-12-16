#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

def run_straight():
	rospy.init_node('run_straight', anonymous=True)
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
	r = rospy.Rate(0.5)
	msg = Twist()

	msg.linear.x = 0
	msg.linear.y = 0
	msg.linear.z = 0

	msg.angular.x = 1
	msg.angular.y = 0
	msg.angular.z = 0

	while not rospy.is_shutdown():
		pub.publish(msg)
		print "published"
		r.sleep()

if __name__ == '__main__':
	try:
		run_straight()

	except rospy.ROSInterruptException: pass