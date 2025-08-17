import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class BatterySensorNode(Node):
    def __init__(self):
        super().__init__('battery_sensor_node')
        self.publisher_ = self.create_publisher(Float32, 'battery_level', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        battery_level = float(random.randint(0, 100)) #Симуляция
        msg = Float32()
        msg.data = battery_level
        self.publisher_.publish(msg)
        self.get_logger().info(f'Battery Level: {battery_level}')

def main(args=None):
    rclpy.init(args=args)
    battery_sensor_node = BatterySensorNode()
    rclpy.spin(battery_sensor_node)
    battery_sensor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
