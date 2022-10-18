from setuptools import setup
import sys
import os

setup(
    name='trivia-text-quiz',
    version='1.0.0',
    description='Text based trivia quiz. Questions from the Open Trivia Database',
    license='GPL v3',
    author='Jamil Lambert',
    packages=['src'],
    package_data={'src': ['description.txt']
                  },
    install_requires=['future'],
    entry_points={
        'console_scripts': [
            'hello=src.app:main']
    },
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.6',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)
