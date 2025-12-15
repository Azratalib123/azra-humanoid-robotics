
# Whisper and LLMs for Conversational Robotics

This chapter explores how to integrate state-of-the-art speech-to-text (STT) models like OpenAI Whisper with Large Language Models (LLMs) to create natural and intelligent conversational interfaces for humanoid robots. We will cover the pipeline from spoken command to robot action, focusing on intent understanding and action generation.

## I. Introduction to Conversational Robotics

Conversational robotics aims to enable robots to understand and respond to human commands using natural language. This involves several key stages:
1.  **Speech-to-Text (STT)**: Converting spoken audio into written text.
2.  **Natural Language Understanding (NLU)**: Interpreting the text to extract intent and relevant information.
3.  **Action Generation/Planning**: Translating understood intent into robot-executable commands.
4.  **Text-to-Speech (TTS)**: (Optional) Generating spoken responses from the robot.

## II. OpenAI Whisper for Speech-to-Text

OpenAI Whisper is a highly accurate and robust open-source STT model.

### 1. Capabilities

*   **Multilingual Transcription**: Transcribes speech in many languages.
*   **Language Identification**: Automatically detects the spoken language.
*   **Robustness**: Handles noise, accents, and different speaking styles well.
*   **Timestamping**: Provides word-level timestamps, useful for synchronization.

### 2. Integration Approaches

*   **Cloud API**: Easiest to use for prototyping, offloads computation. Requires internet.
*   **Local Models**: Runs on local hardware (CPU/GPU) for low-latency, offline operation, and data privacy. Different model sizes (`tiny`, `base`, `small`, `medium`, `large`) offer accuracy/speed trade-offs.

### 3. Robotics Considerations

*   **Audio Capture**: Quality microphones are essential.
*   **Voice Activity Detection (VAD)**: Important for real-time processing to segment speech from silence.
*   **Resource Management**: Choose an appropriate model size based on robot platform's computational resources.

## III. Large Language Models (LLMs) for NLU and Action Generation

LLMs act as the brain to translate human intent into robot actions.

### 1. Role of LLMs in Robotics

*   **Intent Understanding**: Extracting the user's goal from natural language.
*   **Parameter Extraction**: Identifying key details (e.g., object names, locations, actions) from commands.
*   **Action Sequence Generation**: Producing a series of low-level robot commands to achieve the intent.
*   **Reasoning**: For more complex tasks, LLMs can perform basic reasoning to break down goals into sub-tasks.

### 2. Prompt Engineering for Robot Control

The way you structure your input (prompt) to the LLM significantly impacts its performance.

*   **Zero-shot/Few-shot**: Providing a clear instruction and/or a few examples in the prompt.
*   **Function Calling / Tool Use**: This is crucial. Define a set of available robot functions (e.g., `move_to(location)`, `pick_up(object)`, `say(phrase)`). The LLM's task is to output calls to these functions in a structured format (e.g., JSON).

    *   **Example Function Definition**:
        ```json
        {
          "name": "move_to",
          "description": "Move the robot to a specified location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The target location (e.g., 'table', 'door', 'charging_station')."
              }
            },
            "required": ["location"]
          }
        }
        ```
    *   **LLM Output for "Robot, go to the table."**:
        ```json
        {
          "tool_calls": [
            {
              "function": {
                "name": "move_to",
                "arguments": {
                  "location": "table"
                }
              }
            }
          ]
        }
        ```

### 3. Grounding LLM Outputs

*   **Action Primitives**: The LLM's generated function calls must correspond to actual robot capabilities.
*   **State Information**: Providing the LLM with current robot state (e.g., current location, battery level) and world state (e.g., detected objects) can improve planning.
*   **Error Handling**: Implement robust parsing and validation of LLM outputs, as they can sometimes produce invalid or "hallucinated" commands.

## IV. Integrated Pipeline for Voice Commands

A typical pipeline from voice command to robot action:

1.  **Audio Input**: Human speaks to the robot.
2.  **Speech-to-Text (Whisper)**: Audio is transcribed into text.
3.  **Prompt Construction**: Transcribed text, along with available robot functions and relevant context, forms the LLM prompt.
4.  **LLM Inference**: The LLM processes the prompt and generates a structured action (e.g., function call).
5.  **Action Execution**: The robot's control system parses the LLM's output and executes the corresponding robot action (e.g., sending ROS 2 commands).
6.  **Feedback (Optional)**: Robot provides verbal (TTS) or visual feedback.

## V. What's Next?

The next sections will delve into practical implementations of this pipeline, including Python scripts for Whisper integration, prompt engineering examples, and connecting LLM outputs to ROS 2 actions.

## VI. Exercises

1.  **Integrate a Real Whisper Model (Local)**:
    *   Modify `src/vla_interface/whisper_asr.py` to use a local Whisper model (e.g., from `HuggingFace Transformers` or `openai-whisper` library).
    *   Experiment with different model sizes (`tiny`, `base`, `small`) and observe their impact on accuracy and latency.
    *   (Optional) Integrate a simple Voice Activity Detection (VAD) library to only process speech segments.
2.  **Integrate a Real LLM API**:
    *   Modify `src/vla_interface/llm_planner.py` to make actual API calls to a commercial LLM (e.g., OpenAI GPT, Google Gemini, Anthropic Claude) or a locally running open-source LLM.
    *   Experiment with prompt engineering to improve the LLM's ability to extract robot actions and parameters.
    *   Define more complex robot functions (e.g., `pick_up(object_name, location)`) and include them in the LLM prompt for function calling.
3.  **Implement a Text-to-Speech (TTS) Response**:
    *   Add a TTS capability to your `ros2_vla_node.py`.
    *   Have the robot provide verbal confirmation of received commands (e.g., "Moving forward," "Turning left") or responses to simple queries.
4.  **Error Handling for LLM Outputs**:
    *   Enhance the `llm_planner.py` to gracefully handle cases where the LLM produces invalid JSON, suggests unknown functions, or fails to generate any action.
