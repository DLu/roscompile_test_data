#!/usr/bin/env python

from setuptools import setup

package_name = 'my_cpp_py_pkg'

setup(
    name=package_name,
    data_files=[('share/' + package_name, ['package.xml'])],
    packages=[package_name],
)
