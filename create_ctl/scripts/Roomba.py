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

bot.digit_led_ascii('VOOV')

while True:
	bot.play_test_sound()


while True:
#バンパの状態を延々と得る
	for i in range(0,10):
		bot.get_packet(7)
		Right = bot.sensor_state['wheel drop and bumps']['bump right']
		Left = bot.sensor_state['wheel drop and bumps']['bump left']
		print  Right
		print  Left
		time.sleep(1)

		if Right or Left == True:
			break
print 'stop'


#Close the connection
bot.destroy()