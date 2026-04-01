import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Get the path to your URDF file
    urdf_file_name = 'robot.urdf'
    urdf_path = os.path.join(
        get_package_share_directory('robotics_assets'), # Assuming 'robotics_assets' is a ROS 2 package
        'module_1_ros2',
        'models',
        urdf_file_name
    )

    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),
        # Optional: Add joint_state_publisher_gui for manual joint control and testing
        # Node(
        #     package='joint_state_publisher_gui',
        #     executable='joint_state_publisher_gui',
        #     name='joint_state_publisher_gui',
        #     output='screen',
        # ),
    ])