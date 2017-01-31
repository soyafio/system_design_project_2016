#!/usr/bin/python
# -*- coding: utf-8 -*-
# license removed for brevity
import rospy
import create2api
import time

from geometry_msgs.msg import Twist
# State.msgにはstateという変数をもつ
from create_ctl.msg import State

class Roomba_runrun:

	def __init__(self):

		# ROSのノードを宣言
		# ROSシステムの中で唯一の名前にしなけばならない
		rospy.init_node('roomber', anonymous=True)
		# Publisherのインスタンス
		
		self.msg = Twist()
		self.sasaki_mode = 0
		self.my_state = 0
		self.bot = create2api.Create2()
		#Start the Create2
		self.bot.start()
		#Put the Create2 into 'safe' mode so we can drive it
		self.bot.full()

		# ルンバディスプレイへの文字表示
		self.bot.digit_led_ascii('O_O ')

		# マックのポテトの音を流し続ける
#		while True:
#			self.bot.play_test_sound()

	def makoto_callback(self,data):
		# 受けとったmessageの中身をmodeに
		print "subscribed %s"%data.state
		self.sasaki_mode = data.state
		self.makoto_sub.unregister()

	def subscribe_makoto(self):
		self.makoto_sub = None
		self.makoto_sub = rospy.Subscriber('input_data',State, self.makoto_callback, self.makoto_sub)

	def roomba_bumper(self):
		print "check bumper"
		#バンパの状態を延々と得る
		self.bot.get_packet(7)
		Right = self.bot.sensor_state['wheel drop and bumps']['bump right']
		Left = self.bot.sensor_state['wheel drop and bumps']['bump left']

		if Right ==True or Left == True:
			self.bot.drive(0,0)
			self.bot.digit_led_ascii(' -_-')
			print "collision"
			return True
		else:
			return False


	def direction(self, mode):

		#turn right 90
		if mode == 1: 
			self.bot.drive(95, -1)
			time.sleep(1.7)
		#turn right 45
		elif mode == 2:
			self.bot.drive(95, -1)
			time.sleep(1)
		# turn left 45
		elif mode == 4:
			self.bot.drive(95, 1)
			time.sleep(1)

		# turn left 90
		elif mode == 5:
			self.bot.drive(95, 1)
			time.sleep(1.7)


	def main(self):

		# state 0 : go straight
		print "start roomba"
		r = rospy.Rate(2)
		while not rospy.is_shutdown():
			if self.my_state == 0:
				print "state %s"%self.my_state
				self.bot.drive(250, 32767)
				self.bot.digit_led_ascii('O_O ')
				
				if self.roomba_bumper() == True:
					self.my_state = 1

			elif self.my_state == 1:
				print "state %s"%self.my_state
				self.subscribe_makoto()
				self.direction(self.sasaki_mode)
				self.bot.drive(250, 32767)
				self.my_state = 0
				

			else:
				continue
			r.sleep()


if __name__ == '__main__':
	soya = Roomba_runrun()
	soya.main()