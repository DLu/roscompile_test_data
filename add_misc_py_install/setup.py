#!/usr/bin/env python

from setuptools import setup
from glob import glob

package_name = 'my_minimal_python'

setup(
    name=package_name,
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages', ['resource/my_minimal_python']),
        ('share/' + package_name + '/launch', ['launch/core.launch']),
        ('share/' + package_name + '/urdf', glob('urdf/*urdf')),
    ],
)
