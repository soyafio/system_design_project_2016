#!/usr/bin/python
# -*- coding: utf-8 -*-
# license removed for brevity
import rospy

from geometry_msgs.msg import Twist
from create_ctl.msg import State

class Roomba_runrun:

	def __init__(self):

		# ROSのノードを宣言
		# ROSシステムの中で唯一の名前にしなけばならない
		rospy.init_node('roomber', anonymous=True)
		# Publisherのインスタンス
		self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)		
		self.msg = Twist()

	# ルンバを動かす関数
	def roomba_go(self, time, zengo, sayu):
		self.msg.linear.x = zengo
		self.msg.angular.z = sayu
		self.pub.publish(msg)
		print ":-)"
		self.sleep(time)

	# 麻琴からもらった値によって方向転換
def callback(data):
    # 受けとったmessageの中身 → a
    mode = data.state
	
def bumper(data):
	if data.state == 1
		#soya.roomba_go(1,0,0)
		#soya.roomba_go(0.3,-1,0)
		print data.state

#		if mode == 1
#    		soya.roomba_go(2,0,-1)

#    	elif mode == 2
#    		soya.roomba_go(1,0,-1)

# 		elif mode == 4
#    		soya.roomba_go(1,0,1)

# 		elif mode == 5
#    		soya.roomba_go(2,0,1)

def main():

	bot = create2api.Create2()

	#Start the Create2
	bot.start()

	#Put the Create2 into 'safe' mode so we can drive it
	bot.safe()

	# ルンバディスプレイへの文字表示
	bot.digit_led_ascii('PPAP')

	# マックのポテトの音を流し続ける
#	while True:
#	bot.play_test_sound()

	soya = Roomba_runrun()

	while not rospy.is_shutdown():
		soya.roomba_go(1,1,0)


def soya():
    rospy.init_node('soya', anonymous=True)

  #input_data に麻琴が送って私が見る
    rospy.Subscriber('input_data', Int8, callback)

    rospy.Subscriber('Roomba_bumper', Int8, bumper)

    # トピック更新の待ちうけを行う関数
    rospy.spin()

if __name__ == '__main__':
	soya()