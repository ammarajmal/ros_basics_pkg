#!/usr/bin/env python3
import rospy
from ammar_pkg.srv import adder, adderResponse

def callback_adder(request):
    return adderResponse(request.a + request.b)

def adder_server():
    rospy.init_node('adder_server_node')
    rospy.Service('adder', adder, callback_adder)
    rospy.spin()

if __name__ == '__main__':
    adder_server()