from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
	name='cocotask',
    
	version='0.1.0.4',
    
    description='A Framework for handling multiple Rabbitmq consumers using Pika',
    long_description=long_description,
    long_description_content_type='text/markdown', 

    url='https://github.com/likexx/cocotask',
    
    author='Like Zhang',
    
    author_email='zlike@yahoo.com',

    license='MIT',
    
#    packages=[''],
    packages=find_packages(exclude=['release.sh']),

    zip_safe=False,
      
    entry_points={
        'console_scripts': [
            'cocotask = taskrunner:main',
        ],
    },

	keywords='A Framework for handling multiple Rabbitmq consumers using Pika',
    
    install_requires=['pika'],

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/likexx/cocotask/issues',
        'Funding': 'https://github.com/likexx/cocotask/',
        'Say Thanks!': 'https://github.com/likexx/cocotask/',
        'Source': 'https://github.com/likexx/cocotask/',
    },
)

