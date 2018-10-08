from setuptools import find_packages
from setuptools import setup

setup(
    name='models',
    version='1.11',
    include_package_data=True,
    packages=setuptools.find_packages(exclude=["samples", "tutorials"]),
    description='Models built with TensorFlow'
)