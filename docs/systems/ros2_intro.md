---
sidebar_position: 1
---

# Introduction to ROS 2

The Robot Operating System (ROS) is a flexible framework for writing robot software. It is a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robotic platforms. ROS 2 is a complete redesign of the original ROS, built to support new use cases like multi-robot systems, real-time control, and small embedded systems.

## The ROS 2 Graph

The fundamental concept in ROS 2 is the **graph**, which is the network of ROS 2 elements processing data together. The graph consists of several key components that communicate with each other in a distributed, peer-to-peer topology [1, 3].

### Core Concepts

#### 1. Nodes

A **Node** is the smallest, most fundamental unit of computation in a ROS 2 system. Think of a node as a small, single-purpose program within a larger robotic application [4, 5, 7].

-   **Responsibility**: Each node is typically responsible for one specific task, such as controlling a wheel motor, reading data from a laser sensor, or planning a path.
-   **Modularity**: This modular design allows for complex systems to be broken down into smaller, more manageable, and reusable parts.
-   **Communication**: Nodes communicate with each other by sending and receiving messages via Topics, Services, Actions, and Parameters [4, 6].

You can see all active nodes in a system by running the command `ros2 node list` in your terminal.

#### 2. Topics

**Topics** are the primary mechanism for asynchronous, publish-subscribe communication. They act as a bus over which nodes can exchange messages [9, 10].

-   **Publish/Subscribe Model**: A node can *publish* data to a topic, and any number of other nodes can *subscribe* to that topic to receive the data. This decouples the production of data from its consumption [11].
-   **Use Case**: Topics are ideal for continuous data streams, such as sensor readings (e.g., `/camera/image_raw`), robot state updates (e.g., `/odom`), or control commands (e.g., `/cmd_vel`).
-   **Message Types**: Each topic is strongly typed. A specific message type defines the structure of the data being sent over the topic, ensuring that publishers and subscribers agree on the format [10, 11].

#### 3. Services

**Services** provide a synchronous, request/response model of communication, similar to a classic client-server architecture [13, 14].

-   **Request/Response**: A client node sends a request to a server node and waits for a response. This is useful for remote procedure calls (RPCs) where an immediate answer is required [16, 12].
-   **Use Case**: Services are best for tasks that are not continuous, such as querying the state of a hardware driver, triggering a one-time action like taking a picture, or performing a specific calculation.
-   **Guaranteed Delivery**: Unlike topics, services offer a guarantee that the request was received and processed (though the server may still fail to produce a result) [13]. For long-running tasks, however, ROS 2 provides another mechanism called **Actions**.

---

*(Note: APA citations to be added in a later task.)*

## III. ROS 2 Control (ros2_control) for Humanoid Robots

`ros2_control` is a powerful framework within ROS 2 specifically designed to manage robot hardware interfaces and execute controllers. It's particularly well-suited for complex robots like humanoids due to its flexibility and modularity.

### Architecture

The core of `ros2_control` involves:

*   **Hardware Interfaces**: These are the software layers that directly communicate with your robot's physical actuators (e.g., motors, servos) and sensors (e.g., encoders, force sensors). For humanoids, this would abstract away the low-level communication protocols for dozens of joints.
*   **Controllers**: These are software components that implement control algorithms (e.g., PID controllers for joint position, velocity, or effort; impedance controllers). `ros2_control` provides a standardized way to load, start, stop, and configure these controllers.

### Interaction with ROS 2 Communication Mechanisms

`ros2_control` leverages ROS 2 topics, services, and actions to interact with higher-level planning and application logic:

*   **Topics (for Real-time Data Streaming)**:
    *   **Publishing Robot State**: Controllers within `ros2_control` frequently publish the robot's current state (e.g., `joint_states` messages containing position, velocity, and effort of each joint) to ROS 2 topics. Other nodes (e.g., visualization tools, planners) subscribe to this data.
    *   **Receiving Commands**: Higher-level nodes can publish commands (e.g., desired joint positions, velocities, or efforts) to topics that `ros2_control` controllers subscribe to. This allows for continuous, real-time control adjustments.
    *   *For Humanoids*: Critical for streaming sensor data (IMU, force-feedback) and sending high-frequency joint commands for reactive behaviors like balance control.

*   **Services (for Configuration and Management)**:
    *   **Controller Management**: Services are used for infrequent, blocking operations related to the control system. Examples include:
        *   `controller_manager/load_controller`: To load a controller into memory.
        *   `controller_manager/switch_controller`: To activate or deactivate controllers, or switch between different control modes (e.g., from position control to torque control for a set of joints).
        *   `controller_manager/list_controllers`: To query the status of all managed controllers.
    *   **Parameter Adjustments**: Services can be used to dynamically adjust parameters of running controllers without needing to restart the entire system.
    *   *For Humanoids*: Useful for changing the robot's control strategy, reconfiguring joint groups, or managing different gaits on the fly.

*   **Actions (for Long-Running, Goal-Oriented Tasks)**:
    *   **Trajectory Execution**: A common use case is executing complex joint trajectories. An action client (e.g., a motion planning node) sends a `FollowJointTrajectory` goal to an action server managed by `ros2_control`. The server then executes the trajectory, providing continuous feedback on its progress and allowing for preemption.
    *   **Whole-Body Control**: For humanoids, actions are ideal for coordinating multiple joints to achieve a complex goal like walking to a specific point, reaching for an object, or executing a specific whole-body motion sequence.
    *   *For Humanoids*: Provides a robust and feedback-rich mechanism for higher-level planners to command complex behaviors, offering greater reliability and user interaction.

## IV. What's Next?

In the subsequent sections, we will delve into practical examples of how to set up `ros2_control` for a simulated humanoid robot, including defining its hardware interfaces and writing basic controllers to achieve desired movements.

## V. Exercises

1.  **Create a Custom Joint Publisher**:
    *   Modify `src/ros2_humanoid_controller/src/joint_publisher.py` to publish commands for a different sequence of joint positions.
    *   Add a new joint to your `simple_humanoid.urdf` (e.g., an additional degree of freedom in the neck or waist) and update the `joint_publisher.py` to include commands for this new joint.
2.  **Filter Joint States**:
    *   Modify `src/ros2_humanoid_controller/src/state_subscriber.py` to only print the position of a specific joint (e.g., `neck_joint`) when it receives joint states.
    *   Add logic to detect if any joint exceeds a certain position threshold and print a warning.
3.  **Explore ROS 2 CLI Tools**:
    *   While your humanoid is running in Gazebo and the `joint_publisher` is active, use ROS 2 command-line tools:
        *   `ros2 topic list`: To see all active topics. Identify the `/joint_states` and `/joint_trajectory_controller/joint_trajectory` topics.
        *   `ros2 topic echo /joint_states`: To observe the raw joint state messages being published.
        *   `ros2 node list`: To see all active nodes.
        *   `ros2 param list`: To see any parameters being used by nodes.
4.  **Implement a Simple Service Client**:
    *   Write a new Python ROS 2 node that acts as a client to a simple service (e.g., `std_srvs/srv/Trigger`). This exercise focuses on the service communication pattern rather than direct robot control, as `ros2_control` service examples are more complex.
    *   Set up a simple ROS 2 service server (e.g., using `ros2 run cpp_srvcli service`) and have your client call it.
