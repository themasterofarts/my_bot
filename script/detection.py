#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy, QoSDurabilityPolicy


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        # Définition des politiques QoS
        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
                                          history=rclpy.qos.HistoryPolicy.KEEP_LAST,
                                          depth=1)


        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
             qos_profile=qos_policy)
        self.subscription  # prevent unused variable warning
## publisher 
        self.publisher_ = self.create_publisher(String, 'Alarm', 10)
        #self.timer_ = self.create_timer(1.0, self.publish_alarm)

        self.out = String()

    def listener_callback(self, msg):
        self.get_logger().info( "msg.scan_time" )
        self.detect(msg.ranges)
       # msg_1 = String()
       # msg_1.data = "red"
        self.publisher_.publish(self.out)


    def detect(self, rang):
        for i in range(len(rang)):
            if(rang[i]>2):
                self.out.data = "red"

        


    # def publish_alarm(self):
    #      msg_1 = String()
    #      msg_1.data = "red"
    #      self.publisher_.publish(msg_1)
        
        
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()