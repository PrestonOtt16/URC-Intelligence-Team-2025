#dependency for generating python classes from ros2 msg types
#from rosidl_runtime_py import generate_distutils_setup
from setuptools import setup, find_packages, Extension

package_name = 'aruco_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='preston',
    maintainer_email='prestonottsuperluminal@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'aruco_node = aruco_ros.aruco_node:main',
        ],
    },
    
)
