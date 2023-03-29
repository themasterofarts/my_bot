#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose

class genWaipoint(Node):

    

    def __init__(self):
        super().__init__('genWaypoint')
        #self.timer_ = self.create_timer(1.0, self.pos_target)
        #self.publisher_ = self.create_publisher(Pose, 'target_pose', 1)

        self.data_ = []
        self.position = Pose()
        

        self.subscription = self.create_subscription(
            Odometry, 
            'odometry/globalv', 
            self.callback, 
            1
        )

    def callback(self, msg):
       
       self.position =  msg.pose.pose 
       #print(self.position)
       self.data_.append(self.position)
       print(len(self.data_))
       
       
       
    
    #def pos_target(self):
        #self.publisher_.publish(self.data_)
        #print(self.data_)








def main(args=None):
    rclpy.init(args=args)
    node = genWaipoint()
   # d = []
    #for i in range(5):
    #    d.append(node.position)
        
    #print(d)      
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
