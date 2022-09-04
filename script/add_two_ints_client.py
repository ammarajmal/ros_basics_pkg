#!/usr/bin/env python

import sys
import rospy
from ros_basics_pkg.srv import AddTwoInts


def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1
    except rospy.ROSInterruptException as e:
        print("Service call falied: %s" % e)


def usage():
    return '%s [x, y]' % sys.argv[0]

if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print('Requesting %s + %s' % (x, y))
    print('%s + %s = %s' % (x, y, add_two_ints_client(x, y)))
