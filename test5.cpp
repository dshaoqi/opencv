#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
using namespace std;
using namespace cv;
void colorReduce(Mat & inputImage,Mat & outputImage,int div);
int main(int argc,char **argv))
{
	if(argc<2)
	{
		cout<<"need a image"<<endl;
		return -1;
	}
	Mat image=imread(argv[1]);
	imshow("origin pic",image);

	Mat result;
	result.create(image.rows,image.cols,image.type());

}
