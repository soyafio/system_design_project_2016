#!/usr/bin/python
# -*- coding: utf-8 -*-
# license removed for brevity
import rospy
from ros_adder.msg import Adder

# Subscribeする対象のトピックが更新されたら呼び出されるコールバック関数
# 引数にはトピックにPublishされるメッセージの型と同じ型を定義する
def callback(data):
    # 受けとったmessageの中身 → a
    print data.a

def adder():
    rospy.init_node('adder', anonymous=True)

    # Subscriberとしてimage_dataというトピックに対してSubscribeし、トピックが更新されたときは
  # callbackという名前のコールバック関数を実行する
  #input_data に麻琴が送って私が見る
    rospy.Subscriber('input_data', Adder, callback)

    rospy.Subscriber('Roomba_bumper', Adder, callback)

    # トピック更新の待ちうけを行う関数
    rospy.spin()

if __name__ == '__main__':
    adder()
