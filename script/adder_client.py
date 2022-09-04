#!/usr/bin/env python
import rospy
from ros_basics_pkg.srv import Adder


def adder_client(x, y):
    rospy.init_node('adder_client_node')
    rospy.wait_for_service('adder')
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            add_two_ints = rospy.ServiceProxy('adder', Adder)
            response = add_two_ints(x, y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException as e:
            print('Service call failed %s', e)

if __name__ == '__main__':
    adder_client(2, 3)
