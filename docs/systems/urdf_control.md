<<<<<<< HEAD
# URDF Model Creation and Basics

This chapter provides detailed instructions on how to create a Unified Robot Description Format (URDF) model for a simple humanoid robot. URDF is an XML format used in ROS (Robot Operating System) to describe robot kinematics, dynamics, and visual properties.

## I. Understanding URDF Fundamentals

A URDF file describes a robot as a tree-like structure of `links` connected by `joints`.

*   **`<robot name="robot_name">`**: The root element for your robot description.
*   **`<link name="link_name">`**: Defines a rigid body part of the robot. Each link has:
    *   `<visual>`: Describes the visual appearance (color, mesh) of the link.
    *   `<collision>`: Describes the collision geometry of the link. This can be simpler than the visual geometry.
    *   `<inertial>`: Describes the physical properties (mass, inertia tensor) of the link, crucial for physics simulations.
*   **`<joint name="joint_name" type="joint_type">`**: Defines how two links are connected.
    *   `parent` link: The link closer to the robot's base.
    *   `child` link: The link further from the robot's base.
    *   `<origin rpy="roll pitch yaw" xyz="x y z">`: Defines the joint's position and orientation relative to the parent link's origin.
    *   `<axis xyz="x y z">`: Defines the axis of rotation for revolute/continuous joints or translation for prismatic joints.
    *   `<limit lower="val" upper="val" effort="val" velocity="val">`: Defines the joint's movement limits (for revolute/prismatic joints).
    *   `type`:
        *   `revolute`: A rotating joint with a limited range.
        *   `continuous`: A rotating joint with unlimited range.
        *   `prismatic`: A sliding joint with a limited range.
        *   `fixed`: A rigid connection (no movement).
        *   `floating`: Represents a free-flying base link (rarely used directly in a fixed-base robot).
        *   `planar`: Allows movement in a plane.

## II. Design Your Humanoid (Conceptual Sketch)

Before writing any XML, sketch out your humanoid. A simple humanoid might consist of:

1.  **Base Link:** `base_link` (often a `fixed` joint to the world or a `floating` joint if it moves freely)
2.  **Torso:** `torso_link`
3.  **Head:** `head_link` (connected to torso)
4.  **Arms (L/R):**
    *   `shoulder_link` (connected to torso)
    *   `upper_arm_link` (connected to shoulder)
    *   `lower_arm_link` (connected to upper arm)
    *   `hand_link` (connected to lower arm)
5.  **Legs (L/R):**
    *   `hip_link` (connected to torso)
    *   `upper_leg_link` (connected to hip)
    *   `lower_leg_link` (connected to upper leg)
    *   `foot_link` (connected to lower leg)

## III. Step-by-Step URDF Creation

Let's build a simple humanoid, starting from the base and working our way out.

**1. Create the Robot Root:**

```xml
<?xml version="1.0"?>
<robot name="simple_humanoid">
  <!-- Define materials here if you want to reuse colors -->
  <material name="blue">
    <color rgba="0 0 0.8 1"/>
  </material>
  <material name="red">
    <color rgba="0.8 0 0 1"/>
  </material>
  <material name="green">
    <color rgba="0 0.8 0 1"/>
  </material>
  <material name="gray">
    <color rgba="0.5 0.5 0.5 1"/>
  </material>

  <!-- Start defining links and joints -->

</robot>
```

**2. Define the Base Link (e.g., a simple torso):**

This will be your `base_link`. It's common to make the torso the base link of the kinematic chain.

```xml
  <!-- Torso Link -->
  <link name="torso_link">
    <visual>
      <geometry>
        <box size="0.2 0.3 0.5"/> <!-- Width, Depth, Height -->
      </geometry>
      <material name="blue"/>
    </visual>
    <collision>
      <geometry>
        <box size="0.2 0.3 0.5"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="10.0"/>
      <origin xyz="0 0 0.25"/> <!-- Center of mass, assuming uniform density -->
      <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0"/> <!-- Placeholder values -->
    </inertial>
  </link>
```

**3. Add the Head:**

Connect the `head_link` to the `torso_link` with a `revolute` joint to allow for nodding (pitch) or turning (yaw).

```xml
  <!-- Head Link -->
  <link name="head_link">
    <visual>
      <geometry>
        <sphere radius="0.1"/>
      </geometry>
      <material name="red"/>
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.1"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="1.0"/>
      <origin xyz="0 0 0"/>
      <inertia ixx="0.1" ixy="0.0" ixz="0.0" iyy="0.1" iyz="0.0" izz="0.1"/>
    </inertial>
  </link>

  <!-- Neck Joint (Torso to Head) -->
  <joint name="neck_joint" type="revolute">
    <parent link="torso_link"/>
    <child link="head_link"/>
    <origin xyz="0 0 0.25" rpy="0 0 0"/> <!-- Head sits on top of the torso -->
    <axis xyz="0 0 1"/> <!-- Yaw axis for turning head -->
    <limit lower="-1.57" upper="1.57" effort="10.0" velocity="0.5"/>
  </joint>
```

**4. Add Arms (Left & Right):**

Each arm will have multiple links and joints. Let's do the right arm. The left arm will be mirrored.

```xml
  <!-- Right Shoulder Link -->
  <link name="right_shoulder_link">
    <visual>
      <geometry>
        <sphere radius="0.05"/>
      </geometry>
      <material name="green"/>
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.05"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.1"/>
      <origin xyz="0 0 0"/>
      <inertia ixx="0.01" ixy="0.0" ixz="0.0" iyy="0.01" iyz="0.0" izz="0.01"/>
    </inertial>
  </link>

  <!-- Right Shoulder Joint (Torso to Shoulder) - Yaw -->
  <joint name="right_shoulder_yaw_joint" type="revolute">
    <parent link="torso_link"/>
    <child link="right_shoulder_link"/>
    <origin xyz="0 0.15 0.2" rpy="0 0 0"/> <!-- Right side, near top of torso -->
    <axis xyz="0 0 1"/> <!-- Yaw axis for shoulder rotation -->
    <limit lower="-1.57" upper="1.57" effort="10.0" velocity="0.5"/>
  </joint>

  <!-- Right Upper Arm Link -->
  <link name="right_upper_arm_link">
    <visual>
      <geometry>
        <cylinder radius="0.04" length="0.2"/>
      </geometry>
      <origin xyz="0 0 -0.1" rpy="0 0 0"/> <!-- Shift origin to connect to shoulder properly -->
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.04" length="0.2"/>
      </geometry>
      <origin xyz="0 0 -0.1" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="0.5"/>
      <origin xyz="0 0 -0.1"/>
      <inertia ixx="0.05" ixy="0.0" ixz="0.0" iyy="0.05" iyz="0.0" izz="0.05"/>
    </inertial>
  </link>

  <!-- Right Shoulder Pitch Joint (Shoulder to Upper Arm) -->
  <joint name="right_shoulder_pitch_joint" type="revolute">
    <parent link="right_shoulder_link"/>
    <child link="right_upper_arm_link"/>
    <origin xyz="0 0 0" rpy="0 0 0"/> <!-- Origin of upper arm is at the sphere's center -->
    <axis xyz="0 1 0"/> <!-- Pitch axis for raising/lowering arm -->
    <limit lower="-1.57" upper="1.57" effort="10.0" velocity="0.5"/>
  </joint>

  <!-- Right Lower Arm Link -->
  <link name="right_lower_arm_link">
    <visual>
      <geometry>
        <cylinder radius="0.03" length="0.18"/>
      </geometry>
      <origin xyz="0 0 -0.09" rpy="0 0 0"/>
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.03" length="0.18"/>
      </geometry>
      <origin xyz="0 0 -0.09" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="0.4"/>
      <origin xyz="0 0 -0.09"/>
      <inertia ixx="0.04" ixy="0.0" ixz="0.0" iyy="0.04" iyz="0.0" izz="0.04"/>
    </inertial>
  </link>

  <!-- Right Elbow Joint (Upper Arm to Lower Arm) -->
  <joint name="right_elbow_joint" type="revolute">
    <parent link="right_upper_arm_link"/>
    <child link="right_lower_arm_link"/>
    <origin xyz="0 0 -0.2" rpy="0 0 0"/> <!-- Connects at the end of the upper arm -->
    <axis xyz="0 1 0"/> <!-- Pitch axis for elbow bend -->
    <limit lower="-2.0" upper="0.0" effort="10.0" velocity="0.5"/> <!-- Only bends inwards -->
  </joint>

  <!-- Right Hand Link -->
  <link name="right_hand_link">
    <visual>
      <geometry>
        <box size="0.05 0.08 0.03"/>
      </geometry>
      <origin xyz="0 0 -0.015" rpy="0 0 0"/>
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <box size="0.05 0.08 0.03"/>
      </geometry>
      <origin xyz="0 0 -0.015" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="0.1"/>
      <origin xyz="0 0 -0.015"/>
      <inertia ixx="0.01" ixy="0.0" ixz="0.0" iyy="0.01" iyz="0.0" izz="0.01"/>
    </inertial>
  </link>

  <!-- Right Wrist Joint (Lower Arm to Hand) -->
  <joint name="right_wrist_joint" type="revolute">
    <parent link="right_lower_arm_link"/>
    <child link="right_hand_link"/>
    <origin xyz="0 0 -0.18" rpy="0 0 0"/> <!-- Connects at the end of the lower arm -->
    <axis xyz="0 1 0"/> <!-- Pitch axis for wrist bend -->
    <limit lower="-0.5" upper="0.5" effort="5.0" velocity="0.5"/>
  </joint>
```

**Repeat for Left Arm:**
You would essentially copy the arm structure, changing `right_` to `left_` and adjusting the `xyz` origin for the `left_shoulder_yaw_joint` (e.g., `xyz="0 -0.15 0.2"`).

**5. Add Legs (Left & Right):**

Similar to arms, define links and joints for legs. Let's do the right leg.

```xml
  <!-- Right Hip Link -->
  <link name="right_hip_link">
    <visual>
      <geometry>
        <sphere radius="0.06"/>
      </geometry>
      <material name="green"/>
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.06"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.2"/>
      <origin xyz="0 0 0"/>
      <inertia ixx="0.02" ixy="0.0" ixz="0.0" iyy="0.02" iyz="0.0" izz="0.02"/>
    </inertial>
  </link>

  <!-- Right Hip Yaw Joint (Torso to Hip) -->
  <joint name="right_hip_yaw_joint" type="revolute">
    <parent link="torso_link"/>
    <child link="right_hip_link"/>
    <origin xyz="0 -0.08 -0.2" rpy="0 0 0"/> <!-- Right side, lower part of torso -->
    <axis xyz="0 0 1"/> <!-- Yaw axis for hip rotation -->
    <limit lower="-0.5" upper="0.5" effort="20.0" velocity="0.5"/>
  </joint>

  <!-- Right Upper Leg Link -->
  <link name="right_upper_leg_link">
    <visual>
      <geometry>
        <cylinder radius="0.05" length="0.3"/>
      </geometry>
      <origin xyz="0 0 -0.15" rpy="0 0 0"/>
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.05" length="0.3"/>
      </geometry>
      <origin xyz="0 0 -0.15" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="1.5"/>
      <origin xyz="0 0 -0.15"/>
      <inertia ixx="0.15" ixy="0.0" ixz="0.0" iyy="0.15" iyz="0.0" izz="0.15"/>
    </inertial>
  </link>

  <!-- Right Hip Pitch Joint (Hip to Upper Leg) -->
  <joint name="right_hip_pitch_joint" type="revolute">
    <parent link="right_hip_link"/>
    <child link="right_upper_leg_link"/>
    <origin xyz="0 0 0" rpy="0 0 0"/>
    <axis xyz="0 1 0"/> <!-- Pitch axis for leg forward/backward -->
    <limit lower="-1.57" upper="1.57" effort="20.0" velocity="0.5"/>
  </joint>

  <!-- Right Lower Leg Link -->
  <link name="right_lower_leg_link">
    <visual>
      <geometry>
        <cylinder radius="0.04" length="0.25"/>
      </geometry>
      <origin xyz="0 0 -0.125" rpy="0 0 0"/>
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.04" length="0.25"/>
      </geometry>
      <origin xyz="0 0 -0.125" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="1.0"/>
      <origin xyz="0 0 -0.125"/>
      <inertia ixx="0.1" ixy="0.0" ixz="0.0" iyy="0.1" iyz="0.0" izz="0.1"/>
    </inertial>
  </link>

  <!-- Right Knee Joint (Upper Leg to Lower Leg) -->
  <joint name="right_knee_joint" type="revolute">
    <parent link="right_upper_leg_link"/>
    <child link="right_lower_leg_link"/>
    <origin xyz="0 0 -0.3" rpy="0 0 0"/> <!-- Connects at the end of the upper leg -->
    <axis xyz="0 1 0"/> <!-- Pitch axis for knee bend -->
    <limit lower="-2.0" upper="0.0" effort="20.0" velocity="0.5"/>
  </joint>

  <!-- Right Foot Link -->
  <link name="right_foot_link">
    <visual>
      <geometry>
        <box size="0.15 0.08 0.03"/>
      </geometry>
      <origin xyz="0 0 -0.015" rpy="0 0 0"/>
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <box size="0.15 0.08 0.03"/>
      </geometry>
      <origin xyz="0 0 -0.015" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="0.3"/>
      <origin xyz="0 0 -0.015"/>
      <inertia ixx="0.03" ixy="0.0" ixz="0.0" iyy="0.03" iyz="0.0" izz="0.03"/>
    </inertial>
  </link>

  <!-- Right Ankle Joint (Lower Leg to Foot) -->
  <joint name="right_ankle_joint" type="revolute">
    <parent link="right_lower_leg_link"/>
    <child link="right_foot_link"/>
    <origin xyz="0 0 -0.25" rpy="0 0 0"/> <!-- Connects at the end of the lower leg -->
    <axis xyz="0 1 0"/> <!-- Pitch axis for ankle bend -->
    <limit lower="-0.5" upper="0.5" effort="10.0" velocity="0.5"/>
  </joint>
```

**Repeat for Left Leg:**
Similar to the arm, copy the leg structure, changing `right_` to `left_` and adjusting the `xyz` origin for the `left_hip_yaw_joint` (e.g., `xyz="0 0.08 -0.2"`).

**IV. Advanced Considerations & Best Practices**

*   **Xacro (`.xacro` files):** For complex robots with many repetitive parts (like a humanoid's limbs), `xacro` is invaluable. It's an XML macro language that allows you to define reusable components, parameters, and mathematical expressions, making your URDF much more readable and maintainable. You would define macros for an arm, a leg, a joint, etc., and then instantiate them with specific parameters.
    *   Example xacro usage: `roslaunch urdf_tutorial display.launch model:=my_robot.urdf.xacro`
*   **Meshes:** For more realistic visuals and collision shapes, use `<mesh filename="package://your_package/meshes/your_mesh.stl"/>` instead of primitive geometries (box, cylinder, sphere). You'll need CAD software (Blender, SolidWorks, FreeCAD) to create these `.stl` or `.dae` files.
*   **Coordinate Frames:** Always be mindful of your coordinate frames. ROS typically uses a right-handed coordinate system, with Z-up. Joint origins are defined relative to the *parent link's frame*.
*   **Inertial Properties:** Accurate inertial properties (mass and inertia tensor) are crucial for realistic physics simulations. If using CAD software, it can often export these values for you. Otherwise, you'll need to estimate them.
*   **`robot_state_publisher` and `joint_state_publisher`:** In ROS, these nodes are used to publish the robot's state (joint positions) and broadcast the TF (Transform) tree, allowing visualization in tools like RViz.
*   **Visualization (`RViz`):** Always visualize your URDF in RViz to check for correct link placement, joint axes, and geometry.
    *   `roslaunch urdf_tutorial display.launch model:=your_robot_description_package/urdf/your_robot.urdf`
*   **Joint Limits:** Set realistic joint limits for `revolute` and `prismatic` joints. These prevent the robot from moving into physically impossible or damaging configurations.
*   **Collision vs. Visual:** Often, collision geometry can be simpler than visual geometry to reduce computational load during collision checking. For example, a complex hand mesh might have a simple box or cylinder as its collision representation.
*   **Materials:** Define materials at the top level or in a separate file to keep your `<visual>` tags cleaner.
*   **Transmission Tags:** If you plan to control your robot with ROS controllers (e.g., `ros_control`), you'll need to add `<transmission>` tags to specify how motors relate to joints.

**V. Example Directory Structure for ROS Package**

If you're using ROS, your URDF would typically reside in a package:

```
my_humanoid_description/
├── CMakeLists.txt
├── package.xml
├── launch/
│   └── display.launch  # For RViz visualization
├── urdf/
│   └── simple_humanoid.urdf  # Your URDF file
│   └── simple_humanoid.urdf.xacro # (If using xacro)
└── meshes/
    ├── torso.stl
    ├── head.stl
    └── ...
```

By following these detailed instructions, you can construct a functional URDF model for your simple humanoid robot. Remember to test and visualize frequently using RViz as you build it.

## VI. Exercises

1.  **Extend the Humanoid Model**:
    *   Add a waist joint to your `simple_humanoid.urdf` to allow the upper body to rotate.
    *   Add simple cameras or other sensors to the head link.
    *   Implement basic fingers or grippers on the hands.
2.  **Create an Xacro Macro**:
    *   Convert one of the arm or leg structures into a `.xacro` macro.
    *   Instantiate both the left and right limbs using this macro in a new `simple_humanoid.urdf.xacro` file.
    *   Process the `.xacro` file into a standard URDF and visualize it in RViz.
3.  **Explore Collision Geometries**:
    *   Modify the `collision` tags for different links in your URDF.
=======
# URDF Model Creation and Basics

This chapter provides detailed instructions on how to create a Unified Robot Description Format (URDF) model for a simple humanoid robot. URDF is an XML format used in ROS (Robot Operating System) to describe robot kinematics, dynamics, and visual properties.

## I. Understanding URDF Fundamentals

A URDF file describes a robot as a tree-like structure of `links` connected by `joints`.

*   **`<robot name="robot_name">`**: The root element for your robot description.
*   **`<link name="link_name">`**: Defines a rigid body part of the robot. Each link has:
    *   `<visual>`: Describes the visual appearance (color, mesh) of the link.
    *   `<collision>`: Describes the collision geometry of the link. This can be simpler than the visual geometry.
    *   `<inertial>`: Describes the physical properties (mass, inertia tensor) of the link, crucial for physics simulations.
*   **`<joint name="joint_name" type="joint_type">`**: Defines how two links are connected.
    *   `parent` link: The link closer to the robot's base.
    *   `child` link: The link further from the robot's base.
    *   `<origin rpy="roll pitch yaw" xyz="x y z">`: Defines the joint's position and orientation relative to the parent link's origin.
    *   `<axis xyz="x y z">`: Defines the axis of rotation for revolute/continuous joints or translation for prismatic joints.
    *   `<limit lower="val" upper="val" effort="val" velocity="val">`: Defines the joint's movement limits (for revolute/prismatic joints).
    *   `type`:
        *   `revolute`: A rotating joint with a limited range.
        *   `continuous`: A rotating joint with unlimited range.
        *   `prismatic`: A sliding joint with a limited range.
        *   `fixed`: A rigid connection (no movement).
        *   `floating`: Represents a free-flying base link (rarely used directly in a fixed-base robot).
        *   `planar`: Allows movement in a plane.

## II. Design Your Humanoid (Conceptual Sketch)

Before writing any XML, sketch out your humanoid. A simple humanoid might consist of:

1.  **Base Link:** `base_link` (often a `fixed` joint to the world or a `floating` joint if it moves freely)
2.  **Torso:** `torso_link`
3.  **Head:** `head_link` (connected to torso)
4.  **Arms (L/R):**
    *   `shoulder_link` (connected to torso)
    *   `upper_arm_link` (connected to shoulder)
    *   `lower_arm_link` (connected to upper arm)
    *   `hand_link` (connected to lower arm)
5.  **Legs (L/R):**
    *   `hip_link` (connected to torso)
    *   `upper_leg_link` (connected to hip)
    *   `lower_leg_link` (connected to upper leg)
    *   `foot_link` (connected to lower leg)

## III. Step-by-Step URDF Creation

Let's build a simple humanoid, starting from the base and working our way out.

**1. Create the Robot Root:**

```xml
<?xml version="1.0"?>
<robot name="simple_humanoid">
  <!-- Define materials here if you want to reuse colors -->
  <material name="blue">
    <color rgba="0 0 0.8 1"/>
  </material>
  <material name="red">
    <color rgba="0.8 0 0 1"/>
  </material>
  <material name="green">
    <color rgba="0 0.8 0 1"/>
  </material>
  <material name="gray">
    <color rgba="0.5 0.5 0.5 1"/>
  </material>

  <!-- Start defining links and joints -->

</robot>
```

**2. Define the Base Link (e.g., a simple torso):**

This will be your `base_link`. It's common to make the torso the base link of the kinematic chain.

```xml
  <!-- Torso Link -->
  <link name="torso_link">
    <visual>
      <geometry>
        <box size="0.2 0.3 0.5"/> <!-- Width, Depth, Height -->
      </geometry>
      <material name="blue"/>
    </visual>
    <collision>
      <geometry>
        <box size="0.2 0.3 0.5"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="10.0"/>
      <origin xyz="0 0 0.25"/> <!-- Center of mass, assuming uniform density -->
      <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0"/> <!-- Placeholder values -->
    </inertial>
  </link>
```

**3. Add the Head:**

Connect the `head_link` to the `torso_link` with a `revolute` joint to allow for nodding (pitch) or turning (yaw).

```xml
  <!-- Head Link -->
  <link name="head_link">
    <visual>
      <geometry>
        <sphere radius="0.1"/>
      </geometry>
      <material name="red"/>
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.1"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="1.0"/>
      <origin xyz="0 0 0"/>
      <inertia ixx="0.1" ixy="0.0" ixz="0.0" iyy="0.1" iyz="0.0" izz="0.1"/>
    </inertial>
  </link>

  <!-- Neck Joint (Torso to Head) -->
  <joint name="neck_joint" type="revolute">
    <parent link="torso_link"/>
    <child link="head_link"/>
    <origin xyz="0 0 0.25" rpy="0 0 0"/> <!-- Head sits on top of the torso -->
    <axis xyz="0 0 1"/> <!-- Yaw axis for turning head -->
    <limit lower="-1.57" upper="1.57" effort="10.0" velocity="0.5"/>
  </joint>
```

**4. Add Arms (Left & Right):**

Each arm will have multiple links and joints. Let's do the right arm. The left arm will be mirrored.

```xml
  <!-- Right Shoulder Link -->
  <link name="right_shoulder_link">
    <visual>
      <geometry>
        <sphere radius="0.05"/>
      </geometry>
      <material name="green"/>
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.05"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.1"/>
      <origin xyz="0 0 0"/>
      <inertia ixx="0.01" ixy="0.0" ixz="0.0" iyy="0.01" iyz="0.0" izz="0.01"/>
    </inertial>
  </link>

  <!-- Right Shoulder Joint (Torso to Shoulder) - Yaw -->
  <joint name="right_shoulder_yaw_joint" type="revolute">
    <parent link="torso_link"/>
    <child link="right_shoulder_link"/>
    <origin xyz="0 0.15 0.2" rpy="0 0 0"/> <!-- Right side, near top of torso -->
    <axis xyz="0 0 1"/> <!-- Yaw axis for shoulder rotation -->
    <limit lower="-1.57" upper="1.57" effort="10.0" velocity="0.5"/>
  </joint>

  <!-- Right Upper Arm Link -->
  <link name="right_upper_arm_link">
    <visual>
      <geometry>
        <cylinder radius="0.04" length="0.2"/>
      </geometry>
      <origin xyz="0 0 -0.1" rpy="0 0 0"/> <!-- Shift origin to connect to shoulder properly -->
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.04" length="0.2"/>
      </geometry>
      <origin xyz="0 0 -0.1" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="0.5"/>
      <origin xyz="0 0 -0.1"/>
      <inertia ixx="0.05" ixy="0.0" ixz="0.0" iyy="0.05" iyz="0.0" izz="0.05"/>
    </inertial>
  </link>

  <!-- Right Shoulder Pitch Joint (Shoulder to Upper Arm) -->
  <joint name="right_shoulder_pitch_joint" type="revolute">
    <parent link="right_shoulder_link"/>
    <child link="right_upper_arm_link"/>
    <origin xyz="0 0 0" rpy="0 0 0"/> <!-- Origin of upper arm is at the sphere's center -->
    <axis xyz="0 1 0"/> <!-- Pitch axis for raising/lowering arm -->
    <limit lower="-1.57" upper="1.57" effort="10.0" velocity="0.5"/>
  </joint>

  <!-- Right Lower Arm Link -->
  <link name="right_lower_arm_link">
    <visual>
      <geometry>
        <cylinder radius="0.03" length="0.18"/>
      </geometry>
      <origin xyz="0 0 -0.09" rpy="0 0 0"/>
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.03" length="0.18"/>
      </geometry>
      <origin xyz="0 0 -0.09" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="0.4"/>
      <origin xyz="0 0 -0.09"/>
      <inertia ixx="0.04" ixy="0.0" ixz="0.0" iyy="0.04" iyz="0.0" izz="0.04"/>
    </inertial>
  </link>

  <!-- Right Elbow Joint (Upper Arm to Lower Arm) -->
  <joint name="right_elbow_joint" type="revolute">
    <parent link="right_upper_arm_link"/>
    <child link="right_lower_arm_link"/>
    <origin xyz="0 0 -0.2" rpy="0 0 0"/> <!-- Connects at the end of the upper arm -->
    <axis xyz="0 1 0"/> <!-- Pitch axis for elbow bend -->
    <limit lower="-2.0" upper="0.0" effort="10.0" velocity="0.5"/> <!-- Only bends inwards -->
  </joint>

  <!-- Right Hand Link -->
  <link name="right_hand_link">
    <visual>
      <geometry>
        <box size="0.05 0.08 0.03"/>
      </geometry>
      <origin xyz="0 0 -0.015" rpy="0 0 0"/>
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <box size="0.05 0.08 0.03"/>
      </geometry>
      <origin xyz="0 0 -0.015" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="0.1"/>
      <origin xyz="0 0 -0.015"/>
      <inertia ixx="0.01" ixy="0.0" ixz="0.0" iyy="0.01" iyz="0.0" izz="0.01"/>
    </inertial>
  </link>

  <!-- Right Wrist Joint (Lower Arm to Hand) -->
  <joint name="right_wrist_joint" type="revolute">
    <parent link="right_lower_arm_link"/>
    <child link="right_hand_link"/>
    <origin xyz="0 0 -0.18" rpy="0 0 0"/> <!-- Connects at the end of the lower arm -->
    <axis xyz="0 1 0"/> <!-- Pitch axis for wrist bend -->
    <limit lower="-0.5" upper="0.5" effort="5.0" velocity="0.5"/>
  </joint>
```

**Repeat for Left Arm:**
You would essentially copy the arm structure, changing `right_` to `left_` and adjusting the `xyz` origin for the `left_shoulder_yaw_joint` (e.g., `xyz="0 -0.15 0.2"`).

**5. Add Legs (Left & Right):**

Similar to arms, define links and joints for legs. Let's do the right leg.

```xml
  <!-- Right Hip Link -->
  <link name="right_hip_link">
    <visual>
      <geometry>
        <sphere radius="0.06"/>
      </geometry>
      <material name="green"/>
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.06"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.2"/>
      <origin xyz="0 0 0"/>
      <inertia ixx="0.02" ixy="0.0" ixz="0.0" iyy="0.02" iyz="0.0" izz="0.02"/>
    </inertial>
  </link>

  <!-- Right Hip Yaw Joint (Torso to Hip) -->
  <joint name="right_hip_yaw_joint" type="revolute">
    <parent link="torso_link"/>
    <child link="right_hip_link"/>
    <origin xyz="0 -0.08 -0.2" rpy="0 0 0"/> <!-- Right side, lower part of torso -->
    <axis xyz="0 0 1"/> <!-- Yaw axis for hip rotation -->
    <limit lower="-0.5" upper="0.5" effort="20.0" velocity="0.5"/>
  </joint>

  <!-- Right Upper Leg Link -->
  <link name="right_upper_leg_link">
    <visual>
      <geometry>
        <cylinder radius="0.05" length="0.3"/>
      </geometry>
      <origin xyz="0 0 -0.15" rpy="0 0 0"/>
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.05" length="0.3"/>
      </geometry>
      <origin xyz="0 0 -0.15" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="1.5"/>
      <origin xyz="0 0 -0.15"/>
      <inertia ixx="0.15" ixy="0.0" ixz="0.0" iyy="0.15" iyz="0.0" izz="0.15"/>
    </inertial>
  </link>

  <!-- Right Hip Pitch Joint (Hip to Upper Leg) -->
  <joint name="right_hip_pitch_joint" type="revolute">
    <parent link="right_hip_link"/>
    <child link="right_upper_leg_link"/>
    <origin xyz="0 0 0" rpy="0 0 0"/>
    <axis xyz="0 1 0"/> <!-- Pitch axis for leg forward/backward -->
    <limit lower="-1.57" upper="1.57" effort="20.0" velocity="0.5"/>
  </joint>

  <!-- Right Lower Leg Link -->
  <link name="right_lower_leg_link">
    <visual>
      <geometry>
        <cylinder radius="0.04" length="0.25"/>
      </geometry>
      <origin xyz="0 0 -0.125" rpy="0 0 0"/>
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.04" length="0.25"/>
      </geometry>
      <origin xyz="0 0 -0.125" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="1.0"/>
      <origin xyz="0 0 -0.125"/>
      <inertia ixx="0.1" ixy="0.0" ixz="0.0" iyy="0.1" iyz="0.0" izz="0.1"/>
    </inertial>
  </link>

  <!-- Right Knee Joint (Upper Leg to Lower Leg) -->
  <joint name="right_knee_joint" type="revolute">
    <parent link="right_upper_leg_link"/>
    <child link="right_lower_leg_link"/>
    <origin xyz="0 0 -0.3" rpy="0 0 0"/> <!-- Connects at the end of the upper leg -->
    <axis xyz="0 1 0"/> <!-- Pitch axis for knee bend -->
    <limit lower="-2.0" upper="0.0" effort="20.0" velocity="0.5"/>
  </joint>

  <!-- Right Foot Link -->
  <link name="right_foot_link">
    <visual>
      <geometry>
        <box size="0.15 0.08 0.03"/>
      </geometry>
      <origin xyz="0 0 -0.015" rpy="0 0 0"/>
      <material name="gray"/>
    </visual>
    <collision>
      <geometry>
        <box size="0.15 0.08 0.03"/>
      </geometry>
      <origin xyz="0 0 -0.015" rpy="0 0 0"/>
    </collision>
    <inertial>
      <mass value="0.3"/>
      <origin xyz="0 0 -0.015"/>
      <inertia ixx="0.03" ixy="0.0" ixz="0.0" iyy="0.03" iyz="0.0" izz="0.03"/>
    </inertial>
  </link>

  <!-- Right Ankle Joint (Lower Leg to Foot) -->
  <joint name="right_ankle_joint" type="revolute">
    <parent link="right_lower_leg_link"/>
    <child link="right_foot_link"/>
    <origin xyz="0 0 -0.25" rpy="0 0 0"/> <!-- Connects at the end of the lower leg -->
    <axis xyz="0 1 0"/> <!-- Pitch axis for ankle bend -->
    <limit lower="-0.5" upper="0.5" effort="10.0" velocity="0.5"/>
  </joint>
```

**Repeat for Left Leg:**
Similar to the arm, copy the leg structure, changing `right_` to `left_` and adjusting the `xyz` origin for the `left_hip_yaw_joint` (e.g., `xyz="0 0.08 -0.2"`).

**IV. Advanced Considerations & Best Practices**

*   **Xacro (`.xacro` files):** For complex robots with many repetitive parts (like a humanoid's limbs), `xacro` is invaluable. It's an XML macro language that allows you to define reusable components, parameters, and mathematical expressions, making your URDF much more readable and maintainable. You would define macros for an arm, a leg, a joint, etc., and then instantiate them with specific parameters.
    *   Example xacro usage: `roslaunch urdf_tutorial display.launch model:=my_robot.urdf.xacro`
*   **Meshes:** For more realistic visuals and collision shapes, use `<mesh filename="package://your_package/meshes/your_mesh.stl"/>` instead of primitive geometries (box, cylinder, sphere). You'll need CAD software (Blender, SolidWorks, FreeCAD) to create these `.stl` or `.dae` files.
*   **Coordinate Frames:** Always be mindful of your coordinate frames. ROS typically uses a right-handed coordinate system, with Z-up. Joint origins are defined relative to the *parent link's frame*.
*   **Inertial Properties:** Accurate inertial properties (mass and inertia tensor) are crucial for realistic physics simulations. If using CAD software, it can often export these values for you. Otherwise, you'll need to estimate them.
*   **`robot_state_publisher` and `joint_state_publisher`:** In ROS, these nodes are used to publish the robot's state (joint positions) and broadcast the TF (Transform) tree, allowing visualization in tools like RViz.
*   **Visualization (`RViz`):** Always visualize your URDF in RViz to check for correct link placement, joint axes, and geometry.
    *   `roslaunch urdf_tutorial display.launch model:=your_robot_description_package/urdf/your_robot.urdf`
*   **Joint Limits:** Set realistic joint limits for `revolute` and `prismatic` joints. These prevent the robot from moving into physically impossible or damaging configurations.
*   **Collision vs. Visual:** Often, collision geometry can be simpler than visual geometry to reduce computational load during collision checking. For example, a complex hand mesh might have a simple box or cylinder as its collision representation.
*   **Materials:** Define materials at the top level or in a separate file to keep your `<visual>` tags cleaner.
*   **Transmission Tags:** If you plan to control your robot with ROS controllers (e.g., `ros_control`), you'll need to add `<transmission>` tags to specify how motors relate to joints.

**V. Example Directory Structure for ROS Package**

If you're using ROS, your URDF would typically reside in a package:

```
my_humanoid_description/
├── CMakeLists.txt
├── package.xml
├── launch/
│   └── display.launch  # For RViz visualization
├── urdf/
│   └── simple_humanoid.urdf  # Your URDF file
│   └── simple_humanoid.urdf.xacro # (If using xacro)
└── meshes/
    ├── torso.stl
    ├── head.stl
    └── ...
```

By following these detailed instructions, you can construct a functional URDF model for your simple humanoid robot. Remember to test and visualize frequently using RViz as you build it.

## VI. Exercises

1.  **Extend the Humanoid Model**:
    *   Add a waist joint to your `simple_humanoid.urdf` to allow the upper body to rotate.
    *   Add simple cameras or other sensors to the head link.
    *   Implement basic fingers or grippers on the hands.
2.  **Create an Xacro Macro**:
    *   Convert one of the arm or leg structures into a `.xacro` macro.
    *   Instantiate both the left and right limbs using this macro in a new `simple_humanoid.urdf.xacro` file.
    *   Process the `.xacro` file into a standard URDF and visualize it in RViz.
3.  **Explore Collision Geometries**:
    *   Modify the `collision` tags for different links in your URDF.
>>>>>>> 7e329f05dc838a13bb52fffdaed4957972c4fcd9
    *   Experiment with using simpler geometries (e.g., spheres or cylinders) for collision detection compared to the visual meshes. Observe any changes in simulation behavior (if you have a simulator running with collision checking).