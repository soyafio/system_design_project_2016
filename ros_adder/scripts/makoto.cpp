// ros/ros.h　ROSに関する基本的なAPIのためのヘッダ
#include "ros/ros.h"
// image_tutorial/image.h　image.msgから生成されたメッセージを定義しているヘッダ
#include "image_tutorial/image.h"

#include <stdlib.h>
#include <iostream>
using namespace std;

int main(int argc, char** argv)
{
  // 初期化宣言
  // このノードは"publisher"という名前であるという意味
  ros::init(argc, argv, "publisher");
  // ノードハンドラの宣言
  ros::NodeHandle n;
  //　Publisherとしての定義
  // n.advertise<image_tutorial::image>("image_data", 1000);
  // image_tutorial::image型のメッセージをimage_dataというトピックへ配信する
  //"1000"はトピックキューの最大値
  ros::Publisher pub = n.advertise<image_tutorial::image>("image_data", 1000);
  //1秒間に1回の間隔でループする
  ros::Rate loop_rate(1);

  //image_tutorial::image型のオブジェクトを定義
  //image.msgで定義したflameID,imgはメンバ変数としてアクセスできる
  image_tutorial::image msg;

  // 変数imgはsensor_msgs/Image型である
  // この型はもともとメンバ変数を持った型なので以下のような使い方でアクセスできる
  msg.img.height = 480;
  msg.img.width  = 640;
  msg.img.encoding = "rgb8"; 
  msg.img.step =  msg.img.width;

  // sensor_msgs/Image型のデータ部にデータをプッシュバックしている
  //　実際はOpenCVなどで画像のRGB情報を得たあと，データを格納する
  for(int i = 0; i <  msg.img.height; i++){
    for (int j = 0; j < msg.img.width; j++){
      msg.img.data.push_back(0xFF);
    }
  }

  int frameid = 0;
  //ノードが実行中は基本的にros::ok() = 1
  // Ctrl + Cなどのインタラプトが起こるとros::ok() = 0となる
  while (ros::ok())
  {
    msg.frameID = frameid;
    // Publishする関数
    pub.publish(msg);
    cout << "published !" << endl;
    ros::spinOnce();
    frameid++;

    loop_rate.sleep();
  }
  return 0;
}