#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class MovementLoggingNode():

    def __init__(self):
        rospy.init_node("MovementLoggingNode")
        rospy.Subscriber("/cmd_vel_mux/input/teleop",
                            Twist, 
                            self.RobotMovedCallback)
        print('I am starting')

        # rospy.spin() tells the program to not exit until you press 
        # ctrl + c.  If this wasn't there, it'd subscribe to 
        # /cmd_vel_mux/input/teleop/ then immediately exit (therefore 
        # stop "listening" to the thread).
        rospy.spin()

    def RobotMovedCallback(self, data):
        if (data.linear.x != 0.0) or (data.angular.z != 0.0):
            rospy.loginfo("Moving (linear=%f, angular=%f)",
                data.linear.x,
                data.angular.z)

if __name__ == '__main__':
    MovementLoggingNode()
