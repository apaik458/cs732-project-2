#!/usr/bin/env python3

import rospy
from python_nodes.srv import *

def send_ping():
    rospy.wait_for_service('ping')
    try:
        client = rospy.ServiceProxy('ping', ping)
        resp = client('Python client')
        print 'Count is %d' % (resp.count,)
        print 'Last caller was %s' % (resp.last,)
    except rospy.ServiceException, e:
        print "Service call failed: %s" % (e,)

if __name__ == "__main__":
    send_ping()
