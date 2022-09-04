#!/usr/bin/env python
import rospy
from ros_basics_pkg.srv import Adder, AdderResponse
# from ros_basics_pkg.srv import Adder, AdderResponse


def callback_adder(request):
    return AdderResponse(request.a + request.b)


def adder_server():
    rospy.init_node('adder_server_node')
    rospy.Service('adder', Adder, callback_adder)
    rospy.spin()

if __name__ == '__main__':
    adder_server()
