#!/usr/bin/env python

from setuptools import setup

package_name = 'min_py_src_lib'

setup(
    name=package_name,
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages', ['resource/min_py_src_lib']),
    ],
    packages=['min_py_src_lib'],
    package_dir={'': 'src'},
    entry_points={'console_scripts': ['rex = min_py_src_lib.rex:main']},
)
