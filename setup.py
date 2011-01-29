#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='slacklog',
    version='0.0.1',
    author='Mikko Värri',
    author_email='vmj@linuxbox.fi',
    maintainer='Mikko Värri',
    maintainer_email='vmj@linuxbox.fi',
    packages=['slacklog',],
    scripts=['bin/slacklog2rss',],
    url='http://pypi.python.org/pypi/slacklog/',
    license='GNU GPLv3',
    description='Convert Slackware ChangeLog to RSS',
    long_description=''.join([
            open('README.rst').read(),
            '\n\n',
            open('CHANGES.rst').read()
            ]),
    requires=['dateutil',],
    )
