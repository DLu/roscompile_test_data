#!/usr/bin/env python

from setuptools import setup

package_name = 'my_minimal_python'

setup(
    name=package_name,
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages', ['resource/my_minimal_python']),
    ],
    scripts=['scripts/node.py'],
)
