#!/usr/bin/env python3

from python_nodes.srv import ping,pingResponse
import rospy

count = 0
last_caller = '<none>'

def handle_ping(req):
    print "Handling a call from " + req.requester
    global count
    global last_caller
    count += 1
    resp = pingResponse()
    resp.count = count
    resp.last = last_caller
    last_caller = req.requester
    return resp

def ping_server():
    rospy.init_node('ping_server')
    s = rospy.Service('ping', ping, handle_ping)
    print "Ready to handle pings."
    rospy.spin()

if __name__ == "__main__":
    ping_server()
