
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.action import ActionClient
from control_msgs.action import FollowJointTrajectory # Example action for robot control
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class ROS2VLANode(Node):
    def __init__(self):
        super().__init__('ros2_vla_node')
        self.action_command_subscription = self.create_subscription(
            String,
            '/robot_action_commands',
            self.action_command_callback,
            10
        )
        self.action_command_subscription  # prevent unused variable warning
        self.get_logger().info('ROS 2 VLA Node started. Waiting for action commands...')

        # Create an action client for FollowJointTrajectory
        # This assumes a controller is running in Gazebo/Isaac Sim that exposes this action server.
        self._action_client = ActionClient(self, FollowJointTrajectory, '/joint_trajectory_controller/follow_joint_trajectory')

        # Dummy joint names for demonstration (should match URDF)
        self.joint_names = [
            'neck_joint',
            'right_shoulder_yaw_joint', 'right_shoulder_pitch_joint', 'right_elbow_joint', 'right_wrist_joint',
            'left_shoulder_yaw_joint', 'left_shoulder_pitch_joint', 'left_elbow_joint', 'left_wrist_joint',
            'right_hip_yaw_joint', 'right_hip_pitch_joint', 'right_knee_joint', 'right_ankle_joint',
            'left_hip_yaw_joint', 'left_hip_pitch_joint', 'left_knee_joint', 'left_ankle_joint'
        ]

    def action_command_callback(self, msg):
        command_str = msg.data
        self.get_logger().info(f'Received action command: "{command_str}"')

        # Parse the command string (e.g., "move_forward {}" or "turn_left {}")
        parts = command_str.split(' ', 1)
        action_name = parts[0]
        # args_json = parts[1] if len(parts) > 1 else "{}"

        if action_name == "move_forward":
            self.send_trajectory_goal(action_name)
        elif action_name == "turn_left":
            self.send_trajectory_goal(action_name)
        elif action_name == "stop":
            self.send_trajectory_goal(action_name) # Stop action might be a trajectory to current positions or specific stop command
        else:
            self.get_logger().warn(f"Unknown action: {action_name}")

    def send_trajectory_goal(self, action_name):
        goal_msg = FollowJointTrajectory.Goal()
        trajectory = JointTrajectory()
        trajectory.joint_names = self.joint_names
        
        point = JointTrajectoryPoint()
        point.time_from_start = Duration(sec=2) # 2 seconds to reach position

        if action_name == "move_forward":
            # Example: make hip joints move slightly forward
            point.positions = [0.0] * len(self.joint_names)
            if 'right_hip_pitch_joint' in self.joint_names:
                idx = self.joint_names.index('right_hip_pitch_joint')
                point.positions[idx] = -0.2
            if 'left_hip_pitch_joint' in self.joint_names:
                idx = self.joint_names.index('left_hip_pitch_joint')
                point.positions[idx] = -0.2
            self.get_logger().info('Sending move_forward trajectory goal.')

        elif action_name == "turn_left":
            # Example: make neck joint turn left
            point.positions = [0.0] * len(self.joint_names)
            if 'neck_joint' in self.joint_names:
                idx = self.joint_names.index('neck_joint')
                point.positions[idx] = 0.5 # Turn head left
            self.get_logger().info('Sending turn_left trajectory goal.')

        elif action_name == "stop":
            point.positions = [0.0] * len(self.joint_names) # Return to neutral position or current position
            self.get_logger().info('Sending stop trajectory goal.')

        trajectory.points.append(point)
        goal_msg.trajectory = trajectory

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Action result: {result.error_code}')


def main(args=None):
    rclpy.init(args=args)
    ros2_vla_node = ROS2VLANode()
    rclpy.spin(ros2_vla_node)
    ros2_vla_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
