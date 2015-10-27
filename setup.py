#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='kiga_plugin',
    version='0.0.1',
    description='plugin loader using pkg_resources.',
    author='succhiello',
    author_email='succhiello@gmail.com',
    url='https://github.com/succhiello/kiga-plugin',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
    ],
    packages=find_packages(),
)
