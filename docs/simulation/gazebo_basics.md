
# Gazebo Simulation Setup

This chapter will guide you through setting up and using Gazebo, a powerful 3D robot simulator, for simulating humanoid robots. We will cover how to launch Gazebo, import URDF models, and interact with the simulated environment.

## I. Introduction to Gazebo

Gazebo is an open-source 3D robotics simulator that accurately simulates populations of robots, sensors, and objects in a 3D environment. It offers robust physics engines, high-quality graphics, and convenient programmatic interfaces.

## II. Installing Gazebo

Gazebo is often installed as part of a ROS 2 distribution. Ensure you have a full ROS 2 installation (e.g., Humble or Iron) as recommended in our research decisions.

For Ubuntu 22.04 (ROS 2 Humble):

```bash
sudo apt update
sudo apt install ros-humble-gazebo-ros-pkgs
```

This package includes the necessary bridges to connect Gazebo with ROS 2.

## III. Launching Gazebo

You can launch an empty Gazebo world from your terminal:

```bash
gazebo
```

Or, if installed with ROS 2:

```bash
ros2 launch gazebo_ros gazebo.launch.py
```

This will open the Gazebo GUI with an empty world.

## IV. Spawning a URDF Model in Gazebo

To spawn your `simple_humanoid.urdf` model into Gazebo, you typically use the `spawn_entity.py` script provided by `gazebo_ros`.

First, ensure your URDF model is accessible. In a ROS 2 workspace, you would usually place your URDF inside a ROS 2 package's `urdf/` directory, and the `gazebo_ros` package would automatically find it. For now, we will assume the URDF is accessible via its full path for demonstration.

```bash
# Example command - adjust paths and package names as needed
ros2 run gazebo_ros spawn_entity.py -entity simple_humanoid -file /path/to/your/simple_humanoid.urdf -x 0 -y 0 -z 1
```

Replace `/path/to/your/simple_humanoid.urdf` with the actual path to your URDF file (e.g., `docs/systems/assets/simple_humanoid.urdf`). The `-x -y -z` arguments specify the initial spawn position in meters.

## V. Basic Interaction with the Simulated Robot

Once your robot is spawned, you can:
- **Move the camera**: Use mouse controls to pan, rotate, and zoom in the Gazebo GUI.
- **Inspect joints**: Select the robot model in the GUI and inspect its joint properties.
- **Apply forces**: In the GUI, you can manually apply forces or torques to links (for testing purposes).

## VI. What's Next?

In the next sections, we will delve deeper into controlling your robot with ROS 2 messages, reading sensor data from Gazebo, and creating more complex simulation environments. We will also explore how to build dedicated ROS 2 launch files to automate the process of launching Gazebo and spawning your robot.

## VII. Exercises

1.  **Launch with Custom World**:
    *   Create a simple Gazebo world file (e.g., `my_world.world`) with a few primitive shapes.
    *   Modify `spawn_humanoid.launch.py` to launch Gazebo with your custom world instead of the default empty world.
2.  **Spawn Multiple Robots**:
    *   Modify `spawn_humanoid.launch.py` or create a new launch file to spawn two `simple_humanoid` robots simultaneously at different positions.
3.  **Explore Gazebo Plugins**:
    *   Research basic Gazebo plugins (e.g., camera plugins, joint state publishers).
    *   Add a simple camera plugin to your `simple_humanoid.urdf` and verify that a camera topic becomes available in Gazebo.
4.  **Interactive Joint Control**:
    *   Using the Gazebo GUI, try to manually move the joints of your spawned humanoid.
