#!/usr/bin/python
# -*- coding: utf-8 -*-

import create2api
import rospy
from time import sleep
from geometry_msgs.msg import Twist
from ros_adder.msg import Adder

class Roomba_runrun:

	def __init__(self):

		# ROSのノードを宣言
		# ROSシステムの中で唯一の名前にしなけばならない
		rospy.init_node('run_straight', anonymous=True)
		# Publisherのインスタンス
		self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)		
		self.msg = Twist()

	def roomba_go(self, time, zengo, sayu):
		self.msg.linear.x = zengo
		self.msg.angular.z = sayu
		self.pub.publish(msg)
		print ":-)"
		self.sleep(time)

	def makoto(data):
		soya = Roomba_runrun()

		if data.a == 1:   # 麻琴からreturn=1
		soya.roomba_go(?,1,-2)

		if 



def main():

	bot = create2api.Create2()

	#Start the Create2
	bot.start()

	#Put the Create2 into 'safe' mode so we can drive it
	bot.safe()

	

	soya = Roomba_runrun()

	soya.roomba_go(3,1,0)



if __name__ == '__main__':
	try:
		run_straight()

	except rospy.ROSInterruptException: pass
