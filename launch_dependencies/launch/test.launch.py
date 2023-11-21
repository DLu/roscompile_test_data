import os.path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        Node(name='cool_but_rude',
             package='raphael',
             executable='raphael_node',
             parameters=[os.path.join(get_package_share_directory('leonardo'),
                 'config/params.yaml'
                 )
    ]),
    ])
 
