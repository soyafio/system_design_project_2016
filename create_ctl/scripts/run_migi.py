#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

def run_turn():
	rospy.init_node('run_turn', anonymous=True)
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
	r = rospy.Rate(1)
	msg = Twist()

	msg.linear.x = 0
	msg.linear.y = 0
	msg.linear.z = 1

	while not rospy.is_shutdown():
		
		pub.publish(msg)
		print "published"
		msg.linear.x = msg.linear.x *(-1)
		r.sleep()


if __name__ == '__main__':
	try:
		run_turn()

	except rospy.ROSInterruptException: pass

