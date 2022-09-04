#!/usr/bin/env python
import rospy
from ros_basics_pkg.srv import Multiplier, MultiplierResponse


def callback_server(request):
    return MultiplierResponse(request.a * request.b)


def multiply_server():
    rospy.init_node('multiply_server')
    service_mult = rospy.Service('multiplier', Multiplier, callback_server)
    rospy.spin()
if __name__ == '__main__':
    multiply_server()
