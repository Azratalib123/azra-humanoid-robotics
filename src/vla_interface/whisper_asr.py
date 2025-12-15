import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

# Placeholder for Whisper library/API integration
# In a real scenario, you would integrate OpenAI Whisper API or a local model here.
def transcribe_audio_placeholder(audio_data):
    """
    Simulates Whisper transcribing audio data.
    """
    if "move forward" in audio_data.lower():
        return "move forward"
    elif "turn left" in audio_data.lower():
        return "turn left"
    elif "stop" in audio_data.lower():
        return "stop"
    else:
        return "unknown command"

class WhisperASRNode(Node):
    def __init__(self):
        super().__init__('whisper_asr_node')
        self.publisher_ = self.create_publisher(String, '/speech_to_text', 10)
        self.timer = self.create_timer(5.0, self.simulate_audio_input) # Simulate audio every 5 seconds
        self.get_logger().info('Whisper ASR Node started. Simulating audio input...')

        self.simulated_commands = [
            "Robot, move forward.",
            "Can you please turn left?",
            "Stop, robot.",
            "What is the weather like today?" # Example of an unrecognized command
        ]
        self.command_index = 0

    def simulate_audio_input(self):
        """
        Simulates receiving audio input (e.g., from a microphone).
        In a real system, this would come from an audio capture ROS 2 node.
        """
        simulated_audio = self.simulated_commands[self.command_index]
        self.get_logger().info(f'Simulating audio input: "{simulated_audio}"')

        # Transcribe the simulated audio
        transcribed_text = transcribe_audio_placeholder(simulated_audio)

        # Publish the transcribed text
        msg = String()
        msg.data = transcribed_text
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published transcribed text: "{transcribed_text}"')

        self.command_index = (self.command_index + 1) % len(self.simulated_commands)


def main(args=None):
    rclpy.init(args=args)
    whisper_asr_node = WhisperASRNode()
    rclpy.spin(whisper_asr_node)
    whisper_asr_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
