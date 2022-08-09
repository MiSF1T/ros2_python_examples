import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

#Subscriber node with 2subs and a publisher
class SubscriberPublisher(Node):
    def __init__(self):
        super().__init__('listener')
        msg1_val = msg2_val = 0

        self.subscriber1 = self.create_subscription(
            ##String,
            Int32,
            'topic1',
            self.listener_callback1,
            10
        )

        self.subscriber2 = self.create_subscription(
            ##String,
            Int32,
            'topic2',
            self.listener_callback2,
            10
        )

        self.publisher = self.create_publisher(
            String,
            'addition',
            10
        )

        timer_period = 0.5 ##Delay of 0.5s
        self.timer = self.create_timer(
            timer_period, self.timer_callback
        )

    def listener_callback1(self,msg1):
        self.get_logger().info('Received frm topic1: %s'% msg1.data)
        self.msg1_val = msg1.data


    def listener_callback2(self,msg2):
        self.get_logger().info('Received frm topic2: %s' %msg2.data)
        self.msg2_val = msg2.data

    def timer_callback(self):
        msg = String()
        msg.data = 'Total: %s' %(self.msg1_val + self.msg2_val)
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    
    subscriber_node = SubscriberPublisher()
    rclpy.spin(subscriber_node)
    rclpy.shutdown()