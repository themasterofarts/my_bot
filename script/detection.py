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
        #self.get_logger().info( 'Obstacle detection is running...' )
        self.detect(msg.ranges)
        self.publisher_.publish(self.out)


    def detect(self, rang):

        state = ["Red","Green","Orange"]
        count = 0
        for i in range (len(rang)):
            if rang[i] < 2:
                count +=1
                if count == 10 :
                    self.out.data = state[0]
                    self.get_logger().info( 'Alarm level Red..' )
                    count = 0

            elif rang[i] >= 2 and rang[i] < 4 :
                    count += 1 
                    if count == 10 :
                        self.out.data = state[1]
                        self.get_logger().info( 'Alarm level green..' )
                        count = 0

            elif rang[i] >= 4 and rang[i] < 6 : 
                count += 1 
                if count == 10 :
                    self.out.data = state[2]
                    self.get_logger().info( 'Alarm level orange..' )
                    count = 0
           

            
### current result ###
# le niveau d'alarme est detecté comme espéré
# pour le niveau orange reste actif à cause des autres rayons, il faut delimiter et faire des releases d'alarmes
# rendre la detection robuste           il faut faire le reset des alarmes  (une fois que la variable est dans le selt.out, elle ne change jusqu'a nouvelle detection
# pour le reset, il faut ajouter un clean d'alarme)
            
        
        
        


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