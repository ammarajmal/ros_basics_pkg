#!/usr/bin/env python3
import rospy
from ammar_pkg.srv import subtract, subtractResponse

def subtract_client(x, y):
    rospy.init_node('subtract_client_node')
    rospy.wait_for_service('subtract')
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            sub_two = rospy.ServiceProxy('subtract', subtract)
            response = sub_two(x, y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException as e:
            print('Service call failed %', e)

if __name__ == '__main__':
    subtract_client(2, 3)
    
