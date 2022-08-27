#include "ros/ros.h"
#include "ammar_pkg/Multiplier.h"
#include <cstdlib>
int main(int argc, char **argv){
    ros::init(argc, argv, "multiply_client_cpp");
    if (argc !=3) {
        ROS_INFO("usage: multiply_client X Y");
        return 1;
    }
    ros::NodeHandle n;
    ros::ServiceClient client = n.serviceClient<ammar_pkg::Multiplier>("multiply");
    ammar_pkg::Multiplier srv;
    srv.request.a = atoll(argv[1]);
    srv.request.b = atoll(argv[2]);
    if (client.call(srv))
        ROS_INFO("Multiply: %ld", (long int)srv.response.result);
    else {
        ROS_INFO("Falied to call service Multiply_cpp");
        return 1;
    }
    return 0;
}