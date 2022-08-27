#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from ammar_pkg.msg import Message1
def callback(msg):
    rospy.loginfo(msg)
def listener():
    rospy.init_node('listener_node_py', anonymous=True)
    rospy.Subscriber('/my_chatter', Message1, callback)
    rospy.spin()
if __name__ == "__main__":
    listener()