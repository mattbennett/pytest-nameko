from setuptools import setup

setup(
    name="pytest-nameko",
    version='0.0.1',
    description='Pytest plugin providing default configuration and fixtures '
                'for testing nameko services',
    author='Matt Bennett',
    author_email='matt@bennett.name',
    url='http://github.com/nameko/pytest-nameko',

    py_modules=['pytest_nameko'],

    install_requires=[
        "pytest",
        "nameko"
    ],
    extras_require={
            'dev': [
                "urllib3==1.10.2",
                "websocket-client==0.23.0",
            ],
        },

    # the following makes a plugin available to pytest
    entry_points={
        'pytest11': [
            'pytest_nameko = pytest_nameko',
        ]
    },
)
