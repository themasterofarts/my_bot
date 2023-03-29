#! /usr/bin/env python3


import time  # Time library
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped # Pose with ref frame and timestamp
from rclpy.duration import Duration # Handles time for ROS 2
import rclpy # Python client library for ROS 2

from robot_navigator import BasicNavigator, NavigationResult  # Helper module

from geometry_msgs.msg import Pose
from rclpy.node import Node


class genWaipoint(Node):
    

    def __init__(self):
        super().__init__('genWaypoint')
        #self.timer_ = self.create_timer(1.0, self.pos_target)
        #self.publisher_ = self.create_publisher(Pose, 'target_pose', 1)

        self.data_ = []

        self.subscription = self.create_subscription(
            Odometry, 
            'odometry/globalv', 
            self.callback, 
            10
        )

    def callback(self, msg):
       
       Position =  msg.pose 
       print(Position)
       self.data_.append(Position)
       
    
    #def pos_target(self):
    #    self.publisher_.publish(self.data_)
    #    print(self.data_)








#def main(args=None):
 #   rclpy.init(args=args)
  #  node = genWaipoint()
   # rclpy.spin(node)
   # rclpy.shutdown()











#def callback(msg):
   # Position =  msg.pose 
    #goal_poses.append(Position)

    
#goal_poses = []


'''
Navigates a robot from an initial pose to a goal pose.
'''
def main():
  
  


  # Start the ROS 2 Python Client Library
  rclpy.init()

  #mes ajouts
  node1 = genWaipoint()

  #node1 = rclpy.create_node('genWaypoint')  
  #subscription = node1.create_subscription(Odometry, 'odometry/globalv', callback, 1)
  #print(subscription.callback)
  print(node1.data_)
 

  # Launch the ROS 2 Navigation Stack
  navigator = BasicNavigator()

  # Set the robot's initial pose if necessary
  # initial_pose = PoseStamped()
  # initial_pose.header.frame_id = 'map'
  # initial_pose.header.stamp = navigator.get_clock().now().to_msg()
  # initial_pose.pose.position.x = 0.0
  # initial_pose.pose.position.y = 0.0
  # initial_pose.pose.position.z = 0.0
  # initial_pose.pose.orientation.x = 0.0
  # initial_pose.pose.orientation.y = 0.0
  # initial_pose.pose.orientation.z = 0.0
  # initial_pose.pose.orientation.w = 1.0
  # navigator.setInitialPose(initial_pose)

  # Activate navigation, if not autostarted. This should be called after setInitialPose()
  # or this will initialize at the origin of the map and update the costmap with bogus readings.
  # If autostart, you should `waitUntilNav2Active()` instead.
  # navigator.lifecycleStartup()

  # Wait for navigation to fully activate. Use this line if autostart is set to true.
  navigator.waitUntilNav2Active()

  # If desired, you can change or load the map as well
  # navigator.changeMap('/path/to/map.yaml')

  # You may use the navigator to clear or obtain costmaps
  # navigator.clearAllCostmaps()  # also have clearLocalCostmap() and clearGlobalCostmap()
  # global_costmap = navigator.getGlobalCostmap()
  # local_costmap = navigator.getLocalCostmap()

  # Set the robot's goal pose
  goal_pose = PoseStamped()
  goal_pose.header.frame_id = 'map'
  goal_pose.header.stamp = navigator.get_clock().now().to_msg()
  goal_pose.pose.position.x = 5.0
  goal_pose.pose.position.y = -2.0
  goal_pose.pose.position.z = 0.0
  goal_pose.pose.orientation.x = 0.0
  goal_pose.pose.orientation.y = 0.0
  goal_pose.pose.orientation.z = 0.0
  goal_pose.pose.orientation.w = 1.0

  goal_poses = []

  #for g in range(len(goal_poses)):
  #   goal_poses.append(goal_pose)

  # sanity check a valid path exists
  # path = navigator.getPath(initial_pose, goal_pose)

  # Go to the goal pose
  navigator.goToPose(goal_pose)

  i = 0

  # Keep doing stuff as long as the robot is moving towards the goal
  while not navigator.isNavComplete():
    ################################################
    #
    # Implement some code here for your application!
    #
    ################################################

    # Do something with the feedback
    i = i + 1
    feedback = navigator.getFeedback()
    if feedback and i % 5 == 0:
      print('Distance remaining: ' + '{:.2f}'.format(
            feedback.distance_remaining) + ' meters.')

      # Some navigation timeout to demo cancellation
      if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
        navigator.cancelNav()

      # Some navigation request change to demo preemption
      if Duration.from_msg(feedback.navigation_time) > Duration(seconds=120.0):
        goal_pose.pose.position.x = -3.0
        navigator.goToPose(goal_pose)

  # Do something depending on the return code
  result = navigator.getResult()
  if result == NavigationResult.SUCCEEDED:
      print('Goal succeeded!')
  elif result == NavigationResult.CANCELED:
      print('Goal was canceled!')
  elif result == NavigationResult.FAILED:
      print('Goal failed!')
  else:
      print('Goal has an invalid return status!')

  # Shut down the ROS 2 Navigation Stack
  navigator.lifecycleShutdown()

  rclpy.spin(node1)
  rclpy.shutdown()

  exit(0)

if __name__ == '__main__':
  main()
