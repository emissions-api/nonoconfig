from setuptools import setup, find_packages
import os

path = os.path.abspath(os.path.dirname(__file__))


def read(filename):
    with open(os.path.join(path, filename), encoding='utf-8') as f:
        return f.read()


setup(
    name='nonoconfig',
    author='Emissions API Developers',
    license='MIT',
    version='0.1',
    url='https://github.com/emissions-api/nonoconfig',
    packages=find_packages(),
    install_requires=['pyyaml'],
    description="Zero configuration configuration library",
    long_description=read('README.md'),
    long_description_content_type='text/x-markdown',
)
