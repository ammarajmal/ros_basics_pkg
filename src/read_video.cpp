#include "opencv2/opencv.hpp"
#include <opencv2/aruco.hpp>
using namespace cv;
using namespace std;
int markNum(0);

Mat markerGenerator(int markNum){
    Mat markerImage;
    Ptr<aruco::Dictionary> dictionary = aruco::getPredefinedDictionary(aruco::DICT_6X6_250);
    aruco::drawMarker(dictionary, markNum, 200, markerImage, 1);
    imwrite("marker0.png", markerImage);
    return markerImage;
}
// void makerDetector(Mat inputImage){
//     //Mat inputImage;

//     vector<int> markerIds;
//     vector<vector<Point2f>> markerCorners, rejectedCandidates;
//     Ptr<aruco::DetectorParameters> parameters = aruco::DetectorParameters::create();
//     Ptr<aruco::Dictionary> dictionary = aruco::getPredefinedDictionary(aruco::DICT_6X6_250);
//     aruco::detectMarkers(inputImage, dictionary, markerCorners, markerIds, parameters, rejectedCandidates);

//     Mat outputImage = inputImage.clone();
//     aruco::drawDetectedMarkers(outputImage, markerCorners, markerIds);
//     imwrite("marker0_output.png", outputImage);
// }

void markderDetector(){
    VideoCapture inputVideo;
    inputVideo.open(0);
    Ptr<aruco::Dictionary> dictionary = aruco::getPredefinedDictionary(aruco::DICT_4X4_100);
    while (inputVideo.grab()) {
    Mat image, imageCopy;
    inputVideo.retrieve(image);
    image.copyTo(imageCopy);
    vector<int> ids;
    vector<vector<Point2f> > corners;
    aruco::detectMarkers(image, dictionary, corners, ids);
    
    // if at least one marker detected
    if (ids.size() > 0)
            aruco::drawDetectedMarkers(imageCopy, corners, ids);
    imshow("out", imageCopy);
    char key = (char) cv::waitKey(50);
    if (key == 'q')
        break;
    }
}



int main(int, char**)
{
    markderDetector();




    
    

    // VideoCapture video_capture(0); // open the default camera
    // if(!video_capture.isOpened())  // check if we succeeded
    //     return -1;

    // Mat gray_image;
    // namedWindow("edges",1);
    // while(true)
    // {
    //     Mat frame;
    //     video_capture >> frame; // get a new frame from camera
    //     cvtColor(frame, gray_image, COLOR_BGR2GRAY);
    //     //GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);
    //     //Canny(edges, edges, 0, 30, 3);
    //     imshow("gray image", gray_image);
    //     if(waitKey(30) >= 0) break;
    // }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
