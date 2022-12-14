#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv){
    ros::init(argc, argv, "talker_cpp_node");
    ros::NodeHandle n;
    ros::Publisher chatter_publisher = n.advertise<std_msgs::String>("chatter", 1000);
    ros::Rate loop_rate(0.5);
    int count(0);
    while (ros::ok()){
        std_msgs::String msg;
        std::stringstream ss;
        ss << "Hello Ammar" << count;
        msg.data = ss.str();
        ROS_INFO("[Talker] I published %s", msg.data.c_str());
        chatter_publisher.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
        count++;
    }
    return 0;
}


















// #include "ros/ros.h"
// #include "std_msgs/String.h"
// #include <sstream>

// int main(int argc, char **argv){
//     ros::init(argc, argv, "talker_cpp_node");
//     ros::NodeHandle n;
//     ros::Publisher chatter_publisher = n.advertise<std_msgs::String>("chatter", 1000);
//     ros::Rate loop_rate(0.5);
//     int count(0);
//     while (ros::ok()){
//         std_msgs::String msg;
//         std::stringstream ss;
//         ss <<"Hello World"<< count;
//         // msg.data == ss.str();
//         msg.data == "hello ammar";
//         ROS_INFO("[Talker] I published %s", msg.data.c_str());
//         chatter_publisher.publish(msg);
//         ros::spinOnce();
//         loop_rate.sleep();
//         count++;
//     }
//     return 0;
// }