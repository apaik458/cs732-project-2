#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class MovementNode():
    def __init__(self):
        # Initialise
        rospy.init_node('MovementNode', anonymous=False)

        # Tell user how to stop TurtleBot
        rospy.loginfo("To stop TurtleBot CTRL + C")

        # What function to call when you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        
        # Create a publisher which can "talk" to TurtleBot and tell it to move
        self.cmd_vel=rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
        #
        self.servo_sub = rospy.Subscriber("servo_topic", Float32, self.callback)

        # TurtleBot will stop if we don't keep telling it to move
        # self.r = rospy.Rate(10);
        # Twist is a datatype for velocity
        self.move_cmd = Twist()
    
    def callback(self, data):
        # Let's go forward at 0.2 m/s
        # self.move_cmd.linear.x = 0.2
        self.move_cmd.angular.z = -1.0 * data.data
        print("Position:", data.data)
        print("Velocity:", -1.0 * data.data)
        print("")

        # publish the velocity
        self.cmd_vel.publish(self.move_cmd)
        # wait for 0.1 seconds (10 HZ) and publish again
        # self.r.sleep()

    def shutdown(self):
        # Stop turtlebot
        rospy.loginfo("Stop TurtleBot")

        # A default Twist has linear.x of 0 and angular.z of 0.  
        # So it'll stop TurtleBot
        self.cmd_vel.publish(Twist())
        # Sleep just makes sure TurtleBot receives the stop command
        # prior to shutting
        # down the script
        rospy.sleep(1)
    
if __name__ == '__main__':
    MovementNode()
    rospy.spin()
