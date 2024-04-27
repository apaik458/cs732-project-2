#!/usr/bin/env python3
import rospy
import cv2
import numpy as np

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import Point

class colour_detection:
    def __init__(self):
        self.bridge = CvBridge()
        
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.callback)
        # self.image_pub = rospy.Publisher("hand_point_topic", Point)

    def callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

        # Convert to HSV
        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        # define range wanted color in HSV
        lower_val = np.array([0,50,50])
        upper_val = np.array([10,255,255])

        # Threshold the HSV image - any red color will show up as white
        mask = cv2.inRange(hsv, lower_val, upper_val)

        # apply mask to image and get all non zero values
        coord = cv2.findNonZero(mask)
        coord_mean = (int(cv2.mean(coord)[0]), int(cv2.mean(coord)[1]))

        cv2.circle(cv_image, coord_mean, 5, (0,255,0), cv2.FILLED)

        # display image
        cv2.imshow("Res", cv_image)

        if cv2.waitKey(3) == ord('q'):
            rospy.signal_shutdown("Closing windows")

def main():
    cd = colour_detection()

    rospy.init_node('colour_detector', anonymous=True)

    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()