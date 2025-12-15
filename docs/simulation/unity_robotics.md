<<<<<<< HEAD
# Unity Robotics Simulation Setup

This chapter will guide you through setting up and using Unity as a robotics simulation platform. We will cover the installation of Unity, the Unity Robotics Hub, importing URDF models, and basic interaction with ROS 2.

## I. Introduction to Unity for Robotics

Unity is a powerful 3D development platform widely known for game development, but increasingly used in robotics for its high-fidelity rendering, extensive asset store, and flexible scripting environment. The Unity Robotics Hub provides packages and tools specifically designed to integrate Unity with ROS and facilitate robotics simulation.

## II. Installing Unity and the Robotics Hub

1.  **Install Unity Hub**: Download and install Unity Hub from the official Unity website.
2.  **Install Unity Editor**: Use Unity Hub to install a recommended version of the Unity Editor (e.g., 2022.3 LTS or newer).
3.  **Create a New Unity Project**: Open Unity Hub, create a new 3D (URP or HDRP) project.
4.  **Install Unity Robotics Hub Packages**:
    *   Open your Unity project.
    *   Go to `Window > Package Manager`.
    *   Click the `+` icon -> `Add package from git URL...`
    *   Add the following packages:
        *   `com.unity.robotics.ros-tcp-connector` (for ROS 2 communication)
        *   `com.unity.robotics.urdf-importer` (for importing URDF models)
        *   `com.unity.robotics.visualizations` (for debugging and visualization)
    *   Ensure the packages are successfully imported.

## III. Importing a URDF Model into Unity

Using the `Unity.Robotics.URDFImporter` package:

1.  **Open URDF Importer**: Go to `Robotics > URDF Importer`.
2.  **Import URDF**: Click `Import URDF` and navigate to your `simple_humanoid.urdf` file (e.g., `docs/systems/assets/simple_humanoid.urdf`).
3.  **Configure Import Settings**:
    *   Set `Root Link` to the base link of your robot (e.g., `torso_link`).
    *   Ensure `Generate Mesh Colliders` is checked if you want physics interactions.
    *   Click `Import`.

Unity will generate a GameObject hierarchy representing your robot. You may need to adjust materials, colors, and scale if they don't appear correctly.

## IV. Basic ROS 2 Integration with Unity

The `Unity-ROS-TCP-Connector` package facilitates communication between Unity and ROS 2.

1.  **Add ROSConnection Script**: Create an empty GameObject in your Unity scene, rename it to `ROSConnection`, and add the `ROSConnection.cs` script component to it (`Assets > ROS TCP Connector > Scripts > ROSConnection.cs`).
2.  **Configure ROS IP**: In the `ROSConnection` component, set the `ROS IP Address` to your ROS 2 machine's IP address (e.g., `127.0.0.1` for local, or the IP of your Ubuntu machine).
3.  **Start ROS TCP Endpoint**: On your ROS 2 machine, run the ROS TCP Endpoint:
    ```bash
    ros2 run ros_tcp_endpoint default_server_endpoint --ros-args -p ROS_IP:=<your_ros_ip> -p ROS_TCP_PORT:=10000
    ```
4.  **Connect in Unity**: Run the Unity scene. If configured correctly, the `ROSConnection` status in Unity should show "Connected."

## V. Controlling the Robot in Unity via ROS 2 (Conceptual)

To control the imported URDF robot from ROS 2, you would typically:
1.  **Create Unity Scripts**: Write C# scripts that subscribe to ROS 2 topics (e.g., `/joint_commands`) and apply corresponding torques or positions to the robot's joints.
2.  **Create ROS 2 Nodes**: On the ROS 2 side, write Python or C++ nodes that publish joint commands to the Unity-subscribed topics.

## VI. What's Next?

=======
# Unity Robotics Simulation Setup

This chapter will guide you through setting up and using Unity as a robotics simulation platform. We will cover the installation of Unity, the Unity Robotics Hub, importing URDF models, and basic interaction with ROS 2.

## I. Introduction to Unity for Robotics

Unity is a powerful 3D development platform widely known for game development, but increasingly used in robotics for its high-fidelity rendering, extensive asset store, and flexible scripting environment. The Unity Robotics Hub provides packages and tools specifically designed to integrate Unity with ROS and facilitate robotics simulation.

## II. Installing Unity and the Robotics Hub

1.  **Install Unity Hub**: Download and install Unity Hub from the official Unity website.
2.  **Install Unity Editor**: Use Unity Hub to install a recommended version of the Unity Editor (e.g., 2022.3 LTS or newer).
3.  **Create a New Unity Project**: Open Unity Hub, create a new 3D (URP or HDRP) project.
4.  **Install Unity Robotics Hub Packages**:
    *   Open your Unity project.
    *   Go to `Window > Package Manager`.
    *   Click the `+` icon -> `Add package from git URL...`
    *   Add the following packages:
        *   `com.unity.robotics.ros-tcp-connector` (for ROS 2 communication)
        *   `com.unity.robotics.urdf-importer` (for importing URDF models)
        *   `com.unity.robotics.visualizations` (for debugging and visualization)
    *   Ensure the packages are successfully imported.

## III. Importing a URDF Model into Unity

Using the `Unity.Robotics.URDFImporter` package:

1.  **Open URDF Importer**: Go to `Robotics > URDF Importer`.
2.  **Import URDF**: Click `Import URDF` and navigate to your `simple_humanoid.urdf` file (e.g., `docs/systems/assets/simple_humanoid.urdf`).
3.  **Configure Import Settings**:
    *   Set `Root Link` to the base link of your robot (e.g., `torso_link`).
    *   Ensure `Generate Mesh Colliders` is checked if you want physics interactions.
    *   Click `Import`.

Unity will generate a GameObject hierarchy representing your robot. You may need to adjust materials, colors, and scale if they don't appear correctly.

## IV. Basic ROS 2 Integration with Unity

The `Unity-ROS-TCP-Connector` package facilitates communication between Unity and ROS 2.

1.  **Add ROSConnection Script**: Create an empty GameObject in your Unity scene, rename it to `ROSConnection`, and add the `ROSConnection.cs` script component to it (`Assets > ROS TCP Connector > Scripts > ROSConnection.cs`).
2.  **Configure ROS IP**: In the `ROSConnection` component, set the `ROS IP Address` to your ROS 2 machine's IP address (e.g., `127.0.0.1` for local, or the IP of your Ubuntu machine).
3.  **Start ROS TCP Endpoint**: On your ROS 2 machine, run the ROS TCP Endpoint:
    ```bash
    ros2 run ros_tcp_endpoint default_server_endpoint --ros-args -p ROS_IP:=<your_ros_ip> -p ROS_TCP_PORT:=10000
    ```
4.  **Connect in Unity**: Run the Unity scene. If configured correctly, the `ROSConnection` status in Unity should show "Connected."

## V. Controlling the Robot in Unity via ROS 2 (Conceptual)

To control the imported URDF robot from ROS 2, you would typically:
1.  **Create Unity Scripts**: Write C# scripts that subscribe to ROS 2 topics (e.g., `/joint_commands`) and apply corresponding torques or positions to the robot's joints.
2.  **Create ROS 2 Nodes**: On the ROS 2 side, write Python or C++ nodes that publish joint commands to the Unity-subscribed topics.

## VI. What's Next?

>>>>>>> 7e329f05dc838a13bb52fffdaed4957972c4fcd9
Future chapters will explore advanced topics like sensor simulation in Unity, generating synthetic datasets for AI training, and implementing sophisticated control algorithms.