#!/usr/bin/env python3

from distutils.core import setup

setup(
        name='redp', 
        version='0.1', 
        description='Converts reddit submissions and comments to a maildir', 
        author='Peter J. Schroeder', 
        author_email='peterjschroeder@gmail.com', 
        url='https://github.com/peterjschroeder/redp',
        scripts=['redpick.py', 'redpull.py', 'redpush.py'],
        install_requires=['archivenow', 'asciimatics', 'better-profanity', 'configparser', 'gallery-dl', 'natsort', 'praw', 'psaw', 'python-pidfile', 'tqdm', 'xdg', 'youtube-dl']
)
