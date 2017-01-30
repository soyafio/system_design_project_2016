#!/usr/bin/python
# -*- coding: utf-8 -*-
# license removed for brevity
# described by kazushi yamashina

import rospy
from create_ctl.msg import myState
from createstate import driveState as ds
from roomba_runrun import DEBUG as debug
DEBUG = debug

class Soya(object):
	"""docstring for ClassName"""
	def __init__(self):
		rospy.init_node('roomber', anonymous=True)
		self.makoto_sub = None
		self.bumper_sub = None
		self.ope_pub = rospy.Publisher('operation_state', myState, queue_size=100)

		self.bumper_state = 0
		self.sensor_data = 0
		self.ope_msg = myState()
		self.state = ds['stop']

	def check_bamper(self, data):
		self.bumper_state = data.state
		print "subscribed bumper state is %s"%(data.state)
		self.bumper_sub.unregister()

	def makoto_callback(self, data):
		self.sensor_data = data.state
		self.makoto.unregister()

	def subscribe_bumper(self):
		self.bumper_sub = None
		self.bumper_sub = rospy.Subscriber('roomba_bumper',myState, self.check_bamper, self.bumper_sub)
	def subscribe_makoto(self):
		self.makoto_sub = None
		self.makoto_sub = rospy.Subscriber('input_data',myState, self.makoto_callback, self.makoto_sub)

	def subscribe_all_msg(self):
		self.subscribe_bumper()
		self.subscribe_makoto()

	def roomber_fsm(self):
		r = rospy.Rate(1)
		while not rospy.c():
			# ステートマシンを書く
			if self.state == ds['stop']:
				self.ope_msg.state = ds['run'] # ルンバを動かすためのコマンド
				self.ope_pub.publish(self.ope_msg) # Roomba_runrun_nodeへpublish
				print "publsihed to operation_state"
				self.subscribe_all_msg()
				self.state = ds['run']
				bot.drive(95, 1)

			elif self.state == ds['run']:
				self.ope_msg.state = ds['stop'] # ルンバを動かすためのコマンド
				self.ope_pub.publish(self.ope_msg) # Roomba_runrun_nodeへpublish
				print "publsihed to operation_state"
				self.subscribe_all_msg()
				self.state = ds['stop']

			else:
				continue
			r.sleep()

def soya_operaion_main():
	soya = Soya()
	soya.roomber_fsm()

if __name__ == '__main__':
soya_operaion_main()