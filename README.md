# Physical AI & Humanoid Robotics 🦾🤖

A **spec-driven, AI-authored technical book** focused on **Physical AI and Humanoid Robotics**, built using **Spec-Kit Plus**, **Claude Code**, and **Docusaurus**, and deployed via **vercel**.

This project explores how AI systems move beyond digital environments into the **physical world**, enabling humanoid robots to perceive, reason, and act using embodied intelligence.

🌐 Live Book:  
https://humanoid-robotics-book-kfn6dk8fn-ersa-ranis-projects.vercel.app/

---

## 📘 Project Overview

The future of AI lies in **Physical AI**—systems that understand physics, interact with real environments, and operate through robotic bodies.

This book bridges the gap between:
- **Digital intelligence (LLMs, planners, perception)**
- **Physical embodiment (robots, sensors, actuators)**

Students and developers learn how to design, simulate, and deploy **autonomous humanoid robots** using modern robotics and AI tooling.

---

## 🎯 Focus Areas

- Embodied Intelligence & Physical AI
- ROS 2 (Robot Operating System)
- Gazebo & Unity Digital Twins
- NVIDIA Isaac Sim & Isaac ROS
- Vision-Language-Action (VLA)
- Conversational Robotics (Whisper + LLMs)
- Sim-to-Real Robot Deployment

---

## 🧩 Book Structure

### Module 1: The Robotic Nervous System (ROS 2)
- ROS 2 nodes, topics, services, actions
- Python agents with `rclpy`
- URDF humanoid robot modeling

### Module 2: The Digital Twin (Gazebo & Unity)
- Physics simulation (gravity, collisions)
- Sensor simulation (LiDAR, depth cameras, IMUs)
- High-fidelity robot environments

### Module 3: The AI-Robot Brain (NVIDIA Isaac)
- Isaac Sim & synthetic data generation
- Isaac ROS for VSLAM and navigation
- Path planning with Nav2

### Module 4: Vision-Language-Action (VLA)
- Voice-to-Action using OpenAI Whisper
- LLM-based cognitive planning
- Multi-modal human-robot interaction

### Capstone: Autonomous Humanoid
- Natural language command input
- Path planning & navigation
- Object recognition & manipulation
- End-to-end autonomous behavior

---

## 🛠️ Tech Stack

- **Documentation:** Docusaurus + Markdown
- **Spec-Driven Authoring:** Spec-Kit Plus
- **AI Authoring:** Claude Code
- **Robotics:** ROS 2, Gazebo, Unity
- **AI & Simulation:** NVIDIA Isaac Sim, Isaac ROS
- **Edge AI:** Jetson Orin Nano / NX
- **Deployment:** GitHub Pages

---

## 🧪 Development Workflow

This project follows a **Spec-Driven Development** process:

1. `/sp.constitution` – Core principles & standards  
2. `/sp.spec` – Project scope & requirements  
3. `/sp.clarify` – Resolve ambiguities  
4. `/sp.plan` – Architecture & validation strategy  
5. `/sp.tasks` – Execution breakdown  
6. AI-assisted writing + validation  
7. Docusaurus build & deployment  

---

## 🚀 Getting Started (Local)

```bash
git clone https://github.com/ersa-rani/humanoid-robotics-book.git
cd humanoid-robotics-book
npm install
npm run start
Build for production:

bash
Copy code
npm run build
🎓 Target Audience
AI & Robotics students

Computer Science learners

Hackathon participants

Developers exploring humanoid robotics

Anyone interested in Physical AI & embodied intelligence

📜 License
This project is released for educational and research purposes.


🙌 Acknowledgements
Spec-Kit Plus (Panaversity)

gemini cli

ROS 2 Community

NVIDIA Isaac Platform

OpenAI (Whisper & LLM concepts)

✨ Author
Ersa Rani
