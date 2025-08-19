from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    package_name = 'my_robot_vacuum'

    rviz_arg = DeclareLaunchArgument(
        name='rviz',
        default_value='False',
        description='Open RViz2 along with the robot driver'
    )

    # Determine path to rviz config file
    rviz_config_file = os.path.join(
        get_package_share_directory(package_name),
        'rviz',
        'robot_view.rviz'
    )

    rviz_node = Node(
        package='rviz2',
        namespace='',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        condition=IfCondition(LaunchConfiguration("rviz"))
    )


    return LaunchDescription([
        rviz_arg,
        Node(
            package=package_name,
            executable='ultrasonic_sensor',
            name='ultrasonic_sensor_node',
            namespace='',  
            output='screen' # Вывод в терминал

        ),
        Node(
            package=package_name,
            executable='battery_sensor',
            name='battery_sensor_node',
            namespace='',
            output='screen'
        ),
        rviz_node
    ])
