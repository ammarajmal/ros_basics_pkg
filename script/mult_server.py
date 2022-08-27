#!/usr/bin/env python3
import rospy
from ammar_pkg.srv import multiplier, multiplierResponse

def callback_server(request):
    return multiplierResponse(request.a * request.b)

def multiply_server():
    rospy.init_node('multiply_server')
    service_mult = rospy.Service('multiplier', multiplier, callback_server)
    rospy.spin()
    
if __name__ == '__main__':
    multiply_server()
