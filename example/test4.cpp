#include <opencv2/highgui/highgui.hpp>  
#include <opencv2/imgproc/imgproc.hpp>  
#include <opencv2/core/core.hpp>  
#include <iostream>
using namespace cv;
using namespace std;
  
int main()  
{  
    VideoCapture cap(0);  
    if(!cap.isOpened())  
    { 
        cout<<"open failed"<<endl;
        return -1;  
    }  
    else cout<<"success";
    Mat frame;  
    Mat edges;  
  
    bool stop = false;  
    while(!stop)  
    {  
        cap>>frame;  
        cvtColor(frame, edges, CV_BGR2GRAY);  
        GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);  
        Canny(edges, edges, 0, 30, 3);  	
        imshow("当前视频",edges);  
        if(cvWaitKey(30) ==27)  
            stop = true;  
    }  
    return 0;  
}  
