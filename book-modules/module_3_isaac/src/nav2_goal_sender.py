import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose

class Nav2GoalSender(Node):
    def __init__(self):
        super().__init__('nav2_goal_sender')
        self.get_logger().info('Nav2 Goal Sender Node (Conceptual Placeholder) Started.')
        self._action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def send_goal(self, x, y, yaw):
        self.get_logger().info(f'Waiting for "navigate_to_pose" action server...')
        self._action_client.wait_for_server()

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.z = math.sin(yaw / 2.0)
        goal_msg.pose.pose.orientation.w = math.cos(yaw / 2.0)

        self.get_logger().info('Sending goal to Nav2...')
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        status = future.result().status
        if status == ActionStatus.SUCCEEDED:
            self.get_logger().info('Goal succeeded! Result: {0}'.format(result.results_field_name))
        else:
            self.get_logger().info('Goal failed with status: {0}'.format(status))
        rclpy.shutdown()

import math
from action_msgs.msg import GoalStatus # Import ActionStatus for comparison

def main(args=None):
    rclpy.init(args=args)
    node = Nav2GoalSender()
    
    # Example: Send a goal to (5, 5) with 0 yaw (facing x-axis)
    node.send_goal(5.0, 5.0, 0.0)
    
    rclpy.spin(node)
    
    # Note: Shutdown is called in get_result_callback, but good practice to have here too
    if rclpy.ok():
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
