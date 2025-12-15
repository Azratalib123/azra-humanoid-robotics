<<<<<<< HEAD
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class StateSubscriber(Node):
    def __init__(self):
        super().__init__('state_subscriber')
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Joint state subscriber started.')

    def joint_state_callback(self, msg):
        self.get_logger().info(f'Received Joint States: {msg.name} -> {msg.position}')


def main(args=None):
    rclpy.init(args=args)
    state_subscriber = StateSubscriber()
    rclpy.spin(state_subscriber)
    state_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
=======
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class StateSubscriber(Node):
    def __init__(self):
        super().__init__('state_subscriber')
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Joint state subscriber started.')

    def joint_state_callback(self, msg):
        self.get_logger().info(f'Received Joint States: {msg.name} -> {msg.position}')


def main(args=None):
    rclpy.init(args=args)
    state_subscriber = StateSubscriber()
    rclpy.spin(state_subscriber)
    state_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
>>>>>>> 7e329f05dc838a13bb52fffdaed4957972c4fcd9
