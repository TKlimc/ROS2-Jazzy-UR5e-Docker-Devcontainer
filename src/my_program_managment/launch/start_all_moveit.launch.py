from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    # Pfade zu den anderen Launch-Dateien
    control_launch_path = os.path.join(
        get_package_share_directory('my_robot_cell_control'),
        'launch',
        'start_robot.launch.py'
    )

    move_group_launch_path = os.path.join(
        get_package_share_directory('my_robot_cell_moveit_config'),
        'launch',
        'move_group.launch.py'
    )
    
    rviz_launch_path = os.path.join(
        get_package_share_directory('my_robot_cell_moveit_config'),
        'launch',
        'moveit_rviz.launch.py'
    )

    # Schritt 1: Test Launch (nach Realsense)
    control_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(control_launch_path),
        launch_arguments={
            'launch_rviz': 'false',
            'use_fake_hardware': 'true'
        }.items()
    )

    # Schritt 2: Move Group Launch
    move_group_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(move_group_launch_path)
    )

    # Schritt 3: RViz Launch
    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rviz_launch_path)
    )

    return LaunchDescription([
        control_launch,
        move_group_launch,
        rviz_launch,
    ])
