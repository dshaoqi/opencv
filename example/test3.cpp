//#include "stdafx.h"
  
#include <cv.h>  
#include <cxcore.h>  
#include <highgui.h>  
   
int main( int argc, char** argv )  
{  
  //声明IplImage指针  
  IplImage* pFrame = NULL;  
  
 //获取摄像头  
  CvCapture* pCapture = cvCreateCameraCapture(-1);  
   
  //创建窗口  
  cvNamedWindow("video", 1);  
while(1)  
  {  
      pFrame=cvQueryFrame( pCapture );  
      if(!pFrame)break;  
      cvShowImage("video",pFrame);  
      char c=cvWaitKey(33);  
      if(c==27)break;  
  }  
  cvReleaseCapture(&pCapture);  
  cvDestroyWindow("video");  
}   
