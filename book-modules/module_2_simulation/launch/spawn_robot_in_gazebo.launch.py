import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    
    # Get the path to your URDF file
    urdf_file_name = 'robot.urdf'
    urdf_path = os.path.join(
        get_package_share_directory('robotics_assets'), # Assuming 'robotics_assets' is a ROS 2 package
        'module_2_simulation',
        'models',
        urdf_file_name
    )

    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        # Launch Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
            ),
            launch_arguments={'gz_args': '-r empty_world.world'}.items(), # Use the empty_world.world
        ),

        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),

        # Spawn the robot into Gazebo
        Node(
            package='ros_gz_sim',
            executable='create',
            name='spawn_robot',
            output='screen',
            arguments=[
                '-string', robot_desc,
                '-name', 'simple_humanoid',
                '-x', '0',
                '-y', '0',
                '-z', '0.5' # Spawn slightly above ground
            ]
        )
    ])