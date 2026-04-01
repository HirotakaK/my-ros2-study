from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_first_scan',
            executable='scan_publisher',
            name='scan_publisher',
            output='screen',
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_laser',
            arguments=[
                '--x', '0.2',
                '--y', '0',
                '--z', '0.1',
                '--frame-id', 'base_link',
                '--child-frame-id', 'laser_frame',
            ],
        ),
        Node(
            package='foxglove_bridge',
            executable='foxglove_bridge',
            name='foxglove_bridge',
            parameters=[{'port': 8765}],
            output='screen',
        ),
    ])
