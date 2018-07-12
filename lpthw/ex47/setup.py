try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'small project to test',
    'author': 'ioana manoliu',
    'url': '',
    'download_url': 'https://lab.learncodethehardway.com/ioio/lpthw',
    'author_email': 'io.manoliu@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
