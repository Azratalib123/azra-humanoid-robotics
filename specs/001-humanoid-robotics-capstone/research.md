# Research Decisions for Building Intelligent Humanoid Robotics

## ROS 2 Version: Humble vs Iron

- **Decision**: Recommend ROS 2 Humble as the primary version for the book due to its Long-Term Support (LTS) status and broader community adoption. ROS 2 Iron is acknowledged as a newer alternative, but readers are advised to verify compatibility and stability with other tools.
- **Rationale**: LTS releases like Humble provide a stable foundation for learning and development, ensuring long-term code viability and access to a mature ecosystem. Iron may offer newer features but has a shorter support cycle.
- **Alternatives Considered**: Using ROS 2 Iron exclusively (rejected), using both with separate instructions (rejected).  
- **Further Clarification Needed**: Specific compatibility with NVIDIA Isaac Sim should be confirmed from official documentation.

## Simulation Environment: Gazebo, Unity, or Both

- **Decision**: Prioritize NVIDIA Isaac Sim as the primary simulation environment due to superior physics (PhysX 5), photorealistic rendering (Omniverse), deep ROS 2 integration, and built-in synthetic data generation. Unity Robotics Simulation is secondary for visually rich environments, Gazebo for basic open-source ROS 2 integration.
- **Rationale**: Humanoid robotics requires accurate physics for locomotion and interactions. Isaac Sim provides high fidelity simulation and synthetic data for AI perception. Unity is strong graphically, Gazebo is mature but lower fidelity.
- **Alternatives Considered**: Exclusively Gazebo (rejected), exclusively Unity (rejected), all three (rejected for complexity).  
- **Further Clarification Needed**: Optimal hardware requirements for Isaac Sim and cross-platform asset creation.

## Isaac Sim vs Isaac ROS Features

- **Decision**: Isaac Sim for high-fidelity simulation and synthetic data. Isaac ROS for GPU-accelerated ROS 2 packages (VSLAM, object detection) on physical/simulated hardware.  
- **Rationale**: Isaac Sim provides virtual environment and physics for humanoid behaviors. Isaac ROS enables efficient edge execution. Both are needed for modern robotics development.  
- **Alternatives Considered**: Isaac Sim only (rejected), Isaac ROS only (rejected).  
- **Further Clarification Needed**: How Isaac ROS integrates with Isaac Sim sensor data; Jetson hardware configurations.

## GPU Assumptions: Local RTX vs Cloud

- **Decision**: Hybrid approach: local NVIDIA RTX GPU (3080/4080+) for daily dev and smaller simulations; cloud GPUs (AWS, Azure, GCP) for large-scale simulations and AI training.  
- **Rationale**: Local GPUs are low-latency and cost-effective; cloud GPUs offer scalability for resource-intensive tasks.  
- **Alternatives Considered**: Exclusively local (rejected), exclusively cloud (rejected).  
- **Further Clarification Needed**: Cloud provider recommendations, cost, and data transfer strategies.

## Robot Integration Level: Proxy or Mini-Humanoids

- **Decision**: Focus on **Proxy Humanoids in Simulation** (Isaac Sim) for core humanoid concepts. Include **Mini-Humanoids** (Robotis OP3, Nao) for real-world hardware exposure. Quadrupeds mentioned as complementary.  
- **Rationale**: Simulation-first maximizes accessibility, mini-humanoids provide physical insight. Focus remains on humanoid robots.  
- **Alternatives Considered**: Simulation only (rejected), physical only (rejected), quadrupeds prioritized (rejected).  
- **Further Clarification Needed**: Open-source URDF/USD models for proxy humanoids; differences between simulation and real-world behavior.

## VLA Depth: Intermediate LLM-Assisted

- **Decision**: Focus on **Intermediate (LLM-Assisted Action Selection/Parameterization)** for Vision-Language-Action (VLA). Basic voice-to-action introduced conceptually, full NLP planning discussed conceptually.  
- **Rationale**: Balanced scope for capstone project. Allows students to learn prompt engineering, intent recognition, and language-perception integration.  
- **Alternatives Considered**: Basic only (rejected), full NLP (rejected).  
- **Further Clarification Needed**: LLM API/model selection; visual grounding strategies; error handling.

## End-to-End Task Examples

- **Decision**: Capstone task: **"Fetch a beverage from a simulated fridge"**, integrating perception, navigation, and manipulation.  
- **Rationale**: Demonstrates full autonomous pipeline, visually engaging, achievable within book scope.  
- **Alternatives Considered**: Industrial inspection, search and rescue (rejected).  
- **Further Clarification Needed**: Sub-task breakdown, object recognition strategies, simulated fridge design.

## Conversational Robotics Scope

- **Decision**: Use **Whisper for speech-to-text** and **LLM for action selection/parameter extraction**. Introduce simplified multimodal interaction (vision + language) for context awareness. Full open-ended dialogue discussed as advanced topic.  
- **Rationale**: Practical educational path for human-robot interfaces, balancing complexity.  
- **Alternatives Considered**: Text-only commands (rejected), full open-ended dialogue (rejected), ignore multimodal (rejected).  
- **Further Clarification Needed**: Whisper + LLM integration strategies; visual grounding; task-specific dialogue flows.

## Isaac Sim for VSLAM & Nav2

- **Decision**: Isaac Sim for developing and testing VSLAM and Nav2 integration for humanoids.  
- **Rationale**: Provides realistic sensor data and environment for validating algorithms. Custom motion translation layer needed to map Nav2 outputs to humanoid gaits.  
- **Alternatives Considered**: Real hardware only (rejected), other simulators (rejected).  
- **Further Clarification Needed**: VSLAM packages; motion translation design; performance implications.

## Whisper for Speech-to-Text

- **Decision**: OpenAI Whisper for robust transcription; API-based and local deployment on NVIDIA Jetson.  
- **Rationale**: Multilingual, noise-robust, accurate, low-latency offline option.  
- **Alternatives Considered**: Other ASR models (rejected).  
- **Further Clarification Needed**: Whisper model choice; voice activity detection; ROS 2 integration.

## LLM Integration

- **Decision**: LLMs for high-level planning/action generation from natural language. Both commercial APIs and open-source models explored. Prompt engineering ensures reliable robot action generation.  
- **Rationale**: Bridges semantic gap between human instructions and robot commands. Structured outputs (function calls) ensure reliability.  
- **Alternatives Considered**: Rule-based NLP (rejected), keyword spotting (rejected).  
