fiport rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random #Для симуляции

class UltrasonicSensorNode(Node):
    def __init__(self):
        super().__init__('ultrasonic_sensor_node')
        self.publisher_ = self.create_publisher(Float32, 'ultrasonic_distance', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        distance = float(random.randint(10, 100)) #Симуляция
        msg = Float32()
        msg.data = distance
        self.publisher_.publish(msg)
        self.get_logger().info(f'Distance: {distance}')

def main(args=None):
    rclpy.init(args=args)
    ultrasonic_sensor_node = UltrasonicSensorNode()
    rclpy.spin(ultrasonic_sensor_node)
    ultrasonic_sensor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
