#!/usr/bin/env python3
from ammar_pkg.srv import AddTwoInts, AddTwoIntsResponse
import rospy
# i have changed from ubuntu 20.04
def handle_add_two_ints(req):
    print('Returning [%s + %s = %s]'%(req.a, req.b , (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server', anonymous=False)
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print('ready to add two ints.')
    rospy.spin()
if __name__ == '__main__':
    try:
        add_two_ints_server()
    except rospy.ROSInterruptException:
        pass