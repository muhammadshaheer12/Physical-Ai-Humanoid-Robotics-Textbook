import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

class JointCommandPublisher(Node):
    def __init__(self):
        super().__init__('joint_command_publisher')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_callback) # Publish at 10 Hz
        self.current_angle = 0.0
        self.joint_name = 'joint1' # Name of the joint in robot.urdf

    def timer_callback(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [self.joint_name]
        
        # Simple oscillation for demonstration
        self.current_angle = math.sin(self.get_clock().now().nanoseconds / 1e9) * 1.0 # Oscillate between -1.0 and 1.0 radian
        msg.position = [self.current_angle]
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing JointState: {self.joint_name}={self.current_angle:.2f}')

def main(args=None):
    rclpy.init(args=args)
    joint_command_publisher = JointCommandPublisher()
    rclpy.spin(joint_command_publisher)
    joint_command_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
