#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

class test_vision:
    def __init__(self):
        rospy.init_node('test_vision', anonymous=True)
        self.image_sub = rospy.Subscriber("servo_topic", Float32, self.callback)

    def callback(self, data):
        print(data.data)

def main():
    test_vision()
    rospy.spin()

if __name__ == '__main__':
    main()