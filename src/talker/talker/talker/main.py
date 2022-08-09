from ast import In
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

##Node with 2 publishers...
class PublisherNode(Node):
    count = 0

    def __init__(self):
        super().__init__('talker')
        self.publisher1 = self.create_publisher(
            #String,
            Int32,
            'topic1',
            10
        )

        self.publisher2 = self.create_publisher(
            #String,
            Int32,
            'topic2',
            10
        )
        
        timer_period = 0.5 ##Delay of 0.5s
        self.timer = self.create_timer(
            timer_period, self.timer_callback
        )

    def timer_callback(self):    
        #msg1 = String()
        #msg2 = String()
        #msg1.data = 'Hello Earth, for the: %sth time!!' %self.count
        #msg2.data = 'Hello Mars, for the %sth time!!' %(self.count+10)
        msg1 = Int32()
        msg2 = Int32()
        msg1.data = self.count
        msg2.data = self.count+5

        self.count+=10
        
        self.publisher1.publish(msg1)
        self.publisher2.publish(msg2)

def main(args=None):
    rclpy.init(args=args)
    publisher_node = PublisherNode()
    rclpy.spin(publisher_node)
    rclpy.shutdown()