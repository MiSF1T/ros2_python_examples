#!usr/bin/env
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)

    pubNode = rclpy.create_node('publisher_node')

    pub1 = pubNode.create_publisher(String, 'topic1', 10)
    pub2 = pubNode.create_publisher(String, 'topic2', 10)
    