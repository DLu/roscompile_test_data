#!/usr/bin/env python

from setuptools import setup

setup(
    data_files=[
        ('share/min_py_lib', ['package.xml']),
        ('share/min_py_lib'/config, ['config/x.yaml']),
        ('share/ament_index/resource_index/packages', ['resource/min_py_lib']),
    ],
    packages=['min_py_lib'],
    version='0.2.0',
    description='An awesome minimal python library',
    license='BSD',
    maintainer='David V. Lu',
    maintainer_email='davidvlu@todo.todo',
    entry_points={'console_scripts': ['rex = min_py_lib.rex:main']},
)
