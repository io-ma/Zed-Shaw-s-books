try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'io.manoliu@gmail.com',
    'url': '../',
    'download_url': 'https://lab.learncodethehardway.com/ioio/lpthw',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'name'
}

setup(**config)
