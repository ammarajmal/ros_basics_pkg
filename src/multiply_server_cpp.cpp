#include "ros/ros.h"
#include "ros_basics_pkg/Multiplier.h"
bool multiply(ammar_pkg::Multiplier::Request &req, ammar_pkg::Multiplier::Response &res) {
                res.result = req.a * req.b;
                ROS_INFO("request: x=%ld, y = %ld", (long int)req.a, (long int)req.b);
                ROS_INFO("Sending back response: [%ld]", (long int)res.result);
                return true;
              }

int main(int argc, char **argv){
    ros::init(argc, argv, "multiply_server_cpp");
    ros::NodeHandle n;
    ros::ServiceServer service = n.advertiseService("multiply", multiply);
    ROS_INFO("Ready to multiply");
    ros::spin();
    return 0;
}