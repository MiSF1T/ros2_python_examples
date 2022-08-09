#!usr/bin/env
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)

    pubNode = rclpy.create_node('subscriber_node')

    pub1 = pubNode.create_subscription('topic1',10)

    