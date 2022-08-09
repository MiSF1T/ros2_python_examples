import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberPublisher(Node):
    def __init__(self):
        super().__init__('listener')
        
        self.subscriber1 = self.create_subscription(
            String,
            'topic1',
            self.listener_callback1,
            10
        )

        self.subscriber2 = self.create_subscription(
            String,
            'topic2',
            self.listener_callback2,
            10
        )

    def listener_callback1(self,msg1):
        self.get_logger().info('received: %s'% msg1.data)

    def listener_callback2(self,msg2):
        self.get_logger().info('Received: %s' %msg2.data)

def main(args=None):
    rclpy.init(args=args)
    
    subscriber_node = SubscriberPublisher()
    rclpy.spin(subscriber_node)
    rclpy.shutdown()