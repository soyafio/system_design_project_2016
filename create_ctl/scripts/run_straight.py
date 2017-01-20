#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from time import sleep
from geometry_msgs.msg import Twist

def run_straight():
	# ROSのノードを宣言
	# ROSシステムの中で唯一の名前にしなけばならない
	rospy.init_node('run_straight', anonymous=True)
	# Publisherのインスタンス
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
	# r = rospy.Rate(3)
	
	msg_mae = Twist()
	msg_mae.linear.x = 1
	msg_mae.angular.z = 0

	msg_R = Twist()
	msg_R.linear.x = 0
	msg_R.angular.z = -0.8

	msg_L = Twist()
	msg_L.linear.x = 0
	msg_L.angular.z = 0.8

	msg_stop = Twist()
	msg_stop.linear.x = 0
	msg_stop.angular.z = 0

	sleep(1)
	pub.publish(msg_mae)
	print "straight"
	sleep(3.2)


	pub.publish(msg_L)
	print "turn Left"
	sleep(2)

	pub.publish(msg_mae)
	print "straight"
	sleep(7)

	pub.publish(msg_L)
	print "turn Left"
	sleep(1.8)

	pub.publish(msg_mae)
	print "straight"
	sleep(5)

	pub.publish(msg_stop)
	print "stop"
	sleep(1)


# senser
#return =1
#




if __name__ == '__main__':
	try:
		run_straight()

	except rospy.ROSInterruptException: pass
