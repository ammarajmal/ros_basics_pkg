#!/usr/bin/env python
import rospy
from ros_basics_pkg.srv import subtract, subtractResponse


def callback_subtract(request):
    return subtractResponse(request.b - request.a)


def subtract_server():
    rospy.init_node('subtract_server')
    rospy.Service('subtract', subtract, callback_subtract)
    rospy.spin()

if __name__ == '__main__':
    subtract_server()
