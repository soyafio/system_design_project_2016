#!/usr/bin/python
# -*- coding: utf-8 -*-
# license removed for brevity
# described by kazushi yamashina

import rospy
import create2api
import time

from createstate import bumperState as bs
from create_ctl.msg import myState
DEBUG = True
class Roomba_runrun(object):

	def __init__(self):

		# ROSのノードを宣言
		# ROSシステムの中で唯一の名前にしなけばならない
		rospy.init_node('Roomba_runrun_node', anonymous=True)

		# Publisherのインスタンス
		self.roomba_bumper_pub = rospy.Publisher('roomba_bumper', myState, queue_size=100)
		# Subscriberのインスタンス
		self.roomba_drive_sub = rospy.Subscriber('operation_state', myState, self.drive_callback)

		# bamperのステートを送るためのメッセージ
		self.bumper_msg = myState()

		if DEBUG == False:
			# roombaを動かすために初期化処理
			# 初期化のために作った"bot"はクラスの中で共有
			# Create a Create2. This will automatically try to connect to your
			# robot over serial
			self.bot = create2api.Create2()
			#Start the Create2
			self.bot.start()
			#Put the Create2 into 'safe' mode so we can drive it
			self.bot.safe()

	def roomba_bumper(self):
		# r = rospy.Rate(2)
		if DEBUG == False:
			self.bot.get_packet(7)
			Right = self.bot.sensor_state['wheel drop and bumps']['bump right']
			Left = self.bot.sensor_state['wheel drop and bumps']['bump left']
		else:
			Right = True
			Left = True

		if Right or Left == True:
			self.bumper_msg.state = 1
			self.roomba_bumper_pub.publish(bs['collision'])
			bot.drive(0, 0)
			print 'collision'
			
		else:
			msg.state = 0
			self.roomba_bumper_pub.publish(bs['safe'])
		print "publsihed to roomba_bumper"

	def drive_callback(self, data):
		 if data.state == 5 :
		 	bot.drive(95, 1)
			self.sleep(2)

		 elif data.state == 4 :
		 	bot.drive(95, 1)
			self.sleep(1)

		 elif data.state == 2 :
		 	bot.drive(95, -1)
			self.sleep(1)

		 elif data.state == 1 :
		 	bot.drive(95, -1)
			self.sleep(2)

		print "subscribed drive state is %s"%(data.state)
		self.roomba_bumper()

	# 以下にルンバを動かすメソッドを実装
	def roomba_go(self, time, zengo, sayu):
		pass

def roomba_runrun_main():
	soya = Roomba_runrun()
	rospy.spin()


if __name__ == '__main__':
roomba_runrun_main()