import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.publisher = self.create_publisher(
            String,
            'topic1',
            10
        )

        self.publisher = self.create_publisher(
            String,
            'topic2',
            10
        )
        
        timer_period = 0.5
        self.timer = self.create_timer(
            timer_period, self.timer_callback
        )
    
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello world!!'
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    publisher_node = PublisherNode()
    rclpy.spin(publisher_node)
    rclpy.shutdown()