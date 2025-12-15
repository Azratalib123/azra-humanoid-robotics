
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class FullHumanoidTaskOrchestrator(Node):
    def __init__(self):
        super().__init__('full_humanoid_task_orchestrator')
        self.get_logger().info('Capstone Task Orchestrator Node started.')

        # Publishers and Subscribers for inter-module communication
        self.speech_to_text_pub = self.create_publisher(String, '/speech_to_text', 10)
        self.robot_action_commands_sub = self.create_subscription(
            String, '/robot_action_commands', self.robot_action_callback, 10
        )
        self.nav_goal_pub = self.create_publisher(String, '/navigation_goal', 10) # Placeholder for Nav2 goals
        self.manipulation_cmd_pub = self.create_publisher(String, '/manipulation_commands', 10) # Placeholder for manipulation

        # State variables
        self.current_robot_state = "idle"
        self.task_sequence = []
        self.current_step = 0

        # Simulate a high-level command
        self.create_timer(5.0, self.simulate_high_level_command)

    def simulate_high_level_command(self):
        if self.current_robot_state == "idle":
            self.get_logger().info("Simulating user voice command: 'Robot, please get me a drink from the fridge.'")
            msg = String()
            msg.data = "Robot, please get me a drink from the fridge."
            self.speech_to_text_pub.publish(msg)
            self.current_robot_state = "waiting_for_llm_plan"

    def robot_action_callback(self, msg):
        llm_action_str = msg.data
        self.get_logger().info(f"Orchestrator received LLM action: {llm_action_str}")

        if self.current_robot_state == "waiting_for_llm_plan":
            # For simplicity, parse a hardcoded plan based on the capstone task
            if "move_to" in llm_action_str and "fridge" in llm_action_str:
                self.task_sequence = [
                    {"action": "navigate_to", "target": "fridge"},
                    {"action": "open_fridge"},
                    {"action": "perceive_beverage"},
                    {"action": "grasp_beverage", "item": "coke"}, # Example specific item
                    {"action": "close_fridge"},
                    {"action": "navigate_to", "target": "user_location"},
                    {"action": "deliver_beverage"}
                ]
                self.current_robot_state = "executing_plan"
                self.current_step = 0
                self.execute_next_step()
            else:
                self.get_logger().error("LLM did not provide expected plan for 'fetch a drink'.")
                self.current_robot_state = "idle"

        elif self.current_robot_state == "executing_plan":
            # Placeholder for feedback from executed action (e.g., "navigation_completed")
            if "completed" in llm_action_str: # Assuming LLM action includes completion status for simplicity
                self.current_step += 1
                self.execute_next_step()

    def execute_next_step(self):
        if self.current_step >= len(self.task_sequence):
            self.get_logger().info("Capstone task completed successfully!")
            self.current_robot_state = "idle"
            return

        step = self.task_sequence[self.current_step]
        self.get_logger().info(f"Executing step {self.current_step + 1}: {step['action']}")

        if step["action"] == "navigate_to":
            nav_goal_msg = String()
            nav_goal_msg.data = step["target"]
            self.nav_goal_pub.publish(nav_goal_msg)
            self.get_logger().info(f"Published navigation goal: {step['target']}")
            # In a real system, would wait for navigation completion feedback

        elif step["action"] == "open_fridge":
            manip_cmd_msg = String()
            manip_cmd_msg.data = "open_fridge"
            self.manipulation_cmd_pub.publish(manip_cmd_msg)
            self.get_logger().info("Published manipulation command: open_fridge")
            # In a real system, would wait for manipulation completion feedback

        elif step["action"] == "perceive_beverage":
            self.get_logger().info("Simulating beverage perception...")
            # In a real system, would involve image processing and object detection
            # For simplicity, immediately transition to next step
            self.current_step += 1
            self.execute_next_step()

        elif step["action"] == "grasp_beverage":
            manip_cmd_msg = String()
            manip_cmd_msg.data = f"grasp_beverage {step['item']}"
            self.manipulation_cmd_pub.publish(manip_cmd_msg)
            self.get_logger().info(f"Published manipulation command: grasp {step['item']}")
            # In a real system, would wait for manipulation completion feedback
        
        elif step["action"] == "close_fridge":
            manip_cmd_msg = String()
            manip_cmd_msg.data = "close_fridge"
            self.manipulation_cmd_pub.publish(manip_cmd_msg)
            self.get_logger().info("Published manipulation command: close_fridge")

        elif step["action"] == "deliver_beverage":
            self.get_logger().info("Simulating beverage delivery...")
            # Final step, could involve navigating to person and handing over
            self.current_step += 1
            self.execute_next_step()
        
        else:
            self.get_logger().error(f"Unknown task sequence action: {step['action']}")
            self.current_robot_state = "idle"


def main(args=None):
    rclpy.init(args=args)
    orchestrator = FullHumanoidTaskOrchestrator()
    rclpy.spin(orchestrator)
    orchestrator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
