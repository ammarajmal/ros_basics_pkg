#!/usr/bin/env python
import rospy
from ros_basics_pkg.srv import Multiplier


def multiplier_client(x, y):
    rospy.init_node('multiplier_client_node')
    rospy.wait_for_service('multiplier')
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            multiply_two_ints = rospy.ServiceProxy('multiplier', Multiplier)
            response = multiply_two_ints(x, y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException as e:
            print('Service call failed %s', e)

if __name__ == '__main__':
    multiplier_client(2, 3)
