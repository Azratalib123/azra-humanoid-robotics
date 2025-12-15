<<<<<<< HEAD
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class LLMPlannerNode(Node):
    def __init__(self):
        super().__init__('llm_planner_node')
        self.subscription = self.create_subscription(
            String,
            '/speech_to_text',
            self.speech_to_text_callback,
            10
        )
        self.publisher_ = self.create_publisher(String, '/robot_action_commands', 10)
        self.get_logger().info('LLM Planner Node started. Awaiting speech commands...')

        # Placeholder for robot action primitives, similar to a function calling interface
        self.robot_functions = {
            "move_forward": {"description": "Move the robot forward by a small increment.", "parameters": {}},
            "turn_left": {"description": "Turn the robot left by a fixed angle.", "parameters": {}},
            "stop": {"description": "Stop all current robot movement.", "parameters": {}},
            # Add more complex actions as needed, e.g., with parameters
            # "move_to": {"description": "Move the robot to a specified location.", "parameters": {"location": "string"}}
        }

    def simulate_llm_response(self, prompt):
        """
        Simulates an LLM response with action mapping based on the prompt.
        In a real scenario, this would involve an API call to an LLM or local inference.
        """
        prompt_lower = prompt.lower()
        if "move forward" in prompt_lower:
            return json.dumps({"tool_calls": [{"function": {"name": "move_forward", "arguments": {}}}]})
        elif "turn left" in prompt_lower:
            return json.dumps({"tool_calls": [{"function": {"name": "turn_left", "arguments": {}}}]})
        elif "stop" in prompt_lower:
            return json.dumps({"tool_calls": [{"function": {"name": "stop", "arguments": {}}}]})
        else:
            return json.dumps({"tool_calls": []}) # No recognized action

    def speech_to_text_callback(self, msg):
        transcribed_text = msg.data
        self.get_logger().info(f'Received transcribed text: "{transcribed_text}"')

        # Construct a prompt for the LLM (simplified for this placeholder)
        llm_prompt = f"User said: '{transcribed_text}'. Based on available robot functions: {self.robot_functions}, what action should the robot take? Respond with a JSON function call."

        # Simulate LLM processing
        llm_output_json = self.simulate_llm_response(transcribed_text)
        self.get_logger().info(f'Simulated LLM output: {llm_output_json}')

        try:
            llm_response = json.loads(llm_output_json)
            if "tool_calls" in llm_response and llm_response["tool_calls"]:
                for tool_call in llm_response["tool_calls"]:
                    function_name = tool_call["function"]["name"]
                    function_args = tool_call["function"]["arguments"]
                    
                    if function_name in self.robot_functions:
                        action_msg = String()
                        action_msg.data = f"{function_name} {json.dumps(function_args)}"
                        self.publisher_.publish(action_msg)
                        self.get_logger().info(f"Published robot action: {action_msg.data}")
                    else:
                        self.get_logger().warn(f"LLM suggested unknown function: {function_name}")
            else:
                self.get_logger().info("LLM did not suggest a robot action.")

        except json.JSONDecodeError:
            self.get_logger().error(f"Failed to parse LLM output as JSON: {llm_output_json}")


def main(args=None):
    rclpy.init(args=args)
    llm_planner_node = LLMPlannerNode()
    rclpy.spin(llm_planner_node)
    llm_planner_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
=======
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class LLMPlannerNode(Node):
    def __init__(self):
        super().__init__('llm_planner_node')
        self.subscription = self.create_subscription(
            String,
            '/speech_to_text',
            self.speech_to_text_callback,
            10
        )
        self.publisher_ = self.create_publisher(String, '/robot_action_commands', 10)
        self.get_logger().info('LLM Planner Node started. Awaiting speech commands...')

        # Placeholder for robot action primitives, similar to a function calling interface
        self.robot_functions = {
            "move_forward": {"description": "Move the robot forward by a small increment.", "parameters": {}},
            "turn_left": {"description": "Turn the robot left by a fixed angle.", "parameters": {}},
            "stop": {"description": "Stop all current robot movement.", "parameters": {}},
            # Add more complex actions as needed, e.g., with parameters
            # "move_to": {"description": "Move the robot to a specified location.", "parameters": {"location": "string"}}
        }

    def simulate_llm_response(self, prompt):
        """
        Simulates an LLM response with action mapping based on the prompt.
        In a real scenario, this would involve an API call to an LLM or local inference.
        """
        prompt_lower = prompt.lower()
        if "move forward" in prompt_lower:
            return json.dumps({"tool_calls": [{"function": {"name": "move_forward", "arguments": {}}}]})
        elif "turn left" in prompt_lower:
            return json.dumps({"tool_calls": [{"function": {"name": "turn_left", "arguments": {}}}]})
        elif "stop" in prompt_lower:
            return json.dumps({"tool_calls": [{"function": {"name": "stop", "arguments": {}}}]})
        else:
            return json.dumps({"tool_calls": []}) # No recognized action

    def speech_to_text_callback(self, msg):
        transcribed_text = msg.data
        self.get_logger().info(f'Received transcribed text: "{transcribed_text}"')

        # Construct a prompt for the LLM (simplified for this placeholder)
        llm_prompt = f"User said: '{transcribed_text}'. Based on available robot functions: {self.robot_functions}, what action should the robot take? Respond with a JSON function call."

        # Simulate LLM processing
        llm_output_json = self.simulate_llm_response(transcribed_text)
        self.get_logger().info(f'Simulated LLM output: {llm_output_json}')

        try:
            llm_response = json.loads(llm_output_json)
            if "tool_calls" in llm_response and llm_response["tool_calls"]:
                for tool_call in llm_response["tool_calls"]:
                    function_name = tool_call["function"]["name"]
                    function_args = tool_call["function"]["arguments"]
                    
                    if function_name in self.robot_functions:
                        action_msg = String()
                        action_msg.data = f"{function_name} {json.dumps(function_args)}"
                        self.publisher_.publish(action_msg)
                        self.get_logger().info(f"Published robot action: {action_msg.data}")
                    else:
                        self.get_logger().warn(f"LLM suggested unknown function: {function_name}")
            else:
                self.get_logger().info("LLM did not suggest a robot action.")

        except json.JSONDecodeError:
            self.get_logger().error(f"Failed to parse LLM output as JSON: {llm_output_json}")


def main(args=None):
    rclpy.init(args=args)
    llm_planner_node = LLMPlannerNode()
    rclpy.spin(llm_planner_node)
    llm_planner_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
>>>>>>> 7e329f05dc838a13bb52fffdaed4957972c4fcd9
