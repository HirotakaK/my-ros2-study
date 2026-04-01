from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    tf2_robot_node = Node(
        package='my_tf2_robot',
        executable='tf2_robot_publisher',
        name='tf2_robot_publisher',
        output='screen',
    )

    foxglove_bridge_node = Node(
        package='foxglove_bridge',
        executable='foxglove_bridge',
        name='foxglove_bridge',
        output='screen',
        parameters=[
            {'port': 8765},
        ],
    )

    return LaunchDescription([
        tf2_robot_node,
        foxglove_bridge_node,
    ])
