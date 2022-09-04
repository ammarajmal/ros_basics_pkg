#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ros_basics_pkg.msg import Message1


def talker():
    rospy.init_node('talker_node_py', anonymous=True)
    pub = rospy.Publisher('/my_chatter', Message1, queue_size=10)
    rate = rospy.Rate(1)
    i = 0
    while not rospy.is_shutdown():
        msg = Message1()
        msg.identity = 'Ammar'
        msg.id = 4
        msg.temp = 10.93

        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()
        i += 1
if __name__ == "__main__":
    talker()
