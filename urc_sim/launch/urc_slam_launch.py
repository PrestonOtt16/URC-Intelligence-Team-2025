from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution, LaunchConfiguration, Command
from ament_index_python.packages import get_package_share_directory
import os
import xacro


def generate_launch_description():
	
	pkg_gazebo_sims = get_package_share_directory('urc_sim')
	
	
	#Nodes for controlling turtlebot with ps4 controller, and plotting turtlebot odometry data
	#monitors the states of all buttons on controller and publishes them too joy msg
	n1 = Node(
		package = 'joy',
		executable = 'game_controller_node',
		output = 'screen'
		)
	#converts joy controller messages too Twsit msgs
	n2 = Node(
		package = 'teleop_twist_joy',
		executable = 'teleop_node',
		arguments = ['cmd_vel:=/commands/velocity'],
		parameters = [{
    		'scale_linear.x': 0.5,
    		'scale_angular.yaw': 1.0,
		}],
		output = 'screen'
		)
	
	#Running the rs_camera launch file too fetch images from intel realsense and publish them top ros2 topics
	lf1 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource([
			PathJoinSubstitution([
				FindPackageShare('realsense2_camera'),
					'launch',
					'rs_launch.py'
				])
			])
		)
	
	
	#Running the Kobuki launch file too setup control of turtlebot
	lf2 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource([
			PathJoinSubstitution([
				get_package_share_directory('kobuki_node'),
					'launch',
					'kobuki_node-launch.py'
				])
			])
		)
	
	#Running the static transform node too provide a transform between camera_depth_frame and /base_footprint frame for the SLAM node
	n3 = Node(
		package = 'urc_sim',
		executable = 'tf_cam_base_broadcaster',
		name = 'tf_cam_base_broadcaster_node',
		)
	
	#Running the depthimage too laserscan node too convert our depth image too a laser scan for the slam algorithm
	n4 = Node(
		package = 'depthimage_to_laserscan',
		executable = 'depthimage_to_laserscan_node',
		name = 'depth_img_lsr_node',
		arguments = ['depth:=/camera/camera/depth/image_rect_raw','depth_camera_info:=/camera/camera/depth/camera_info']
		)
	
	
	#Running the SLAM online_async_node too take in laserscans and odometry data too produce a map
	#Running the Kobuki launch file too setup control of turtlebot
	lf3 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource([
			PathJoinSubstitution([
				FindPackageShare('slam_toolbox'),
					'launch',
					'online_async_launch.py'
				])
			])
		)
		
		
	#Adding our processes into the launch description
	ld = LaunchDescription()
	ld.add_action(n1)
	ld.add_action(n2)
	ld.add_action(lf1)
	ld.add_action(lf2)
	ld.add_action(n3)
	ld.add_action(n4)
	ld.add_action(lf3)
	
	return ld
			
