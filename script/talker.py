#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/chatter', String, queue_size=10)
    rate = rospy.Rate(1)
    i = 0
    while not rospy.is_shutdown():
        str_msg = 'hello from talker (pub) : ' + str(i)
        pub.publish(str_msg)
        i += 1
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
