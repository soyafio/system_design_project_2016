#!/usr/bin/python
# -*- coding: utf-8 -*-
# license removed for brevity

import create2api
import time
import rospy

# 自分で定義したmessageファイルから生成されたモジュール
from create_ctl.msg import State
# State.msgにはstateという変数をもつ
def Roomba_bumper():
	rospy.init_node('Roomba_bumper_node', anonymous=True)
	# nodeの宣言 : publisherのインスタンスを作る
	# Roomba_bumperというtopicにInt8型のmessageを送るPublisherをつくった
	pub = rospy.Publisher('Roomba_bumper', State, queue_size=100)

	# 1秒間にpublishする数の設定
	r = rospy.Rate(2)

	#Create a Create2. This will automatically try to connect to your
	#   robot over serial
	bot = create2api.Create2()

	#Start the Create2
	bot.start()

	#Put the Create2 into 'safe' mode so we can drive it
	bot.safe()

	msg = State()
	msg.state = 0
	
	#バンパの状態を延々と得る
	while not rospy.is_shutdown():
			bot.get_packet(7)
			Right = bot.sensor_state['wheel drop and bumps']['bump right']
			Left = bot.sensor_state['wheel drop and bumps']['bump left']

			if Right or Left == True:
				msg.state = 1
				pub.publish(msg)

			else:
				msg.state = 0
				pub.publish(msg)

			r.sleep(1)


if __name__ == '__main__':
	try:
			Roomba_bumper()

	except rospy.ROSInterruptException: pass