#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
    
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        ## publisher
        self.publisher_ = self.create_publisher(String, 'Alarm', 10) # creer le publisher et publie sur le topic Alarm
        timer_period = 1.0  # seconds
        ##self.timer = self.create_timer(timer_period, self.timer_callback)
        ##self.i = 0
        self.timer = self.create_timer(timer_period, self.publish_alarm)
        self.out = String()

    def listener_callback(self, msg): 
        self.get_logger().info("msg.scan_time")  # permet de publier les infos sur le terminal
        self.detect(msg.ranges)
        self.publisher_.publish(self.out)
        #msg= String()
        #msg.data = 'VERT'
        #self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%s"' % msg.data)
        #self.i += 1
    
    def publish_alarm(self):   # permet de publier l'alarm
        #msg_1= String()
        #msg_1.data = "VERT"
        self.publisher_.publish(self.out)

    def detect(self, rang):
        for i in range(len(rang)):
            if(rang[i]>2):
                self.out.data = "orange"

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()     # detruit le noeud
    rclpy.shutdown()   # ferme le noeud


if __name__ == '__main__':
    main()
