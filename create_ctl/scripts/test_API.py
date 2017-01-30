#!/usr/bin/python
# -*- coding: utf-8 -*-

import create2api
import time

#Create a Create2. This will automatically try to connect to your
#   robot over serial
bot = create2api.Create2()

#Start the Create2
bot.start()

#Put the Create2 into 'safe' mode so we can drive it
bot.safe()

bot.drive(95, 1)

bot.digit_led_ascii('ROOM')

#while True:
#	bot.play_test_sound()


while True:
#バンパの状態を延々と得る
	for i in range(0,10):
		bot.get_packet(7)
		Right = bot.sensor_state['wheel drop and bumps']['bump right']
		Left = bot.sensor_state['wheel drop and bumps']['bump left']
		print Right
		print Left
		time.sleep(0.5)

		if Right or Left == True:
			bot.drive(0, 0)
			print 'stop'
			bot.stop()
			break
	break



#Close the connection
#bot.destroy()