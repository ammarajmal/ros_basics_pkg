#!/usr/bin/env python3
import rospy
from ammar_pkg.srv import subtract, subtractResponse

def callback_subtract(request):
    return subtractResponse(request.b - request.a)

def subtract_server():
    rospy.init_node('subtract_server')
    rospy.Service('subtract', subtract, callback_subtract)
    rospy.spin()

if __name__ == '__main__':
    subtract_server()