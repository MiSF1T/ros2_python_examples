# ros2_python_examples
Example publisher and subscriber ROS2 nodes where:

Publisher node:
  - Publishes on two topics ('topic1', 'topic2') of same data type (Int32)
  
Subscriber node:
  - Subscribes to and acknowledges on receiving msg from the two topics
  - Publishes the sum of Int32 data received on the two subscribed topics to the topic 'addition'
