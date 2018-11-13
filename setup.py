from setuptools import setup
from vitex import __version__

import sys

if sys.version_info < (3, 6):
    print('vitex requires python>=3.6.')
    exit(1)

with open('README.md') as f:
    desc = f.read()

setup(
    name='lhe2sqlite',
    version=__version__,
    description='Simple utility to convert LesHouchesEvents files to a sqlite database',
    long_description=desc,
    long_description_content_type='text/markdown',
    url='https://github.com/cfangmeier/lhe2sqlite',
    author='Caleb Fangmeier',
    author_email='caleb@fangmeier.tech',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='lhe sqlite',
    packages=['lhe2sqlite'],
    package_dir={'lhe2sqlite': 'lhe2sqlite'},
    scripts=[
        'scripts/convertlhe2sqlite',
    ],
)
