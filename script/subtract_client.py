#!/usr/bin/env python
import rospy
from ros_basics_pkg.srv import Subtract


def subtract_client(x, y):
    rospy.init_node('subtract_client_node')
    rospy.wait_for_service('subtract')
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            sub_two = rospy.ServiceProxy('subtract', Subtract)
            response = sub_two(x, y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException as e:
            print('Service call failed %', e)

if __name__ == '__main__':
    subtract_client(2, 3)
