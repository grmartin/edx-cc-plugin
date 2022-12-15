#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=open-builtin,native-string
"""
Package metadata for openedx_export_plugins.
"""


import os
import re
import sys

from setuptools import setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.

    Returns:
        list: Requirements file relative path strings
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.split('#')[0].strip() for line in open(path).readlines()
            if is_requirement(line.strip())
        )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement.

    Returns:
        bool: True if the line is not blank, a comment, a URL, or an included file
    """
    return line and not line.startswith(('-r', '#', '-e', 'git+', '-c'))


VERSION = get_version('openedx_export_plugins', '__init__.py')

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
CHANGELOG = open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.rst')).read()

setup(
    name='twou-titan-plugin',
    version=VERSION,
    description="""...TBD...""",
    long_description=README + '\n\n' + CHANGELOG,
    author='Purchase Squad',
    author_email='',
    url='',
    packages=[
        "twou-titan-plugin",
    ],
    include_package_data=True,
    install_requires=load_requirements('requirements/base.in'),
    license="Proprietary", # Internal to 2U Only.
    zip_safe=False,
    keywords='edx-commerce-coordinator-plugin plugin',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Private :: Do Not Upload',
    ],
    entry_points={
        "commerce-coordinator.djangoapp": [
            "twou-titan-plugins = twou-titan-plugin.apps:OpenedxExportPluginsConfig",
        ]
    }
)
