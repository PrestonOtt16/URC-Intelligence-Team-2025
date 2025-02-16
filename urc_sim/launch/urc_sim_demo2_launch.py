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
	#creating a path too a ROS2 pkg
	pkg_gazebo_sims = get_package_share_directory('urc_sim')
	#creating a path too a world
	world_file = os.path.join(pkg_gazebo_sims, 'world','empty_world.world')
	#creating a path too a urdf
	urdf_file = os.path.join(pkg_gazebo_sims,'urdf','demo_block2.xacro.urdf')
	
	#setting environment varible so gazebo can find my mesh files
	os.environ["GAZEBO_MODEL_PATH"] = os.path.join(get_package_share_directory('urc_sim'), 'meshes')
	
	
	#xacro file path too urdf
	xacro_file = os.path.join(pkg_gazebo_sims,
                              'urdf',
                              'demo_block2.xacro.urdf')
	
	#reading xacro file into a parameter
	doc = xacro.parse(open(xacro_file))
	xacro.process_doc(doc)
	params = {'robot_description': doc.toxml()}
		
	
	
	#creating a arugument for path world file
	declare_world_cmd = DeclareLaunchArgument(
		'world',
		default_value = world_file,
		description = 'empty world SDF')
		
	#Defining a argument for the path to the marker sdf file
	#sdf_model_path = "/home/preston/urc_navigation/src/urc_slam/urdf/demo_block3.sdf"
	sdf_model_path = os.path.join(pkg_gazebo_sims,'urdf','demo_block3.sdf')
	sdf_model = LaunchConfiguration('sdf_model')
	declare_sdf_model_path_cmd = DeclareLaunchArgument(
		name='sdf_model', 
		default_value=sdf_model_path, 
		description='Absolute path to robot sdf file')
		
	#Running spawn entity node too spawn test urdf into Gazebo	
	n2 = Node(
		package = 'gazebo_ros',
		executable = 'spawn_entity.py',
		arguments = ['-topic','robot_description','-entity','friction-model','-x','0','-y','0','-z','0.5'],
		output = 'screen'
		)
	
	#The spawn point for the marker urdf 10cm above ground and -2.0m from small-boi
	n3 = Node(
		package = 'gazebo_ros',
		executable = 'spawn_entity.py',
		arguments = ['-file',sdf_model,'-entity','fricton-model2','-x','1.0','-y','0.0','-z','0.10'],
		output = 'screen'
		)
		
	
	#Running robot state publisher too publish tf and joint states of urdf
	n1 = Node(
		package = 'robot_state_publisher',
		executable = 'robot_state_publisher',
		name = 'robot_state_publisher',
		parameters = [params],
		#parameters = [{'robot_description': params, 'use_sim_time': True}],
		output = 'screen'
		)
		
	
	lf1 = IncludeLaunchDescription(
		PythonLaunchDescriptionSource([
			PathJoinSubstitution([
				FindPackageShare('gazebo_ros'),
					'launch',
					'gazebo.launch.py'
				])
			])
		,launch_arguments = {'world' : LaunchConfiguration('world') ,'pause' : 'true'}.items())
	
		
	ld = LaunchDescription()
	ld.add_action(declare_world_cmd)
	ld.add_action(declare_sdf_model_path_cmd)
	ld.add_action(n1)
	ld.add_action(lf1)
	ld.add_action(n2)
	ld.add_action(n3)
	
	return ld
			
