#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Cave divers is a text based game about underwater caves and people lurking in them.',
    'author': 'ioana manoliu',
    'url': '',
    'download_url': 'https://lab.learncodethehardway.com/ioio/lpthw/ex46',
    'author_email': 'io.manoliu@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['cave_divers'],
    'scripts': ['bin/cave_divers'],
    'name': 'Cave Divers'
}

setup(**config)
