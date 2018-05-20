from setuptools import setup, find_packages

setup(
	name='cocotask',
    
	version='0.1.0.0',
    
    description='A Framework for handling multiple Rabbitmq consumers using Pika',
    
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

