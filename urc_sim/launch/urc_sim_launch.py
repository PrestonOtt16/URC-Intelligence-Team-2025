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
    pkgPath = FindPackageShare(package='urc_sim').find('urc_sim')
    urdfModelPath= os.path.join(pkgPath, 'urdf/rover_v1.urdf')
    
    
    #setting environment varible so gazebo can find my mesh files
    os.environ["GAZEBO_MODEL_PATH"] = os.path.join(get_package_share_directory('urc_sim'), 'meshes')
    
    with open(urdfModelPath,'r') as infp:
    	robot_desc = infp.read()
    
    params = {'robot_description': robot_desc}
    
    robot_state_publisher_node = Node(
      package='robot_state_publisher',
      executable='robot_state_publisher',
      output='screen',
      parameters=[params],
    )
    
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[params],
    )
    
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
    )
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(robot_state_publisher_node)
    ld.add_action(joint_state_publisher_node)
    ld.add_action(joint_state_publisher_gui_node)
    ld.add_action(rviz_node)
    
	
    return ld
			
