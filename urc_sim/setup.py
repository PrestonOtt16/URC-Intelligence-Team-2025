from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'urc_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        ('share/' + package_name, ['package.xml']),
    	(os.path.join('share', package_name, 'urdf'), glob('urdf/*.[uU][rR][dD][fF]')),
    	(os.path.join('share',package_name,'world'), glob(os.path.join('world','desert.world'))),
    	(os.path.join('share',package_name,'world'), glob(os.path.join('world','empty_world.sdf'))),
    	(os.path.join('share',package_name,'world'), glob(os.path.join('world','demo_block3.sdf'))),
    	(os.path.join('share',package_name,'world'), glob(os.path.join('world','demo_block4.sdf'))),
    	(os.path.join('share',package_name,'world'), glob(os.path.join('world','empty_world.world'))),
    	(os.path.join('share',package_name,'world'), glob(os.path.join('world','rover_primal.world'))),
    	(os.path.join('share',package_name,'config'), glob(os.path.join('config','rover_primal_fr.yaml'))),
    	(os.path.join('share',package_name,'config'), glob(os.path.join('config','rover_primal_br.yaml'))),
    	(os.path.join('share',package_name,'config'), glob(os.path.join('config','rover_primal_fl.yaml'))),
    	(os.path.join('share',package_name,'config'), glob(os.path.join('config','rover_primal_bl.yaml'))),
    	(os.path.join('share',package_name,'meshes'), glob(os.path.join('meshes','Mars-Desert-Research-Station.stl'))),
    	(os.path.join('share',package_name,'meshes'), glob(os.path.join('meshes','2020+400mm.stl'))),
    	('share/' + package_name + '/meshes', glob('meshes/*')),
    	(os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
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
        'clock_node = urc_sim.clock:main',
        'tf_cam_base_broadcaster = urc_sim.tf_cam_base_broadcaster:main',
        ],
    },
)
