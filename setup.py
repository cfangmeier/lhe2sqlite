from setuptools import setup
from lhe2sqlite import __version__

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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='lhe sqlite',
    packages=['lhe2sqlite'],
    package_dir={'lhe2sqlite': 'lhe2sqlite'},
    scripts=[
        'scripts/convertlhe2sqlite',
    ],
)
