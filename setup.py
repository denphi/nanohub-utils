#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function
from glob import glob
from os.path import join as pjoin
from os.path import realpath
import io

from setuptools import setup, find_packages

def get_version(file, name='__version__'):
    """Get the version of the package from the given file by
    executing it and extracting the given `name`.
    """
    path = realpath(file)
    version_ns = {}
    with io.open(path, encoding="utf8") as f:
        exec(f.read(), {}, version_ns)
    return version_ns[name]

# The name of the project
name = 'nanohub-utils'

# Get our version
version = get_version(pjoin('nanohub', '_version.py'))

long_description = ""
with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = {
    'name'            : name,
    'description'     : 'A set of tools created by nanoHUB',
    'long_description_content_type' : 'text/markdown',
    'long_description':long_description,
    'version'         : version,
    'scripts'         : glob(pjoin('scripts', '*')),
    'packages'        : find_packages(),
    'data_files'      : [('assets', [
                        ])],
    'author'          : 'nanoHUB contributor',
    'author_email'    : 'denphi@denphi.com',
    'url'             : 'https://github.com/denphi/nanohub',
    'license'         : 'BSD',
    'platforms'       : "Linux, Mac OS X, Windows",
    'keywords'        : ['IPython'],
    'classifiers'     : [
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Jupyter',
    ],
    'include_package_data' : True,
    'install_requires' : [
	    'nanohub.remote>=0.1.0',
	    'nanohub.uidl>=0.1.6',
	    'sim2lbuilder>=0.0.6',
        'nanohubtools>=0.2.3'
        'nanohubthemes>=0.0.5'
    ],
    'extras_require' : {
        'test': [
        ],
        'examples': [
        ],
        'docs': [
        ],
    },
    'entry_points' : {
    },
}

if __name__ == '__main__':
    setup(**setup_args)
