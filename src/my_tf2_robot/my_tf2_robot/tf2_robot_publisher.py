import math

import rclpy
from rclpy.node import Node
from rclpy.time import Time

from geometry_msgs.msg import TransformStamped
from sensor_msgs.msg import LaserScan
import tf2_ros


class Tf2RobotPublisher(Node):
    def __init__(self):
        super().__init__('tf2_robot_publisher')

        # --- Dynamic TF broadcaster: odom -> base_link ---
        self._tf_broadcaster = tf2_ros.TransformBroadcaster(self)

        # --- Static TF broadcaster: base_link -> laser_frame ---
        self._static_broadcaster = tf2_ros.StaticTransformBroadcaster(self)
        self._publish_static_tf()

        # --- LaserScan publisher ---
        self._scan_pub = self.create_publisher(LaserScan, '/scan', 10)

        # Timer at 10 Hz
        self._timer = self.create_timer(0.1, self._timer_callback)

        # Robot state
        self._angle = 0.0          # current angle along the circle [rad]
        self._radius = 1.0         # circle radius [m]
        self._angular_speed = 0.1  # [rad/s]

        self.get_logger().info('tf2_robot_publisher started.')

    # ------------------------------------------------------------------
    def _publish_static_tf(self) -> None:
        """Publish a one-time static transform: base_link -> laser_frame."""
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'base_link'
        t.child_frame_id = 'laser_frame'
        t.transform.translation.x = 0.2
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.1
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        self._static_broadcaster.sendTransform(t)

    # ------------------------------------------------------------------
    def _timer_callback(self) -> None:
        now = self.get_clock().now()

        # Advance robot angle
        self._angle += self._angular_speed * 0.1  # dt = 0.1 s

        self._publish_dynamic_tf(now)
        self._publish_laser_scan(now)

    # ------------------------------------------------------------------
    def _publish_dynamic_tf(self, stamp: Time) -> None:
        """Broadcast odom -> base_link (robot moving in a circle)."""
        x = self._radius * math.cos(self._angle)
        y = self._radius * math.sin(self._angle)

        # Robot heading = tangent to the circle = angle + pi/2
        yaw = self._angle + math.pi / 2.0
        qz = math.sin(yaw / 2.0)
        qw = math.cos(yaw / 2.0)

        t = TransformStamped()
        t.header.stamp = stamp.to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'
        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = qz
        t.transform.rotation.w = qw
        self._tf_broadcaster.sendTransform(t)

    # ------------------------------------------------------------------
    def _publish_laser_scan(self, stamp: Time) -> None:
        """Publish a simple LaserScan on /scan."""
        scan = LaserScan()
        scan.header.stamp = stamp.to_msg()
        scan.header.frame_id = 'laser_frame'

        scan.angle_min = -1.57
        scan.angle_max = 1.57
        scan.angle_increment = 0.05
        scan.time_increment = 0.0
        scan.scan_time = 0.1
        scan.range_min = 0.1
        scan.range_max = 10.0

        num_readings = int((scan.angle_max - scan.angle_min) / scan.angle_increment) + 1
        scan.ranges = [2.0] * num_readings

        self._scan_pub.publish(scan)


# ----------------------------------------------------------------------
def main(args=None):
    rclpy.init(args=args)
    node = Tf2RobotPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
