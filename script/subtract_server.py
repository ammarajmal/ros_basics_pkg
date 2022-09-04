#!/usr/bin/env python
import rospy
from ros_basics_pkg.srv import Subtract, SubtractResponse


def callback_subtract(request):
    return SubtractResponse(request.b - request.a)


def subtract_server():
    rospy.init_node('subtract_server')
    rospy.Service('subtract', Subtract, callback_subtract)
    rospy.spin()

if __name__ == '__main__':
    subtract_server()
