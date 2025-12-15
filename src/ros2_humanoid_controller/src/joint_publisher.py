
import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class JointPublisher(Node):
    def __init__(self):
        super().__init__('joint_publisher')
        self.publisher_ = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        self.timer = self.create_timer(1.0, self.publish_joint_commands) # Publish every 1 second
        self.get_logger().info('Joint command publisher started.')

        self.joint_names = [
            'neck_joint',
            'right_shoulder_yaw_joint', 'right_shoulder_pitch_joint', 'right_elbow_joint', 'right_wrist_joint',
            'left_shoulder_yaw_joint', 'left_shoulder_pitch_joint', 'left_elbow_joint', 'left_wrist_joint',
            'right_hip_yaw_joint', 'right_hip_pitch_joint', 'right_knee_joint', 'right_ankle_joint',
            'left_hip_yaw_joint', 'left_hip_pitch_joint', 'left_knee_joint', 'left_ankle_joint'
        ]
        self.current_position_idx = 0
        self.positions = [
            [0.0] * len(self.joint_names),  # All joints at 0
            [0.5 if i % 2 == 0 else -0.5 for i in range(len(self.joint_names))], # Some movement
            [-0.5 if i % 2 == 0 else 0.5 for i in range(len(self.joint_names))], # Other movement
            [0.0] * len(self.joint_names)   # Back to 0
        ]

    def publish_joint_commands(self):
        msg = JointTrajectory()
        msg.joint_names = self.joint_names

        point = JointTrajectoryPoint()
        point.positions = self.positions[self.current_position_idx]
        point.time_from_start = Duration(sec=1) # Reach position in 1 second
        msg.points.append(point)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing joint commands: {self.positions[self.current_position_idx]}')

        self.current_position_idx = (self.current_position_idx + 1) % len(self.positions)


def main(args=None):
    rclpy.init(args=args)
    joint_publisher = JointPublisher()
    rclpy.spin(joint_publisher)
    joint_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
