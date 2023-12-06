from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    robot_description = ParameterValue(
        Command(['xacro ', PathJoinSubstitution(FindPackageShare('donatello'), 'urdf', '01-myfirst.urdf')]),
        value_type=str)
    return LaunchDescription([
        IncludeLaunchDescription(PathJoinSubstitution(FindPackageShare('donatello'), 'launch', '05-arg.launch.py'),
                                 launch_arguments={'pizza_type': 'peppers', 'robot_description': robot_description}.items()),
    ])
