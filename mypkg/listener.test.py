# SPDX-FileCopyrightText: 2025 Hikaru Nemoto
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CpuUsageSubscriber(Node):
    def __init__(self):
        super().__init__('cpu_usage_subscriber')
        self.subscription = self.create_subscription(
            String,
            'cpu_usage',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

def main():
    rclpy.init()
    node = CpuUsageSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

