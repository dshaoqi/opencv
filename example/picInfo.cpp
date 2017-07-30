#include <highgui.h>
#include <cv.h>
#include <iostream>

using namespace std;
using namespace cv;
int main(int argc,char **argv)
{
	if(argc<2) 
	{
		cout<<"input an image"<<endl;
		return -1;
	}
	IplImage* image=cvLoadImage(argv[1],1);
	
	cout<<"size:"<<image->nSize<<endl;
	cout<<"ID:"<<image->ID<<endl;
	cout<<"channel nums:"<<image->nChannels<<endl;
	cout<<"depth:"<<image->depth<<endl;
	cout<<"dataOrder:"<<image->dataOrder<<endl;
	cout<<"origin:"<<image->origin<<endl;
	cout<<"width:"<<image->width<<endl;
	cout<<"height:"<<image->height<<endl;
	cout<<"ROI:"<<image->roi<<endl;
	cout<<"widthStep:"<<image->widthStep<<endl;
	cout<<"imageSize:"<<image->imageSize<<endl;
	cvShowImage("pic",image);

	cvWaitKey(0);

	cvReleaseImage(&image);
	
	return 0;
}
