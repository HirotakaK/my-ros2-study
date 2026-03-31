import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from builtin_interfaces.msg import Time


class ScanPublisher(Node):
    def __init__(self):
        super().__init__('scan_publisher')

        self.publisher_ = self.create_publisher(LaserScan, '/scan', 10)
        self.timer = self.create_timer(0.1, self.publish_scan)  # 10 Hz

        # スキャン設定
        self.angle_min = -math.pi / 2   # -90 度
        self.angle_max = math.pi / 2    #  90 度
        self.angle_increment = math.pi / 180  # 1 度ごと
        self.range_min = 0.1
        self.range_max = 10.0

        self.get_logger().info('ScanPublisher started. Publishing on /scan at 10 Hz.')

    def publish_scan(self):
        msg = LaserScan()
        now = self.get_clock().now().to_msg()

        msg.header.stamp = now
        msg.header.frame_id = 'laser_frame'

        msg.angle_min = self.angle_min
        msg.angle_max = self.angle_max
        msg.angle_increment = self.angle_increment
        msg.time_increment = 0.0
        msg.scan_time = 0.1
        msg.range_min = self.range_min
        msg.range_max = self.range_max

        # 疑似データ: 前方2m、左右に向かって遠くなる
        num_readings = int((self.angle_max - self.angle_min) / self.angle_increment) + 1
        ranges = []
        for i in range(num_readings):
            angle = self.angle_min + i * self.angle_increment
            # 正面に近いほど2m、真横に近いほど5m
            distance = 2.0 + 3.0 * abs(math.sin(angle))
            ranges.append(distance)

        msg.ranges = ranges
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = ScanPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
