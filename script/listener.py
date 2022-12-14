#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def callback_listener(msg):
    print('reached the listener node')
    rospy.loginfo('message received at listener: ' + msg.data)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/chatter', String, callback_listener)
    rospy.spin()
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
