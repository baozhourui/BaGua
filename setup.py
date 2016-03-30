#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
import bagua

setup(
    name         = 'BaGua',
    version      = bagua.__version__,
    author       = 'Floyda',
    author_email = 'floyda@163.com',
    license      = 'MIT',
    description  = '科学占卜, 计算机算命.',
    long_description = '科学占卜, 计算机算命...',
    keywords='chinese bagua yijing zhouyi',
    url          = 'https://github.com/FloydaGithub/BaGua',
    packages=[
        'bagua',
        'bagua.docs',
    ],
    package_data = {
        'bagua.docs': ['*.txt'],
        'bagua': ['*.txt'],
    },
    install_requires = [
        'docopt >= 0.6.1',
    ],
    scripts          = ['bin/bagua'],
    # entry_points={
    #     'console_scripts':[
    #     ]
    #   },
)
