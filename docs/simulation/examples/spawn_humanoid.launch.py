
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Get the path to the current package's share directory
    book_share_dir = get_package_share_directory('humanoid_robotics_book') # Assuming a package named 'humanoid_robotics_book'

    # Path to your URDF file
    # This path is relative to the share directory if in a ROS package,
    # but here we're referencing a file directly in docs/systems/assets
    # which is outside a typical ROS package structure for simplicity in this example.
    # In a real ROS setup, simple_humanoid.urdf would be inside a robot_description package.
    urdf_file_path = os.path.join(
        book_share_dir, 'docs', 'systems', 'assets', 'simple_humanoid.urdf'
    )
    # Note: For a real ROS 2 setup, you would typically place your URDF in a
    # dedicated 'robot_description' package and reference it like:
    # robot_description_path = os.path.join(
    #     get_package_share_directory('my_robot_description'),
    #     'urdf',
    #     'simple_humanoid.urdf'
    # )

    # Set the path to the Gazebo ROS package
    gazebo_ros_dir = get_package_share_directory('gazebo_ros')

    # Define the launch arguments
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    # world = LaunchConfiguration('world', default=os.path.join(gazebo_ros_dir, 'worlds', 'empty.world')) # Example custom world

    ld = LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),

        # Launch Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(gazebo_ros_dir, 'launch', 'gazebo.launch.py')
            ),
            # launch_arguments={'world': world}.items() # For custom world
        ),

        # Define the robot state publisher node
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time,
                         'robot_description': open(urdf_file_path, 'r').read()}],
        ),

        # Spawn the entity (robot) into Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            output='screen',
            arguments=['-entity', 'simple_humanoid',
                       '-topic', 'robot_description',
                       '-x', '0', '-y', '0', '-z', '1'],
        )
    ])

    return ld
