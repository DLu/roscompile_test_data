#!/usr/bin/env python

from setuptools import setup

package_name = 'min_py_lib'

setup(
    name=package_name,
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages', ['resource/min_py_lib']),
    ],
    packages=[package_name],
    entry_points={'console_scripts': ['rex = min_py_lib.rex:main']},
)
