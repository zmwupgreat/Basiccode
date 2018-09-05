#include<iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv/cv.h>
#include <stdlib.h>
#include <Windows.h>

using namespace std;
using namespace cv;
void showvideo();
void showvideo()
{

	Mat frame1, frame2;
	VideoCapture cap1, cap2;
	int cont = 0;
	while (frame1.rows < 2) {
		cap1.open(700);
		cap1.set(CAP_PROP_FOURCC, 'GPJM');
		cap1.set(CAP_PROP_FRAME_WIDTH, 1280);
		cap1.set(CAP_PROP_FRAME_HEIGHT, 480);
		cont = 0;
		while (frame1.rows < 2 && cont<5) {
			cap1 >> frame1;
			cont++;
		}
	}/*
	 while (frame2.rows < 2) {
	 cap2.open(701);
	 cap2.set(CAP_PROP_FOURCC, 'GPJM');
	 cap2.set(CAP_PROP_FRAME_WIDTH, 1280);
	 cap2.set(CAP_PROP_FRAME_HEIGHT, 480);
	 cont = 0;
	 while (frame2.rows < 2 && cont<5) {
	 cap2 >> frame2;
	 cont++;
	 }
	 }*/
	char key;
	char filename[200];
	int count = 1;
	while (true)
	{
		cap1 >> frame1;
		//cap2 >> frame2;

		imshow("cap1", frame1);
		//imshow("cap2", frame2);
		key=waitKey(60);
		if (key == 27)
			break;//按ESC键退出程序  
		if (key == 32)//按空格键进行拍照  
		{
			Mat left, right;
			Rect lr(0,0,640,480);
			Rect rr(640, 0, 640, 480);
			
			left = frame1(lr).clone();
			right = frame1(rr).clone();
			sprintf_s(filename, "left%02d.jpg", count);
			imwrite(filename, left);//图片保存到本工程目录中 
			sprintf_s(filename, "right%02d.jpg", count);
			imwrite(filename, right);//图片保存到本工程目录中  
			count++;
		}
	}
	return ;
}
int main()
{
	showvideo();
	return 0;
}