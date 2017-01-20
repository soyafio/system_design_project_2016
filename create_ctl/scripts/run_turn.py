#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from time import sleep
from geometry_msgs.msg import Twist

def run_turn():
	rospy.init_node('run_turn', anonymous=True)
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
	r = rospy.Rate(1)
	msg = Twist()

	msg.linear.x = 1
	# +MAE -USIRO

	msg.angular.z = 0
	# +HIDARI -MIGI


	msg3 = Twist()
	msg3.angular.z = 0

	r.sleep()
	pub.publish(msg)
	print "straight1"
	sleep(3.2)

	pub.publish(msg3)
	print "stop"
	r.sleep()


if __name__ == '__main__':
	try:
		run_turn()

	except rospy.ROSInterruptException: pass

